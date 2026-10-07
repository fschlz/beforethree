"""Build Before Three: content/*.md -> one self-contained index.html.

Content format (per section file):
  === section-id | Section title        (section summary follows)
  --- category-id | Category title      (category summary follows)
  +++ topic-id | Topic title            (@key: value metadata, then ## What / ## Why / ## How / ## Around the world)
"""
import html
import pathlib
import re
import sys

import markdown

ROOT = pathlib.Path(__file__).parent
CONTENT = ROOT / "content"
import os
SITE_URL = os.environ.get("SITE_URL", "").rstrip("/")   # e.g. https://beforethree.xyz
OUT = pathlib.Path(os.environ.get("OUT", str(ROOT.parent / "index.html")))
OUT_DIR = OUT.parent

SECTION_FILES = ["gear", "nutrition", "care", "parenting"]
STAGES = [
    ("pre", "Planning"),
    ("preg", "Pregnancy"),
    ("birth", "Birth"),
    ("0-6m", "0-6 months"),
    ("6-12m", "6-12 months"),
    ("1-3y", "1-3 years"),
]
STAGE_LABEL = dict(STAGES)
EVIDENCE = {
    "strong": "Strong evidence",
    "moderate": "Moderate evidence",
    "debated": "Debated",
}
PARTS = [
    ("What", "what", "What"),
    ("Why", "why", "Why <small>1st, 2nd and 3rd order effects</small>"),
    ("How", "how", "How"),
    ("Around the world", "culture", "Around the world"),
]

errors = []

BOOKS = {}          # title -> {id, title, author, year, weight, link, body}
BOOK_LIST = []
BOOK_USAGE = {}     # title -> [topic ids]
TOPIC_INDEX = {}
EVLABEL = {"fits": "Fits the evidence", "partly": "Partly supported", "conflicts": "Conflicts with guidance"}
WEIGHT = {"core": "Core source", "background": "Background", "caution": "Used with caution"}
OTHER_CITES = {"American Pregnancy Association", "Some Montessori sources"}
CITE_RE = re.compile(r"\[\[([^\[\]]+?);\s*(fits|partly|conflicts)\]\]")


def note_usage(title, topic_id):
    used = BOOK_USAGE.setdefault(title, [])
    if topic_id not in used:
        used.append(topic_id)


def render_cites(text, topic_id, cited):
    def sub(m):
        names = [n.strip() for n in m.group(1).split(",") if n.strip()]
        parts = []
        for n in names:
            book = BOOKS.get(n)
            if book:
                note_usage(n, topic_id)
                if n not in cited:
                    cited.append(n)
                parts.append('<a href="#%s">%s</a>' % (book["id"], esc(n)))
            elif n in OTHER_CITES:
                parts.append(esc(n[0].lower() + n[1:]) if n.startswith("Some ") else "the " + esc(n))
            else:
                errors.append("%s: unknown cited source %r" % (topic_id, n))
                parts.append(esc(n))
        src = parts[0] if len(parts) == 1 else ", ".join(parts[:-1]) + " and " + parts[-1]
        ev = m.group(2)
        return ('<span class="cite"><span class="cite-src">From %s</span> '
                '<span class="cite-ev ev-%s">%s</span></span>') % (src, ev, EVLABEL[ev])
    return CITE_RE.sub(sub, text)


def parse_books():
    text = (CONTENT / "books.md").read_text()
    head, _, rest = text.partition("\n+++ ")
    rest = "+++ " + rest
    rest, _, conflicts = rest.partition("\n--- conflicts")
    for chunk in re.split(r"\n(?=\+\+\+ )", rest.strip()):
        lines = chunk.split("\n")
        slug_, title = [x.strip() for x in lines[0][4:].split("|", 1)]
        meta, body = {}, []
        for line in lines[1:]:
            if line.startswith("@") and not body:
                k, v = line[1:].split(":", 1)
                meta[k.strip()] = v.strip()
            else:
                body.append(line)
        book = {"id": "books--" + slug_, "title": title, "author": meta.get("author", ""),
                "year": meta.get("year", ""), "weight": meta.get("weight", "background"),
                "link": meta.get("link", ""), "body": "\n".join(body).strip()}
        if book["weight"] not in WEIGHT:
            errors.append("book %s: unknown weight" % title)
        BOOKS[title] = book
        BOOK_LIST.append(book)
    return head, conflicts


