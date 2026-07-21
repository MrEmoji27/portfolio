# zemo — portfolio

Brutalist single-page portfolio. One hand-written HTML file, no framework, no build step.

## Files

| File | What it is |
|---|---|
| `index.html` | The entire site — markup, styles, and scripts in one file |
| `404.html` | Not-found page (Netlify picks it up automatically) |
| `zemo.txt` | ASCII portfolio for terminal users (`curl` the root URL after deploy) |
| `zemo-resume.pdf` | One-page resume, same visual language |
| `humans.txt` / `pgp.txt` / `.well-known/security.txt` | Niche credibility files |
| `site.webmanifest` + `img/icon-*.png` | Installable-site manifest and icons |
| `img/` | Screenshots (optimized JPEGs), OG share card, 88×31 badge |
| `fonts/` | Self-hosted Archivo Black + Space Mono (woff2) |
| `functions/_middleware.js` | Cloudflare Pages Function — serves `zemo.txt` to curl/wget at the root URL |
| `_headers` | Cache and security headers for Cloudflare Pages |

Design history (`index-suprematist.html`, `index-brutal-v1.html`) lives outside this folder in `Desktop\portfolio-archive\`.

## Editing works

Each project is an `<li data-w="...">` inside `#works`. To add one:

1. Copy an existing `<li>` block, change the name, tag, tease, description, features, links.
2. Add a matching shape in the `#art` SVG with the same `data-w` value.
3. Add the key to `scrollFactors` in the script.
4. Update the works count in the red marquee ("ten works").
5. Mirror the entry in `zemo.txt` and (if it matters) the resume.

## Keep in sync — the three-copies rule

Content lives in three places. When you change one, check the others:

- **Site** (`index.html`)
- **ASCII version** (`zemo.txt`)
- **Resume** (`zemo-resume.pdf` — regenerated from a script, ask your agent or rebuild by hand)

## Configuration

- **Tester form**: submits to Formspree — the endpoint is `data-endpoint` on `#tm-form`.
- **GitHub pulse**: fetches `api.github.com/users/MrEmoji27/events/public` — change the username there if it ever changes.
- **PGP**: live — key in `pgp.txt`, fingerprint `9DB9 4C2F 801B F217 AA15 6643 4120 E017 924C 16F1`, expires 2028-07-18 (renew before then). At domain time, update the `Encryption:` line in `.well-known/security.txt`.

## Deploy — Cloudflare Workers (static assets)

Live at `portfolio.mremoji47.workers.dev`, git-connected to `MrEmoji27/portfolio`.

Layout:

- `public/` — everything served to visitors (the site itself)
- `src/index.js` — the Worker: serves assets, and returns `zemo.txt` to curl/wget/httpie at `/`
- `wrangler.jsonc` — config (assets directory, 404 handling)

Updating: `git add . && git commit -m "..." && git push` — Cloudflare rebuilds automatically.
Note: site files live in `public/`, so paths inside `index.html` stay relative and unchanged.

Gotcha worth remembering: Cloudflare serves static assets *before* the Worker runs, so the
Worker never sees `/`. `run_worker_first: ["/", "/index.html"]` in `wrangler.jsonc` is what
makes the curl handler fire. Everything else still bypasses the Worker for full asset speed.

## TODO at deploy / when domain exists

- [ ] Physically move the `#materials` section above `#works` in the markup and delete the
      `main{display:flex}` order rules (marked with a TODO comment in the CSS).
- [ ] Set absolute URLs for `og:image` / `twitter:image` (comment marks the spot in `<head>`).
- [ ] Add `<link rel="canonical">`, `sitemap.xml`, `robots.txt`.
- [ ] Update JSON-LD `url` to the domain.
- [ ] Update `Encryption:` in security.txt once the PGP key + domain exist.
- [ ] Submit the tester form once to confirm the Formspree destination email.
