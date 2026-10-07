TEMPLATE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Before Three: a field guide for first-time parents</title>
<meta name="description" content="An evidence-based guide for first-time parents, from planning a pregnancy to age 3: gear, nutrition and exercise, care and parenting, with what works around the world.">
<meta name="theme-color" content="#F6F8F7">
<meta property="og:type" content="website">
<meta property="og:title" content="Before Three: a field guide for first-time parents">
<meta property="og:description" content="Evidence-based guidance from planning a pregnancy to age 3: gear, nutrition and exercise, care and parenting, with what works around the world.">
{{CANONICAL}}<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E%F0%9F%8C%B1%3C/text%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Literata:ital,opsz,wght@0,7..72,400..700;1,7..72,400..700&family=Schibsted+Grotesk:wght@400..800&display=swap">
<style>{{CSS}}</style>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-head">
  <div class="head-inner">
    <a class="brand" href="#top">Before Three</a>
    <nav class="tabs" aria-label="Sections">{{TABS}}<a class="tab" data-sec="books" href="#books">Books</a><a class="tab" data-sec="glossary" href="#glossary">Glossary</a></nav>
    <div class="head-actions">
      <button type="button" class="btn-plain" id="themeBtn">Dark mode</button>
      <button type="button" class="btn-plain menu-btn" id="menuBtn" aria-expanded="false" aria-controls="rail">Contents</button>
    </div>
  </div>
</header>
<div class="scrim" id="scrim" hidden></div>
<div class="layout">
  <aside class="rail" id="rail" aria-label="Search, filters and contents">
    <div class="rail-inner">
      <div class="rail-top">
        <label class="rail-label" for="q">Search topics</label>
        <button type="button" class="btn-plain close-btn" id="closeBtn">Close</button>
      </div>
      <input id="q" type="search" placeholder="Try stroller, peanut or sleep" autocomplete="off">
      <p class="rail-label" id="stageLabel">Filter by stage</p>
      <ul class="ruler" aria-labelledby="stageLabel">
        <li><button type="button" data-stage="all" aria-pressed="true">All stages</button></li>
        {{RAIL_STAGES}}
      </ul>
      <p class="count" id="count" aria-live="polite">{{TOPIC_COUNT}} topics</p>
      <div class="rail-tools">
        <button type="button" class="btn-line" id="expandAll">Open all</button>
        <button type="button" class="btn-line" id="collapseAll">Close all</button>
      </div>
      <nav class="toc" aria-label="Contents">{{TOC}}</nav>
    </div>
  </aside>
  <main id="main" tabindex="-1">
    <section class="hero" id="top">
      <h1>Before Three</h1>
      <p class="lede">A field guide for first-time parents, from planning a pregnancy to your child's third birthday. What to buy and skip, what to eat and how to move, how to get through birth and the first months, and how to raise a secure, curious child. Plain language, real evidence, and what works in many countries, not just one.</p>
      <div class="hero-ruler">
        <p class="hero-ruler-label" id="heroRulerLabel">Jump to a stage</p>
        <ul aria-labelledby="heroRulerLabel">{{HERO_STAGES}}</ul>
      </div>
    </section>
    <section class="intro" id="start">{{INTRO}}</section>
    <div id="filterbar" class="filterbar" hidden>
      <p id="filterText"></p>
      <button type="button" class="btn-plain" id="showAll">Show everything</button>
    </div>
    <div id="empty" class="empty" hidden>
      <p>No topics match that search and stage.</p>
      <button type="button" class="btn-line" id="clearFilters">Clear search and filters</button>
    </div>
    {{SECTIONS}}
    <section class="books" id="books" aria-labelledby="books-h">{{BOOKS}}</section>
    <section class="glossary" id="glossary" aria-labelledby="glossary-h">
      <h2 id="glossary-h">Glossary</h2>
      <p class="glossary-intro">Every medical and technical term used in this guide, in plain words.</p>
      {{GLOSSARY}}
    </section>
    <section class="about" id="about">{{ABOUT}}</section>
    <footer class="foot">
      <p>Before Three. Education, not medical advice. Last reviewed October 2026.</p>
      <p><a href="#top">Back to top</a></p>
    </footer>
  </main>