def render_books(head, conflicts):
    out = [md(head).replace("<h2>", '<h2 id="books-h">', 1)]
    for book in BOOK_LIST:
        out.append('<article class="book w-%s" id="%s">' % (book["weight"], book["id"]))
        out.append('<div class="book-head"><h3>%s</h3><span class="badge w-%s">%s</span></div>'
                   % (esc(book["title"]), book["weight"], WEIGHT[book["weight"]]))
        out.append('<p class="book-meta">%s, %s</p>' % (esc(book["author"]), esc(book["year"])))
        out.append('<div class="book-body">%s</div>' % md(book["body"]))
        if book["link"]:
            label, url = [x.strip() for x in book["link"].split("|", 1)]
            out.append('<p class="book-link"><a href="%s" rel="noopener" target="_blank">%s</a></p>' % (esc(url), esc(label)))
        used = BOOK_USAGE.get(book["title"], [])
        if used:
            chips = "".join('<a class="chip s-%s" href="#%s"><span class="chip-sec">%s:</span> %s</a>'
                            % (TOPIC_INDEX[u]["sec"], u, esc(TOPIC_INDEX[u]["sec_title"]), esc(TOPIC_INDEX[u]["title"]))
                            for u in used)
            out.append('<nav class="related book-used" aria-label="Topics that use this book">'
                       '<span class="rel-label">Used in</span>%s</nav>' % chips)
        else:
            errors.append("book %s is not used anywhere" % book["title"])
        out.append("</article>")
    out.append('<div class="book-conflicts">%s</div>' % md(conflicts))
    return "".join(out)


# ---------- markdown helpers ----------

def fix_blocks(text):
    """Python-Markdown needs blank lines before lists and tables."""
    out = []
    for line in text.split("\n"):
        prev = out[-1] if out else ""
        is_item = line.startswith("- ")
        is_table = line.startswith("|")
        prev_is_item = re.match(r"^\s*- ", prev) is not None
        if is_item and prev.strip() and not prev_is_item and not prev.startswith("    "):
            out.append("")
        if is_table and prev.strip() and not prev.startswith("|"):
            out.append("")
        if line.strip() and not is_table and prev.startswith("|"):
            out.append("")
        out.append(line)
    return "\n".join(out)


def md(text):
    rendered = markdown.markdown(
        fix_blocks(text.strip()),
        extensions=["tables", "def_list"],
        output_format="html",
    )
    rendered = rendered.replace("<table>", '<div class="table-wrap"><table>')
    rendered = rendered.replace("</table>", "</table></div>")
    return rendered


def verdict_marks(text):
    """Prefix each 'Around the world' bullet with a Helps / Backfires / Mixed / Borrow label."""
    out = []
    for line in text.split("\n"):
        if line.startswith("- "):
            low = line.lower()
            label = None
            helps = re.search(r"\bhelps?\b", low) is not None
            if low.startswith("- **the common thread"):
                label = None
            elif low.startswith("- **what to borrow") or low.startswith("- **what we suggest"):
                label = ("borrow", "Borrow")
            elif "backfire" in low and (helps or "harmless" in low or "partly" in low):
                label = ("mixed", "Mixed")
            elif "backfire" in low:
                label = ("backfires", "Backfires")
            elif helps:
                label = ("helps", "Helps")
            if label:
                line = '- <span class="verdict v-%s">%s</span> %s' % (label[0], label[1], line[2:])
        out.append(line)
    return "\n".join(out)


# ---------- parsing ----------

