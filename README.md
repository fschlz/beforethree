# Before Three

A field guide for first-time parents, from planning a pregnancy to age 3.
Static site: one `index.html`, no framework, no build step on Vercel.

## Folder layout

- `index.html` - the built site (this is what Vercel serves)
- `vercel.json` - security headers and clean URLs
- `robots.txt` - allows search engines
- `.vercelignore` - keeps `source/` and this README out of the deployment
- `source/` - the editable content and the build script
  - `content/*.md` - all text: gear, nutrition, care, parenting, books, glossary, intro, about
  - `build.py` - turns the content files into `index.html` and checks every link
  - `template.py` - page layout, styles and scripts

## First deploy (Vercel CLI)

The Vercel project `beforethree` already exists in your account.

```
cd beforethree
npx vercel link --project beforethree --yes
npx vercel deploy --prod
```

## Updating content

1. Edit a file in `source/content/`.
2. Rebuild:
   ```
   pip install markdown
   cd source
   SITE_URL=https://YOUR-DOMAIN python3 build.py
   ```
   The build stops with an error if a link is broken, a book name is misspelled,
   or a character outside the standard keyboard set slips in.
3. Deploy again with `npx vercel deploy --prod`, or push to GitHub if the
   project is connected to a repository (Vercel then deploys automatically).

## Custom domain

Add the domain in Vercel (Project > Settings > Domains), then at your registrar:

- `A` record for `@` pointing to `76.76.21.21`
- `CNAME` record for `www` pointing to `cname.vercel-dns.com`

Vercel shows the exact values for your domain on the Domains page; use those if they differ.