</div>
<script>{{JS}}</script>
</body>
</html>
"""

CSS = r"""
:root{
  --paper:#F6F8F7; --surface:#FFFFFF; --ink:#1C2632; --muted:#55606C; --line:#D5DCDF; --line-soft:#E5EAEC;
  --gear:#3B6788; --nutrition:#4F6E2F; --care:#8A4A6B; --parenting:#8E5A14;
  --gear-tint:#E6EEF4; --nutrition-tint:#EAF0E2; --care-tint:#F4E8EE; --parenting-tint:#F5ECDF;
  --helps:#2E6B40; --backfires:#A2382C; --mixed:#7A5B12; --borrow:#3B6788; --on-verdict:#FFFFFF;
  --focus:#1F5FD1;
  --sans:"Schibsted Grotesk","Helvetica Neue",Arial,system-ui,sans-serif;
  --serif:"Literata",Georgia,"Times New Roman",serif;
  --head-h:64px;
  color-scheme:light;
  box-sizing:border-box;
  padding-top:env(safe-area-inset-top,0px);
  padding-bottom:env(safe-area-inset-bottom,0px);
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --paper:#11181F; --surface:#17212A; --ink:#E3E9ED; --muted:#A3AEB8; --line:#2E3A45; --line-soft:#232E38;
    --gear:#8EB6D6; --nutrition:#A6C77C; --care:#D99CBA; --parenting:#E2B466;
    --gear-tint:#1A2733; --nutrition-tint:#1C2618; --care-tint:#2A1C24; --parenting-tint:#2B2216;
    --helps:#86CC97; --backfires:#F08C80; --mixed:#E2B466; --borrow:#8EB6D6; --on-verdict:#11181F;
    --focus:#8AB8FF;
    color-scheme:dark;
  }
}
:root[data-theme="dark"]{
  --paper:#11181F; --surface:#17212A; --ink:#E3E9ED; --muted:#A3AEB8; --line:#2E3A45; --line-soft:#232E38;
  --gear:#8EB6D6; --nutrition:#A6C77C; --care:#D99CBA; --parenting:#E2B466;
  --gear-tint:#1A2733; --nutrition-tint:#1C2618; --care-tint:#2A1C24; --parenting-tint:#2B2216;
  --helps:#86CC97; --backfires:#F08C80; --mixed:#E2B466; --borrow:#8EB6D6; --on-verdict:#11181F;
  --focus:#8AB8FF;
  color-scheme:dark;
}
*,*::before,*::after{box-sizing:inherit}
[hidden]{display:none !important}
html{scroll-padding-top:calc(env(safe-area-inset-top,0px) + var(--head-h) + 16px);-webkit-text-size-adjust:100%}
@media (prefers-reduced-motion: no-preference){html{scroll-behavior:smooth}}
body{margin:0;background:var(--paper);color:var(--ink);font:400 18px/1.7 var(--serif);font-optical-sizing:auto}
body.no-scroll{overflow:hidden}
a{color:inherit;text-decoration-thickness:1px;text-underline-offset:3px}
:focus-visible{outline:2px solid var(--focus);outline-offset:2px;border-radius:3px}
.skip{position:absolute;left:12px;top:-60px;background:var(--ink);color:var(--paper);padding:10px 14px;font:600 15px var(--sans);z-index:100;border-radius:4px}
.skip:focus{top:calc(env(safe-area-inset-top,0px) + 8px)}

.s-gear{--c:var(--gear);--t:var(--gear-tint)}
.s-nutrition{--c:var(--nutrition);--t:var(--nutrition-tint)}
.s-care{--c:var(--care);--t:var(--care-tint)}
.s-parenting{--c:var(--parenting);--t:var(--parenting-tint)}

/* header */
.site-head{position:sticky;top:env(safe-area-inset-top,0px);z-index:30;background:var(--paper);border-bottom:1px solid var(--line)}
@supports (backdrop-filter: blur(8px)){.site-head{background:color-mix(in srgb,var(--paper) 90%,transparent);backdrop-filter:blur(8px)}}
.head-inner{max-width:1280px;margin:0 auto;padding:0 28px;height:var(--head-h);display:flex;align-items:center;gap:28px}
.brand{font:800 22px/1 var(--sans);letter-spacing:-0.025em;text-decoration:none;white-space:nowrap}
.tabs{display:flex;gap:2px;flex:1;min-width:0}
.tab{font:600 15px/1 var(--sans);padding:22px 10px 19px;text-decoration:none;color:var(--muted);border-bottom:3px solid transparent;white-space:nowrap}
.tab:hover{color:var(--ink);border-bottom-color:var(--c,var(--line))}
.tab[aria-current="location"]{color:var(--ink);border-bottom-color:var(--c,var(--ink))}
.head-actions{display:flex;gap:8px;margin-left:auto}
.btn-plain{font:600 14px/1 var(--sans);background:none;border:1.5px solid var(--line);color:var(--ink);padding:9px 12px;border-radius:999px;cursor:pointer}
.btn-plain:hover{border-color:var(--ink)}
.btn-line{font:600 14px/1 var(--sans);background:none;border:none;color:var(--ink);padding:6px 0;cursor:pointer;text-decoration:underline;text-underline-offset:3px}
.menu-btn,.close-btn{display:none}

/* layout */
.layout{display:grid;grid-template-columns:260px minmax(0,1fr);gap:64px;max-width:1280px;margin:0 auto;padding:0 28px}
main{max-width:780px;min-width:0;padding-bottom:80px}
main:focus{outline:none}

