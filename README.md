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

## Deploy — Cloudflare Pages

Host: Cloudflare Pages. Deploy the whole folder (git-connected).

- Build command: *(none)*
- Build output directory: `/`
- Functions are picked up automatically from `functions/`

Updating: `git add . && git commit -m "..." && git push` — Pages rebuilds automatically.

## TODO at deploy / when domain exists

- [ ] Physically move the `#materials` section above `#works` in the markup and delete the
      `main{display:flex}` order rules (marked with a TODO comment in the CSS).
- [ ] Set absolute URLs for `og:image` / `twitter:image` (comment marks the spot in `<head>`).
- [ ] Add `<link rel="canonical">`, `sitemap.xml`, `robots.txt`.
- [ ] Update JSON-LD `url` to the domain.
- [ ] Update `Encryption:` in security.txt once the PGP key + domain exist.
- [ ] Submit the tester form once to confirm the Formspree destination email.
