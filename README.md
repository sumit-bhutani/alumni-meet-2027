# Jashn-e-Yaarana: DCE · DIT · DTU · NSIT · NSUT World Alumni Meet 2027

**Atlanta, Georgia, USA · April 16–18, 2027**

Website, flyer and sponsorship pamphlet for the 2027 world alumni reunion of Delhi College of Engineering (DCE), Delhi Institute of Technology (DIT), Delhi Technological University (DTU), Netaji Subhas Institute of Technology (NSIT) and Netaji Subhas University of Technology (NSUT).

| | |
|---|---|
| Live website | https://jashn-e-yaarana-2027.netlify.app |
| This repo | https://github.com/sumit-bhutani/alumni-meet-2027 (public) |
| Previous event | DC26, Washington, D.C., May 1–3, 2026 (`dc26.dcedit.org`, repo `dce-dit-conclave-2026`) |

---

## 1. Final event facts

These are confirmed. Keep every page, flyer and message consistent with them.

| | |
|---|---|
| **Name** | Delhi Polytechnic · DCE · DIT · DTU · NSIT · NSUT **World** Alumni Meet 2027 |
| **Theme** | Jashn-e-Yaarana (jashn = celebration, yaarana = friendship) |
| **Tagline** | The years change. But the friendship stays forever. |
| **Dates** | April 16–18, 2027 (Friday to Sunday) |
| **Location** | Atlanta, Georgia, USA |
| **Venue** | Maison 6405, 6405 Sugarloaf Parkway, Duluth, GA 30097 (greater Atlanta) |

### Program

| Day | Time | Event | Description |
|---|---|---|---|
| Fri Apr 16 | Evening | **Dhamaal** | Welcome night: networking, dinner, music and chai |
| Sat Apr 17 | Daytime | **Ek Saath** | Leadership Conclave: an alumni conference for batchmates, families and the next generation (business casual) |
| Sat Apr 17 | Evening | **Jalwa** | Gala and awards |
| Sun Apr 18 | Morning | **Chai Pila De** | Chai and breakfast, then checkout and departure. No firm end time published until the plan is final |

Timings, the Saturday session schedule and speakers are not yet decided. Do not publish a firm Sunday end time until the plan is final. Open: how to show the Friday evening visually on the website and flyer.