/* rail */
.rail{position:sticky;top:calc(env(safe-area-inset-top,0px) + var(--head-h));align-self:start;max-height:calc(100vh - var(--head-h) - env(safe-area-inset-top,0px));overflow-y:auto;padding:32px 4px 40px 0;scrollbar-width:thin}
.rail-top{display:flex;justify-content:space-between;align-items:center}
.rail-label{display:block;font:700 14px/1.2 var(--sans);margin:0 0 8px;color:var(--ink)}
#q{width:100%;font:400 16px/1.3 var(--sans);padding:10px 12px;border:1.5px solid var(--line);border-radius:8px;background:var(--surface);color:var(--ink);margin-bottom:28px}
#q:focus{border-color:var(--ink);outline:none}
.ruler{list-style:none;margin:4px 0 12px;padding:0;position:relative}
.ruler::before{content:"";position:absolute;left:9px;top:4px;bottom:4px;width:2px;background:var(--line)}
.ruler::after{content:"";position:absolute;left:9px;top:4px;bottom:4px;width:7px;background:repeating-linear-gradient(to bottom,var(--line) 0 1px,transparent 1px 7px)}
.ruler li{margin:0}
.ruler button{all:unset;box-sizing:border-box;position:relative;z-index:1;display:flex;align-items:center;gap:10px;width:100%;padding:7px 0;cursor:pointer;font:500 15px/1.3 var(--sans);color:var(--muted)}
.ruler button::before{content:"";flex:none;width:16px;height:2px;margin-left:9px;background:var(--muted);transition:width .2s ease}
.ruler button:hover{color:var(--ink)}
.ruler button[aria-pressed="true"]{color:var(--ink);font-weight:700}
.ruler button[aria-pressed="true"]::before{width:30px;height:4px;background:var(--ink);border-radius:2px}
.ruler button:focus-visible{outline:2px solid var(--focus);outline-offset:2px;border-radius:3px}
.count{font:500 14px/1.4 var(--sans);color:var(--muted);margin:0 0 6px}
.rail-tools{display:flex;gap:16px;margin-bottom:24px}
.toc{border-top:1px solid var(--line);padding-top:18px}
.toc ul{list-style:none;margin:0;padding:0}
.toc-list>li{margin:0 0 12px}
.toc-list>li>a{font:700 15px/1.3 var(--sans);text-decoration:none}
.toc-sec>a{color:var(--c)}
.toc-sec ul{margin:6px 0 0 0;padding-left:12px;border-left:2px solid var(--c)}
.toc-sec ul a{display:block;font:400 14px/1.35 var(--sans);color:var(--muted);text-decoration:none;padding:3px 0}
.toc a:hover{color:var(--ink);text-decoration:underline}

/* hero */
.hero{padding:64px 0 40px}
.hero h1{font:800 clamp(60px,11vw,124px)/0.9 var(--sans);letter-spacing:-0.045em;margin:0 0 28px;max-width:10ch}
.lede{font:400 21px/1.6 var(--serif);margin:0 0 40px;max-width:36em}
.hero-ruler-label{font:700 14px/1.2 var(--sans);margin:0 0 10px}
.hero-ruler ul{list-style:none;margin:0;padding:22px 0 0;display:grid;grid-template-columns:repeat(6,1fr);position:relative;border-top:3px solid var(--ink)}
.hero-ruler ul::before{content:"";position:absolute;left:0;right:0;top:0;height:12px;background:repeating-linear-gradient(to right,var(--ink) 0 1px,transparent 1px 12px)}
.hero-ruler li{position:relative}
.hero-ruler li::before{content:"";position:absolute;left:0;top:-22px;width:3px;height:22px;background:var(--ink)}
.hero-ruler button{all:unset;box-sizing:border-box;cursor:pointer;display:block;padding:2px 8px 2px 8px;font:600 15px/1.25 var(--sans);color:var(--ink)}
.hero-ruler button:hover{text-decoration:underline;text-underline-offset:3px}
.hero-ruler button:focus-visible{outline:2px solid var(--focus);outline-offset:2px;border-radius:3px}
.hero-ruler button[aria-pressed="true"]{text-decoration:underline;text-decoration-thickness:3px;text-underline-offset:5px}
@media (prefers-reduced-motion: no-preference){
  .hero-ruler ul{animation:measure .9s cubic-bezier(.2,.7,.2,1) both}
  @keyframes measure{from{clip-path:inset(0 100% 0 0)}to{clip-path:inset(0 0 0 0)}}
}