def parse_section(path):
    sec = None
    cur = None
    for raw in path.read_text().split("\n"):
        line = raw.rstrip()
        if line.startswith("=== "):
            sid, title = [x.strip() for x in line[4:].split("|", 1)]
            sec = {"id": sid, "title": title, "summary": [], "cats": []}
            cur = sec
        elif line.startswith("--- "):
            cid, title = [x.strip() for x in line[4:].split("|", 1)]
            cat = {"id": "%s--%s" % (sec["id"], cid), "title": title, "summary": [], "topics": [], "sec": sec["id"]}
            sec["cats"].append(cat)
            cur = cat
        elif line.startswith("+++ "):
            tid, title = [x.strip() for x in line[4:].split("|", 1)]
            cat = sec["cats"][-1]
            topic = {"id": "%s--%s" % (cat["id"], tid), "title": title, "meta": {}, "body": [],
                     "sec": sec["id"], "cat": cat["id"]}
            cat["topics"].append(topic)
            cur = topic
        elif cur is not None and "meta" in cur and line.startswith("@") and not cur["body"]:
            key, val = line[1:].split(":", 1)
            cur["meta"][key.strip()] = val.strip()
        elif cur is not None:
            (cur["body"] if "meta" in cur else cur["summary"]).append(line)
    return sec


def split_parts(body_lines):
    parts, key, buf = {}, None, []
    for line in body_lines:
        m = re.match(r"^## (.+)$", line)
        if m:
            if key:
                parts[key] = "\n".join(buf).strip()
            key, buf = m.group(1).strip(), []
        else:
            buf.append(line)
    if key:
        parts[key] = "\n".join(buf).strip()
    return parts


# ---------- rendering ----------

def esc(s):
    return html.escape(s, quote=True)


def render_topic(t, index):
    meta = t["meta"]
    stages = [s.strip() for s in meta.get("stages", "").split(",") if s.strip()]
    for s in stages:
        if s not in STAGE_LABEL:
            errors.append("%s: unknown stage %r" % (t["id"], s))
    ev = meta.get("evidence", "moderate")
    if ev not in EVIDENCE:
        errors.append("%s: unknown evidence %r" % (t["id"], ev))
    flags = [f.strip() for f in meta.get("flags", "").split(",") if f.strip()]
    parts = split_parts(t["body"])
    for need in ("What", "Why", "How"):
        if need not in parts:
            errors.append("%s: missing ## %s" % (t["id"], need))
    why = parts.get("Why", "")
    for order in ("1st order", "2nd order", "3rd order"):
        if order not in why:
            errors.append("%s: Why is missing %s" % (t["id"], order))

    badges = ['<span class="badge ev-%s">%s</span>' % (ev, EVIDENCE.get(ev, ev))]
    if "safety" in flags:
        badges.append('<span class="badge safety">Safety first</span>')

    body = []
    cited = []
    body.append('<p class="t-stages"><span>Stages:</span> %s</p>'
                % esc(", ".join(STAGE_LABEL.get(s, s) for s in stages)))
    for key, slug, label in PARTS:
        if key not in parts:
            continue
        content = parts[key]
        if slug == "culture":
            content = verdict_marks(content)
        content = render_cites(content, t["id"], cited)
        body.append('<section class="part %s" id="%s-%s"><h5>%s</h5>%s</section>'
                    % (slug, t["id"], slug, label, md(content)))

    related = [r.strip() for r in meta.get("related", "").split(",") if r.strip()]
    if related:
        chips = []
        for rid in related:
            target = index.get(rid)
            if not target:
                errors.append("%s: related id not found %r" % (t["id"], rid))
                continue
            chips.append('<a class="chip s-%s" href="#%s"><span class="chip-sec">%s:</span> %s</a>'
                         % (target["sec"], rid, esc(target["sec_title"]), esc(target["title"])))
        body.append('<nav class="related" aria-label="Related topics"><span class="rel-label">Related</span>%s</nav>'
                    % "".join(chips))

    sources = [s.strip() for s in meta.get("sources", "").split(";;") if s.strip()]
    listed_books = [s[5:].strip() for s in sources if s.startswith("Book:")]
    for title in cited:
        if title not in listed_books:
            sources.append("Book: " + title)
    if sources:
        items, has_book = [], False
        for s in sources:
            if s.startswith("Book:"):
                title = s[5:].strip()
                book = BOOKS.get(title)
                if not book:
                    errors.append("%s: unknown book in sources %r" % (t["id"], title))
                    continue
                has_book = True
                note_usage(title, t["id"])
                items.append('<li><span class="src-book">Book</span> <a href="#%s">%s</a>, %s</li>'
                             % (book["id"], esc(title), esc(book["author"])))
            else:
                title, url = [x.strip() for x in s.split("|", 1)]
                items.append('<li><a href="%s" rel="noopener" target="_blank">%s</a></li>' % (esc(url), esc(title)))
        label = "Sources and books" if has_book else "Sources"
        body.append('<details class="sources"><summary>%s</summary><ul>%s</ul></details>' % (label, "".join(items)))

    return (
        '<details class="topic s-{sec}" id="{id}" data-stages="{stages}">'
        '<summary><span class="t-main"><h4 class="t-title">{title}</h4>'
        '<span class="t-teaser">{teaser}</span><span class="t-badges">{badges}</span></span>'
        '<span class="t-toggle" aria-hidden="true"></span></summary>'
        '<div class="t-body">{body}</div></details>'
    ).format(sec=t["sec"], id=t["id"], stages=" ".join(stages), title=esc(t["title"]),
             teaser=esc(meta.get("teaser", "")), badges="".join(badges), body="".join(body))