### Wording rules
- Write **"World Alumni Meet"**, never "Annual".
- The Sunday event is **"Chai Pila De"**. Never "Chai to Pilade".
- Ek Saath is described as the **"Leadership Conclave"**, not "the family day".
- **No Hindi script (Devanagari) anywhere.** Names are written in Latin letters only.
- **Flyer:** focus on Atlanta, Georgia, USA. Do not name Maison 6405 on the flyer (it is one event's venue). The website's Venue page does name it.
- Never use the early poster dates (April 30 – May 2). They are outdated.

---

## 2. Registration pricing

Prices are final and shown for information only. Registration and payment happen on a separate site (link not yet available). The website highlights the window that is open today (Eastern time) and its bottom bar changes with it.

| Ticket | Presale through Nov 15, 2026 | Early Bird Nov 16 – Dec 15, 2026 | Market Price from Dec 16, 2026 |
|---|---|---|---|
| Single | $199 | $250 | $325 |
| Couple (2 tickets) | $390 | $450 | $600 |
| NextGen | $100 | $140 | $160 |
| Parent | $179 | $229 | $250 |

Open question: the exact meaning and age range of the **NextGen** and **Parent** tickets.

---

## 3. Sponsorship packages

Full benefits are in `sponsorship/pamphlet.pdf`. **Sponsorship contact phone numbers are deliberately not stored in this public repo.** The public pamphlet says contacts are available from the organizing committee. To produce a copy with contacts for private sharing, create `sponsorship/contacts.local.json` (git-ignored) as `[{"name": "...", "phone": "..."}]` and run `build_pamphlet.py`; it then also writes `pamphlet-with-contacts.html` (git-ignored).

| Package | Contribution |
|---|---|
| Grand Patron | $15,000+ |
| Diamond Partner | $10,000 |
| Platinum Partner | $5,000 |
| Gold Partner | $4,000 |
| Silver Partner | $2,000 |
| Friends of DCE/DIT | $500+ |

| Meal and hospitality | Contribution |
|---|---|
| Friday Welcome Reception Partner | $1,500 |
| Saturday Networking Lunch Partner | $1,500 |
| Saturday Grand Gala Dinner Partner | $3,000 |
| Sunday Morning Breakfast Partner | $500 |

---

## 4. Repository layout

```
alumni-meet-2027/
├── build.py                 Generates every page in site/ (copy, nav, footer, price windows)
├── netlify.toml             Netlify config: publish the site/ folder
├── site/                    The website (plain HTML/CSS/JS, nothing to install to host it)
│   ├── index.html  about.html  program.html  speakers.html
│   ├── venue.html  sponsors.html  register.html
│   ├── styles.css           All styling and design tokens
│   ├── site.js              Nav, countdown, price-window logic
│   └── images/              Photos (see section 9)
├── flyer/
│   ├── flyer.html           Flyer source (1080×1080)
│   ├── flyer.png            Exported flyer for WhatsApp and social
│   └── hero-skyline.jpg
└── sponsorship/
    ├── build_pamphlet.py    Pamphlet content (tiers, benefits, contacts) and layout
    ├── pamphlet.html        Generated
    ├── pamphlet.pdf         Exported 4-page US Letter PDF
    └── hero-skyline.jpg
```

---

## 5. The website

### Pages and what each is for
| Page | Focus |
|---|---|
| `index.html` Home | Hero, the four events, last year's photo, a venue teaser and links to Speakers and Sponsors |
| `about.html` About | The vision (decades of friends joined by one alma mater, and what Jashn-e-Yaarana means), the two lineages (Delhi Polytechnic → DCE → DTU and DIT → NSIT → NSUT) and the four values |
| `program.html` Program | Each event in detail (description, dress where decided, timings) |
| `speakers.html` Speakers | Placeholder cards for speakers and bios, and what each bio will include |
| `venue.html` Venue | Maison 6405 details, map link, photos, "Around Atlanta" |
| `sponsors.html` Sponsors | Why partner. Contact details still to be added on this page |
| `register.html` Tickets and pricing | The DCEDIT Club event page image (linked) and the three price windows |

### Registration entry points
Every page except the price page has a **Register** button in the top menu, a closing "Be at the table" band, a footer link and a red bar fixed to the bottom of the screen (it shows "Presale ends Nov 15", then "Early bird ends Dec 15", then the dates). All of them open `register.html`, the price page. `register.html` itself has none of these (it would only link to itself). It shows a picture of the DCEDIT Club event page above the price windows; the picture and a text link under it both open the event page (the `PAYMENT_URL` constant in `build.py`) in a new tab. There is no separate Payment link button.

### Editing and previewing
Copy and layout live in `build.py` (shared constants at the top: `DATES`, `VENUE`, `ADDRESS`, `PAYMENT_URL`). Styling lives in `site/styles.css`.

```bash
python3 build.py                                  # regenerate site/*.html
python3 -m http.server 8765 --directory site      # preview at http://localhost:8765
```

After changing `styles.css` or `site.js`, bump the `?v=` number on the links in `build.py` so browsers load the new file.

### Design
- **Look:** photo-led and quiet, with a full-bleed Atlanta dusk hero, light serif headings and plenty of space. Sticky top menu that turns solid on scroll.
- **Colors:** warm white `#faf7f2`; DTU maroon `#701818` for emphasis; NSUT red as a small accent (`#c4161c`, text variant `#d40000`). Dark mode follows the visitor's system setting.
- **Fonts:** Instrument Serif (display) and Hanken Grotesk (body), from Google Fonts.
- **Responsive:** works from phone width up. The menu collapses to a Menu button below 1000px.

---

## 6. Deploying

The site is hosted on **Netlify** (site `jashn-e-yaarana-2027`, team `sumit-bhutani`). It is a manual upload and is **not linked to GitHub**, so pushing here does not update the live site. To publish changes, ask Claude Code to redeploy with the Netlify connector (it uploads the `site/` folder through `netlify.toml`).

To make deploys automatic, link the Netlify site to this GitHub repo (publish directory `site`, no build command, since the pages are already generated and committed). Remember to run `python3 build.py` and commit before pushing.

### Domain
No custom domain is set up yet.
- `dcedit.org` is already live (its DNS is on Cloudflare, in an account that has not been identified), so subdomains cannot be added until the owner is found.
- Recommended for all future events: a short domain with DCE/DIT and North America in the name, `dceditna.org` (looked unregistered at last check; confirm at a registrar). Plan: `2027.dceditna.org` per event year and `reunion.dceditna.org` always pointing at the current event.

---

## 6a. Handing the site to the DCEDIT team (upload zip)

The dcedit.org owner (Vishal Kumar) uploads the site as a zip and asked for a **single folder** with `index.html` and only web files: html, css, js, images. No `.py` or build folders.

- **Ready-made zip:** `dist/jashn-e-yaarana-site.zip` (about 1.5 MB, 26 files). `index.html` is at the root of the zip. It holds only the contents of `site/`.
- **Rebuild after any change:** run `./make-zip.sh` (it runs `build.py`, then zips `site/`). Commit the new zip so the download link stays current.
- **Download link for the latest zip:** https://github.com/sumit-bhutani/alumni-meet-2027/raw/main/dist/jashn-e-yaarana-site.zip
- **Hosting note:** all links are relative (`about.html`, `images/...`), so the site works in any folder, for example `/events/2027/yaarana/`. Serve it with a trailing slash or `index.html` in the address, otherwise the relative links break. Tested by unzipping into a nested folder and fetching every page and image.
- **Keep out of the zip:** `build.py`, `make-zip.sh`, `flyer/`, `sponsorship/`, `README.md` and `netlify.toml` stay in the repo only.

## 7. The flyer

`flyer/flyer.html` is the source. Export it to a PNG with Google Chrome:

```bash
cd flyer
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --window-size=1080,1080 --virtual-time-budget=8000 --screenshot=flyer.png "file://$PWD/flyer.html"
```

Notes:
- The flyer is shared as a small image on WhatsApp, so text is large. A committee reviewer said the first version's fonts were too small. Keep text at roughly 20px or more on the 1080px canvas.
- The bottom box says "Registration Page coming soon". Replace it with the real link or a QR code when the registration site exists.
- The flyer has no contact email yet.

---

## 8. The sponsorship pamphlet

Edit packages, benefits and contacts in `sponsorship/build_pamphlet.py`, then rebuild:

```bash
cd sponsorship
python3 build_pamphlet.py
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --no-pdf-header-footer --virtual-time-budget=10000 --print-to-pdf=pamphlet.pdf "file://$PWD/pamphlet.html"
```

Pages: 1 cover · 2 Grand Patron and Diamond · 3 Platinum, Gold, Silver and Friends · 4 meal and hospitality sponsors, then the contacts line (names and numbers appear only in the private version). "[Company / Individual]" in the naming-rights lines is a placeholder for the sponsor's name.

---

## 9. Photos and assets

- **Venue photos** (aerial, night, auditorium) and **Atlanta photos** (skyline at dusk, Piedmont Park): supplied by the committee.
- **Archive and memory photos** (polaroids on the home page, "Remember this?" film strip on About): copied from the committee's `dcedit.org/events/2027/yaarana/` page, with the credit "Photo: DTU Alumni Affairs" kept on the Class of '75 photo. Rights for the other archive images (Engifest, Old Delhi 1996, DTC bus and so on) are not verified.
- **Chai photo** (Chai Pila De card): free-to-use photo of a cup of masala chai by Harshit Mahabale on [Unsplash](https://unsplash.com/photos/a-person-holding-a-cup-of-tea-on-a-wooden-table-_w_9J1qJD9E) (Unsplash License). Swap it for a real tea-and-breakfast photo if the committee has one.
- **DC26 group photo** ("Last year" on the home page): from the committee's earlier website.
- The DTU and NSUT logos are **not** used. Their colors were sampled for the palette only. Using the emblems needs the institutions' permission.

---

## 10. Still open

- [x] Payment / registration link: `PAYMENT_URL` in `build.py` points to the event's DCEDIT Club page
- [ ] Event timings for all four events
- [ ] 2027 contact email for the flyer
- [ ] Sponsorship contact details on the website's Sponsors page
- [ ] What the NextGen and Parent tickets cover
- [ ] Speakers and bios
- [ ] Atlanta recommendations from local alumni
- [ ] Custom domain, and whose Cloudflare account holds `dcedit.org`
- [ ] Whether the About page keeps the heading "Not just to survive. To soar."