/* intro */
.intro{border-top:1px solid var(--line);padding-top:40px}
.intro h2,.about h2,.glossary h2{font:800 40px/1.05 var(--sans);letter-spacing:-0.025em;margin:0 0 16px}
.intro h3,.about h3{font:700 23px/1.25 var(--sans);letter-spacing:-0.01em;margin:40px 0 12px}
.intro p,.intro li,.about p,.about li{max-width:68ch}
.intro ul,.about ul{padding-left:1.2em}
.intro li,.about li{margin-bottom:8px}
.intro li a{font:600 15px var(--sans);white-space:nowrap}
.checklist{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:8px 36px;margin-top:20px;padding:24px;background:var(--surface);border:1px solid var(--line);border-radius:10px}
.cl-group h4{font:700 16px/1.3 var(--sans);margin:8px 0 8px}
.cl-group ul{list-style:none;padding:0;margin:0 0 12px}
.cl-group li{margin:0 0 6px;max-width:none}
.cl-group label{display:flex;gap:10px;align-items:flex-start;font:400 16px/1.45 var(--sans);cursor:pointer}
.cl-group input{width:18px;height:18px;margin:2px 0 0;flex:none;accent-color:var(--ink)}
.cl-group input:checked+span{color:var(--muted);text-decoration:line-through}

/* sections */
.sec{margin-top:88px}
.sec-head{border-top:8px solid var(--c);padding-top:22px;margin-bottom:12px}
.sec-head h2{font:800 clamp(44px,6vw,64px)/1 var(--sans);letter-spacing:-0.035em;color:var(--c);margin:0 0 18px}
.sec-sum p,.sec-sum li{max-width:68ch}
.sec-sum ul{padding-left:1.2em}
.sec-sum li{margin-bottom:8px}
.cat{margin-top:56px}
.cat-head h3{font:700 27px/1.2 var(--sans);letter-spacing:-0.015em;margin:0 0 6px}
.cat-sum{color:var(--muted)}
.cat-sum p{margin:0 0 18px;max-width:68ch}

/* topics */
.topics{border-bottom:1px solid var(--line)}
.topic{border-top:1px solid var(--line)}
.topic>summary{list-style:none;cursor:pointer;display:flex;gap:18px;align-items:flex-start;padding:20px 8px 20px 20px;position:relative}
.topic>summary::-webkit-details-marker{display:none}
.topic>summary::before{content:"";position:absolute;left:0;top:22px;bottom:22px;width:4px;border-radius:2px;background:var(--c);opacity:.3}
.topic[open]>summary::before{opacity:1}
.topic>summary:hover{background:var(--t)}
.t-main{flex:1;min-width:0;display:block}
.t-title{font:700 21px/1.25 var(--sans);letter-spacing:-0.01em;margin:0 0 4px}
.t-teaser{display:block;font:400 16.5px/1.5 var(--serif);color:var(--muted)}
.t-badges{display:flex;flex-wrap:wrap;gap:6px;margin-top:10px}
.badge{font:600 12.5px/1 var(--sans);padding:5px 8px;border-radius:4px;border:1px solid var(--line);color:var(--muted);background:var(--surface)}
.badge.ev-strong{color:var(--ink);border-color:var(--ink)}
.badge.ev-debated{color:var(--mixed);border-color:var(--mixed)}
.badge.safety{color:var(--backfires);border-color:var(--backfires)}
.t-toggle{flex:none;width:30px;height:30px;margin-top:2px;border:1.5px solid var(--line);border-radius:50%;position:relative}
.t-toggle::before,.t-toggle::after{content:"";position:absolute;left:50%;top:50%;width:12px;height:2px;background:var(--ink);transform:translate(-50%,-50%)}
.t-toggle::after{transform:translate(-50%,-50%) rotate(90deg);transition:transform .2s ease}
.topic[open] .t-toggle::after{transform:translate(-50%,-50%) rotate(0deg)}
.topic>summary:hover .t-toggle{border-color:var(--ink)}
.t-body{padding:0 8px 32px 20px}
.t-stages{font:500 14px/1.4 var(--sans);color:var(--muted);margin:0}
.t-stages span{font-weight:700;color:var(--ink)}
.part{margin-top:26px}
.part h5{font:700 16px/1.2 var(--sans);color:var(--c);margin:0 0 8px}
.part h5 small{font-weight:500;font-size:13.5px;color:var(--muted);margin-left:6px}
.t-body p,.t-body li{max-width:68ch}
.t-body p{margin:0 0 12px}
.t-body ul,.t-body ol{padding-left:1.15em;margin:0 0 12px}
.t-body li{margin-bottom:6px}
.t-body li ul{margin-top:6px}
.t-body a{color:var(--c)}