def render_section(sec, index):
    out = ['<section class="sec s-{id}" id="{id}" aria-labelledby="{id}-h">'.format(id=sec["id"])]
    out.append('<header class="sec-head"><h2 id="%s-h">%s</h2><div class="sec-sum">%s</div></header>'
               % (sec["id"], esc(sec["title"]), md("\n".join(sec["summary"]))))
    for cat in sec["cats"]:
        static = not cat["topics"]
        cls = "cat static" if static else "cat"
        if cat["id"].endswith("--skip"):
            cls += " cat-skip"
        out.append('<div class="%s" id="%s">' % (cls, cat["id"]))
        summary_html = md("\n".join(cat["summary"]))
        if "cat-skip" in cls:
            def mark(m):
                verdict = m.group(2)
                kind = "danger" if re.match(r"(Banned|Unsafe)", verdict) else (
                    "warn" if re.match(r"(Avoid|Misleading|Limit)", verdict) else "meh")
                return '%s<td class="v-%s">%s</td>' % (m.group(1), kind, verdict)
            summary_html = re.sub(r"(<tr>\s*<td>.*?</td>\s*)<td>(.*?)</td>", mark, summary_html, flags=re.S)
        out.append('<div class="cat-head"><h3>%s</h3><div class="cat-sum">%s</div></div>'
                   % (esc(cat["title"]), summary_html))
        if cat["topics"]:
            out.append('<div class="topics">%s</div>' % "".join(render_topic(t, index) for t in cat["topics"]))
        out.append("</div>")
    out.append("</section>")
    return "".join(out)


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def render_checklist(block):
    groups, cur = [], None
    for line in block.split("\n"):
        line = line.strip()
        if line.startswith("### "):
            cur = {"title": line[4:], "items": []}
            groups.append(cur)
        elif line.startswith("- ") and cur is not None:
            cur["items"].append(line[2:])
    out = ['<div class="checklist">']
    for g in groups:
        out.append('<div class="cl-group"><h4>%s</h4><ul>' % esc(g["title"]))
        for item in g["items"]:
            key = slug(g["title"]) + "--" + slug(item)[:48]
            out.append('<li><label><input type="checkbox" data-key="%s"> <span>%s</span></label></li>'
                       % (key, esc(item)))
        out.append("</ul></div>")
    out.append("</div>")
    return "".join(out)


def render_intro():
    text = (CONTENT / "intro.md").read_text()
    m = re.search(r"\[\[checklist\]\](.*?)\[\[/checklist\]\]", text, re.S)
    checklist = render_checklist(m.group(1)) if m else ""
    text = text.replace(m.group(0), "CHECKLISTTOKEN") if m else text
    out = md(text).replace("<p>CHECKLISTTOKEN</p>", checklist)
    return out


def render_glossary():
    text = (CONTENT / "glossary.md").read_text().strip()
    entries = []
    for block in re.split(r"\n\s*\n", text):
        lines = block.strip().split("\n")
        term = lines[0].strip()
        definition = " ".join(l.strip().lstrip(":").strip() for l in lines[1:])
        entries.append((term, definition))
    entries.sort(key=lambda e: e[0].lower())
    out = ['<dl class="glossary-list">']
    for term, definition in entries:
        out.append('<div class="g-item" id="g-%s"><dt>%s</dt><dd>%s</dd></div>'
                   % (slug(term), esc(term), esc(definition)))
    out.append("</dl>")
    return "".join(out)