/* why: ripples */
.why>ul{list-style:none;padding:0}
.why>ul>li{position:relative;padding-left:36px;margin-bottom:14px}
.why>ul>li::before{content:"";position:absolute;left:9px;top:.55em;width:8px;height:8px;border-radius:50%;background:var(--c)}
.why>ul>li:nth-child(2)::before{box-shadow:0 0 0 3px var(--paper),0 0 0 4.5px var(--c)}
.why>ul>li:nth-child(3)::before{box-shadow:0 0 0 3px var(--paper),0 0 0 4.5px var(--c),0 0 0 7.5px var(--paper),0 0 0 9px var(--c)}
.why>ul>li:nth-child(n+4)::before{background:none;border:1.5px solid var(--muted)}
.why>ul>li>strong:first-child{display:block;font:700 15px/1.3 var(--sans);margin-bottom:2px}

/* around the world: verdicts */
.culture>ul{list-style:none;padding:0}
.culture>ul>li{border-left:3px solid var(--line);padding:2px 0 2px 16px;margin-bottom:16px}
.culture>ul>li:has(.v-helps){border-left-color:var(--helps)}
.culture>ul>li:has(.v-backfires){border-left-color:var(--backfires)}
.culture>ul>li:has(.v-mixed){border-left-color:var(--mixed)}
.culture>ul>li:has(.v-borrow){border-left-color:var(--borrow)}
.verdict{display:inline-block;font:700 12.5px/1 var(--sans);padding:4px 7px;border-radius:4px;margin-right:6px;vertical-align:2px;color:var(--on-verdict)}
.v-helps{background:var(--helps)}
.v-backfires{background:var(--backfires)}
.v-mixed{background:var(--mixed)}
.v-borrow{background:var(--borrow)}

/* related and sources */
.related{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-top:26px}
.rel-label{font:700 14px/1 var(--sans);margin-right:4px}
.chip{display:inline-block;text-decoration:none;color:var(--c) !important;border:1.5px solid var(--c);border-radius:999px;padding:7px 12px;font:600 14px/1.2 var(--sans);background:var(--surface)}
.chip:hover{background:var(--t)}
.chip-sec{font-weight:500;color:var(--muted)}
.sources{margin-top:18px}
.sources summary{cursor:pointer;font:600 14px/1.4 var(--sans);color:var(--muted)}
.sources ul{font:400 15px/1.5 var(--sans);margin-top:8px}
.sources a{color:var(--ink) !important}

/* tables */
.table-wrap{overflow-x:auto;margin:12px 0 18px;-webkit-overflow-scrolling:touch}
table{border-collapse:collapse;width:100%;font:400 15.5px/1.45 var(--serif)}
th{font:700 14px/1.3 var(--sans);text-align:left;border-bottom:2px solid var(--ink);padding:8px 14px 8px 0;vertical-align:bottom}
td{border-bottom:1px solid var(--line);padding:10px 14px 10px 0;vertical-align:top}
td:first-child{font-weight:600}
.cat-skip .table-wrap{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:4px 18px}
.cat-skip td:nth-child(2){font:600 14px/1.45 var(--sans)}

/* book citations inside topics */
.cite-src{font:500 13px/1.3 var(--sans);color:var(--muted);margin-left:4px}
.t-body .cite-src a{color:var(--muted);text-decoration-color:var(--line)}
.t-body .cite-src a:hover{color:var(--ink)}
.cite-ev{display:inline-block;font:600 12px/1 var(--sans);padding:3px 6px;border-radius:4px;border:1px solid currentColor;margin-left:4px;vertical-align:1px;white-space:nowrap}
.ev-fits{color:var(--helps)}
.ev-partly{color:var(--mixed)}
.ev-conflicts{color:var(--backfires)}
.src-book{font:700 11.5px/1 var(--sans);padding:3px 6px;border-radius:4px;border:1px solid var(--line);color:var(--muted);margin-right:4px;vertical-align:1px}

/* bookshelf */
.books{margin-top:96px;border-top:8px solid var(--ink);padding-top:22px}
.books h2{font:800 40px/1.05 var(--sans);letter-spacing:-0.025em;margin:0 0 16px}
.books>p,.books>ul li{max-width:68ch}
.books>ul{padding-left:1.2em}
.books>ul li{margin-bottom:6px}
.book{position:relative;border-top:1px solid var(--line);padding:24px 0 24px 22px}
.book::before{content:"";position:absolute;left:0;top:28px;bottom:28px;width:4px;border-radius:2px;background:var(--w,var(--line))}
.book.w-core{--w:var(--ink)}
.book.w-background{--w:var(--line)}
.book.w-caution{--w:var(--mixed)}
.book-head{display:flex;align-items:baseline;flex-wrap:wrap;gap:6px 12px}
.book h3{font:700 23px/1.25 var(--sans);letter-spacing:-0.01em;margin:0}
.badge.w-core{color:var(--ink);border-color:var(--ink)}
.badge.w-caution{color:var(--mixed);border-color:var(--mixed)}
.book-meta{font:500 15px/1.4 var(--sans);color:var(--muted);margin:4px 0 12px}
.book-body p{max-width:68ch;margin:0 0 10px}
.book-link{margin:4px 0 0;font:600 14px/1.4 var(--sans)}
.book-used{margin-top:14px}
.book-conflicts{border-top:1px solid var(--line);padding-top:8px}
.book-conflicts h3{font:700 23px/1.25 var(--sans);letter-spacing:-0.01em;margin:32px 0 8px}

/* glossary, about, footer */
.glossary,.about{margin-top:96px;border-top:8px solid var(--ink);padding-top:22px}
.glossary-intro{color:var(--muted);margin:0 0 24px}
.glossary-list{margin:0;display:grid;grid-template-columns:1fr;gap:0}
.g-item{display:grid;grid-template-columns:minmax(150px,220px) 1fr;gap:4px 24px;padding:12px 0;border-top:1px solid var(--line)}
.g-item dt{font:700 16px/1.4 var(--sans)}
.g-item dd{margin:0;font-size:16.5px;line-height:1.55}
.foot{margin-top:72px;border-top:1px solid var(--line);padding-top:20px;font:400 14px/1.5 var(--sans);color:var(--muted);display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap}
.empty{margin:48px 0;padding:24px;border:1.5px dashed var(--line);border-radius:10px;font-family:var(--sans)}
.empty p{margin:0 0 8px}
.scrim{position:fixed;inset:0;background:rgba(10,16,22,.45);z-index:35}
.filterbar{display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap;margin:48px 0 0;padding:16px 20px;background:var(--surface);border:1.5px solid var(--ink);border-radius:10px;font:500 16px/1.4 var(--sans)}
.filterbar p{margin:0}
.filtering .sec-sum{display:none}
.filtering .sec{margin-top:56px}
.cat-sum .table-wrap{color:var(--ink)}
.cat-skip td.v-danger{color:var(--backfires)}
.cat-skip td.v-warn{color:var(--mixed)}
.cat-skip td.v-meh{color:var(--muted)}