def build():
    books_head, books_conflicts = parse_books()
    sections = [parse_section(CONTENT / ("%s.md" % f)) for f in SECTION_FILES]

    index = {}
    for sec in sections:
        for cat in sec["cats"]:
            index[cat["id"]] = {"title": cat["title"], "sec": sec["id"], "sec_title": sec["title"]}
            for t in cat["topics"]:
                index[t["id"]] = {"title": t["title"], "sec": sec["id"], "sec_title": sec["title"]}

    topic_count = sum(len(c["topics"]) for s in sections for c in s["cats"])
    TOPIC_INDEX.update(index)
    sections_html = "".join(render_section(s, index) for s in sections)
    books_html = render_books(books_head, books_conflicts)

    toc = ['<ul class="toc-list"><li><a href="#start">Start here</a></li>']
    for sec in sections:
        toc.append('<li class="toc-sec s-%s" data-for="%s"><a href="#%s">%s</a><ul>' % (sec["id"], sec["id"], sec["id"], esc(sec["title"])))
        for cat in sec["cats"]:
            toc.append('<li data-for="%s"><a href="#%s">%s</a></li>' % (cat["id"], cat["id"], esc(cat["title"])))
        toc.append("</ul></li>")
    toc.append('<li><a href="#books">Bookshelf</a></li><li><a href="#glossary">Glossary</a></li>'
               '<li><a href="#about">About this guide</a></li></ul>')

    tabs = "".join('<a class="tab s-%s" data-sec="%s" href="#%s">%s</a>' % (s["id"], s["id"], s["id"], esc(s["title"]))
                   for s in sections)
    rail_stages = "".join('<li><button type="button" data-stage="%s" aria-pressed="false">%s</button></li>' % (k, v)
                          for k, v in STAGES)
    hero_stages = "".join('<li><button type="button" data-stage="%s" data-hero="1">%s</button></li>' % (k, v)
                          for k, v in STAGES)

    page = TEMPLATE
    replacements = {
        "{{CSS}}": CSS,
        "{{JS}}": JS,
        "{{TABS}}": tabs,
        "{{RAIL_STAGES}}": rail_stages,
        "{{HERO_STAGES}}": hero_stages,
        "{{TOC}}": "".join(toc),
        "{{INTRO}}": render_intro(),
        "{{SECTIONS}}": sections_html,
        "{{BOOKS}}": books_html,
        "{{GLOSSARY}}": render_glossary(),
        "{{ABOUT}}": md((CONTENT / "about.md").read_text()),
        "{{TOPIC_COUNT}}": str(topic_count),
        "{{CANONICAL}}": ('<link rel="canonical" href="%s/">\n<meta property="og:url" content="%s/">\n' % (SITE_URL, SITE_URL)) if SITE_URL else "",
    }
    for k, v in replacements.items():
        page = page.replace(k, v)

    # ---------- validation ----------
    ids = set(re.findall(r'\bid="([^"]+)"', page))
    for href in re.findall(r'href="#([^"]*)"', page):
        if href and href not in ids:
            errors.append("broken internal link #%s" % href)
    dupes = [i for i in ids if page.count('id="%s"' % i) > 1]
    for d in dupes:
        errors.append("duplicate id %s" % d)
    for i, ch in enumerate(page):
        if ord(ch) > 127:
            errors.append("non-ASCII %r near: %s" % (ch, page[max(0, i - 40):i + 40].replace("\n", " ")))
    if "{{" in page:
        errors.append("unreplaced template token")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT.write_text(page)
    print("books:", len(BOOK_LIST), "| book uses:", {b["title"][:18]: len(BOOK_USAGE.get(b["title"], [])) for b in BOOK_LIST})
    print("topics:", topic_count, "| bytes:", len(page.encode()), "| internal links:",
          len(re.findall(r'href="#', page)))
    if errors:
        print("\n".join("ERROR: " + e for e in errors))
        sys.exit(1)
    print("OK")


from template import TEMPLATE, CSS, JS  # noqa: E402

if __name__ == "__main__":
    build()