/* mid widths */
@media (max-width:1180px){
  .tab{padding-left:8px;padding-right:8px;font-size:14px}
}
/* small screens: rail becomes a drawer */
@media (max-width:959px){
  .layout{display:block;padding:0 20px}
  .tabs{display:none}
  .menu-btn,.close-btn{display:inline-block}
  .head-inner{padding:0 20px;gap:12px}
  .rail{position:fixed;top:0;left:0;bottom:0;width:min(88vw,360px);max-height:none;height:100%;z-index:40;background:var(--surface);padding:calc(env(safe-area-inset-top,0px) + 20px) 22px calc(env(safe-area-inset-bottom,0px) + 28px);transform:translateX(-105%);visibility:hidden;transition:transform .25s ease,visibility 0s linear .25s;box-shadow:0 0 40px rgba(0,0,0,.25)}
  .rail.open{transform:none;visibility:visible;transition:transform .25s ease}
  .hero{padding-top:40px}
  .g-item{grid-template-columns:1fr}
}
@media (max-width:640px){
  body{font-size:17px}
  .lede{font-size:19px}
  .hero-ruler ul{grid-template-columns:repeat(3,1fr);row-gap:14px;border-top:none;padding-top:0}
  .hero-ruler ul::before{display:none}
  .hero-ruler li{border-top:3px solid var(--ink);padding-top:10px}
  .hero-ruler li::before{display:none}
  .topic>summary{padding:18px 4px 18px 16px}
  .t-body{padding:0 4px 28px 16px}
  .why>ul>li{padding-left:30px}
  .why>ul>li::before{left:6px}
  .head-actions .btn-plain{padding:8px 10px}
  .brand{font-size:20px}
}
@media (prefers-reduced-motion: reduce){
  *,*::before,*::after{transition:none !important;animation:none !important}
}
@media print{
  .site-head,.rail,.scrim,.hero-ruler,.t-toggle,.empty,.skip,.rail-tools{display:none !important}
  .layout{display:block;padding:0}
  main{max-width:none}
  body{background:#fff;color:#000;font-size:11pt}
  .topic>summary::before{opacity:1}
  .sec{break-before:page}
  a{color:inherit !important}
}
"""

JS = r"""
(function(){
  var root=document.documentElement;
  var reduceMotion=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* theme */
  var themeBtn=document.getElementById('themeBtn');
  function stored(k){try{return localStorage.getItem(k)}catch(e){return null}}
  function store(k,v){try{localStorage.setItem(k,v)}catch(e){}}
  function systemDark(){return !!(window.matchMedia&&window.matchMedia('(prefers-color-scheme: dark)').matches)}
  function currentTheme(){return root.getAttribute('data-theme')||(systemDark()?'dark':'light')}
  function updateThemeBtn(){
    var dark=currentTheme()==='dark';
    themeBtn.textContent=dark?'Light mode':'Dark mode';
    themeBtn.setAttribute('aria-label',dark?'Switch to light theme':'Switch to dark theme');
  }
  var savedTheme=stored('b3-theme');
  if(savedTheme==='dark'||savedTheme==='light'){root.setAttribute('data-theme',savedTheme)}
  updateThemeBtn();
  if(window.matchMedia){
    var mq=window.matchMedia('(prefers-color-scheme: dark)');
    if(mq.addEventListener)mq.addEventListener('change',updateThemeBtn);
  }
  themeBtn.addEventListener('click',function(){
    var next=currentTheme()==='dark'?'light':'dark';
    root.setAttribute('data-theme',next);store('b3-theme',next);updateThemeBtn();
  });

  /* filtering */
  var topics=[].slice.call(document.querySelectorAll('details.topic'));
  var cats=[].slice.call(document.querySelectorAll('.cat'));
  var secs=[].slice.call(document.querySelectorAll('section.sec'));
  var stageBtns=[].slice.call(document.querySelectorAll('[data-stage]'));
  var q=document.getElementById('q');
  var count=document.getElementById('count');
  var empty=document.getElementById('empty');
  var state={stage:'all',q:''};
  var filterbar=document.getElementById('filterbar');
  var filterText=document.getElementById('filterText');
  function stageName(k){
    var b=document.querySelector('.ruler [data-stage="'+k+'"]');
    return b?b.textContent:k;
  }
  var suppressHash=false;
  topics.forEach(function(t){t._text=t.textContent.toLowerCase()});
  cats.forEach(function(c){c._text=c.textContent.toLowerCase()});

  function apply(){
    var terms=state.q.trim().toLowerCase().split(/\s+/).filter(Boolean);
    var filtering=state.stage!=='all'||terms.length>0;
    var shown=0;
    topics.forEach(function(t){
      var okStage=state.stage==='all'||(' '+t.getAttribute('data-stages')+' ').indexOf(' '+state.stage+' ')>-1;
      var okText=terms.every(function(w){return t._text.indexOf(w)>-1});
      t.hidden=!(okStage&&okText);
      if(!t.hidden)shown++;
    });
    var staticShown=0;
    cats.forEach(function(c){
      var ts=c.querySelectorAll('details.topic');
      if(ts.length){
        c.hidden=![].some.call(ts,function(t){return !t.hidden});
      }else{
        var okText=terms.every(function(w){return c._text.indexOf(w)>-1});
        c.hidden=state.stage!=='all'||!okText;
        if(!c.hidden&&filtering)staticShown++;
      }
    });
    secs.forEach(function(s){
      s.hidden=![].some.call(s.querySelectorAll('.cat'),function(c){return !c.hidden});
    });
    [].forEach.call(document.querySelectorAll('.toc [data-for]'),function(li){
      var target=document.getElementById(li.getAttribute('data-for'));
      li.hidden=!!(target&&target.hidden);
    });
    stageBtns.forEach(function(b){b.setAttribute('aria-pressed',String(b.getAttribute('data-stage')===state.stage))});
    count.textContent=filtering?(shown+' of '+topics.length+' topics match'):(topics.length+' topics');
    document.body.classList.toggle('filtering',filtering);
    filterbar.hidden=!filtering;
    if(filtering){
      var bits=[];
      if(state.stage!=='all'){bits.push('stage: '+stageName(state.stage))}
      if(terms.length){bits.push('search: "'+state.q.trim()+'"')}
      filterText.textContent='Showing '+shown+' of '+topics.length+' topics ('+bits.join(', ')+').';
    }
    empty.hidden=!(filtering&&shown===0&&staticShown===0);
  }

  function firstVisibleSection(){
    if(!filterbar.hidden)return filterbar;
    for(var i=0;i<secs.length;i++){if(!secs[i].hidden)return secs[i]}
    return empty.hidden?null:empty;
  }

  stageBtns.forEach(function(b){
    b.addEventListener('click',function(){
      state.stage=b.getAttribute('data-stage');
      apply();
      if(isDrawer())setMenu(false,true);
      var target=firstVisibleSection();
      if(target)target.scrollIntoView({behavior:reduceMotion?'auto':'smooth',block:'start'});
    });
  });

  var qTimer=null;
  q.addEventListener('input',function(){
    clearTimeout(qTimer);
    qTimer=setTimeout(function(){state.q=q.value;apply()},120);
  });
  q.addEventListener('keydown',function(e){
    if(e.key==='Enter'){
      e.preventDefault();
      if(isDrawer())setMenu(false,true);
      var target=firstVisibleSection();
      if(target)target.scrollIntoView({behavior:reduceMotion?'auto':'smooth',block:'start'});
    }
  });

  function clearAll(){state.stage='all';state.q='';q.value='';apply()}
  document.getElementById('clearFilters').addEventListener('click',clearAll);
  document.getElementById('showAll').addEventListener('click',clearAll);
  document.getElementById('expandAll').addEventListener('click',function(){
    suppressHash=true;topics.forEach(function(t){if(!t.hidden)t.open=true});
    setTimeout(function(){suppressHash=false},0);
  });
  document.getElementById('collapseAll').addEventListener('click',function(){
    suppressHash=true;topics.forEach(function(t){t.open=false});
    setTimeout(function(){suppressHash=false},0);
  });

  /* deep links: open the topic that contains the target */
  function openTarget(id,smooth){
    if(!id)return;
    var el=document.getElementById(id);
    if(!el)return;
    if(el.closest('[hidden]')){state.stage='all';state.q='';q.value='';apply()}
    var topic=el.matches('details.topic')?el:el.closest('details.topic');
    if(topic&&!topic.open){suppressHash=true;topic.open=true;setTimeout(function(){suppressHash=false},0)}
    requestAnimationFrame(function(){
      el.scrollIntoView({block:'start',behavior:(smooth&&!reduceMotion)?'smooth':'auto'});
      if(topic&&smooth){var s=topic.querySelector('summary');if(s)s.focus({preventScroll:true})}
    });
  }
  window.addEventListener('hashchange',function(){openTarget(decodeURIComponent(location.hash.slice(1)),true)});
  document.addEventListener('click',function(e){
    var a=e.target.closest&&e.target.closest('a[href^="#"]');
    if(!a)return;
    if(isDrawer()&&a.closest('#rail'))setMenu(false,true);
    var id=decodeURIComponent(a.getAttribute('href').slice(1));
    if(('#'+id)===location.hash){e.preventDefault();openTarget(id,true)}
  });
  topics.forEach(function(t){
    t.addEventListener('toggle',function(){
      if(t.open&&!suppressHash&&history.replaceState){history.replaceState(null,'','#'+t.id)}
    });
  });

  /* drawer on small screens */
  var rail=document.getElementById('rail');
  var menuBtn=document.getElementById('menuBtn');
  var scrim=document.getElementById('scrim');
  function isDrawer(){return window.matchMedia('(max-width: 959px)').matches}
  function setMenu(open,quiet){
    rail.classList.toggle('open',open);
    scrim.hidden=!open;
    menuBtn.setAttribute('aria-expanded',String(open));
    document.body.classList.toggle('no-scroll',open);
    if(open){setTimeout(function(){q.focus()},50)}else if(!quiet){menuBtn.focus()}
  }
  menuBtn.addEventListener('click',function(){setMenu(!rail.classList.contains('open'))});
  document.getElementById('closeBtn').addEventListener('click',function(){setMenu(false)});
  scrim.addEventListener('click',function(){setMenu(false)});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&rail.classList.contains('open'))setMenu(false)});
  window.addEventListener('resize',function(){if(!isDrawer()&&rail.classList.contains('open'))setMenu(false,true)});

  /* current section in the header */
  if('IntersectionObserver' in window){
    var tabs=[].slice.call(document.querySelectorAll('.tab[data-sec]'));
    var io=new IntersectionObserver(function(entries){
      entries.forEach(function(en){
        if(!en.isIntersecting)return;
        tabs.forEach(function(tab){
          if(tab.getAttribute('data-sec')===en.target.id)tab.setAttribute('aria-current','location');
          else tab.removeAttribute('aria-current');
        });
      });
    },{rootMargin:'-35% 0px -60% 0px'});
    secs.forEach(function(s){io.observe(s)});
    ['books','glossary'].forEach(function(id){var el=document.getElementById(id);if(el)io.observe(el)});
  }

  /* checklist ticks persist in this browser */
  var KEY='b3-checklist';var saved={};
  try{saved=JSON.parse(localStorage.getItem(KEY)||'{}')||{}}catch(e){saved={}}
  [].forEach.call(document.querySelectorAll('.checklist input[type=checkbox]'),function(cb){
    cb.checked=!!saved[cb.getAttribute('data-key')];
    cb.addEventListener('change',function(){
      saved[cb.getAttribute('data-key')]=cb.checked;
      try{localStorage.setItem(KEY,JSON.stringify(saved))}catch(e){}
    });
  });

  /* print everything open */
  var printOpened=[];
  window.addEventListener('beforeprint',function(){
    suppressHash=true;
    [].forEach.call(document.querySelectorAll('details'),function(d){if(!d.open){d.open=true;printOpened.push(d)}});
  });
  window.addEventListener('afterprint',function(){
    printOpened.forEach(function(d){d.open=false});printOpened=[];
    setTimeout(function(){suppressHash=false},0);
  });

  apply();
  if(location.hash)openTarget(decodeURIComponent(location.hash.slice(1)),false);
})();
"""
