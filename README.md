# Jashn-e-Yaarana: DCE / DIT / DTU / NSIT / NSUT World Alumni Meet 2027

Atlanta, Georgia, USA · April 16–18, 2027

| Folder | What it is |
|---|---|
| `site/` | The website (static HTML/CSS/JS, no build step needed to host it) |
| `build.py` | Generates the pages in `site/` from one place. Run `python3 build.py` after editing copy |
| `flyer/` | Event flyer: `flyer.html` is the source, `flyer.png` the 1080×1080 export |
| `sponsorship/` | Sponsorship pamphlet: `build_pamphlet.py` builds `pamphlet.html`, `pamphlet.pdf` is the export |
| `netlify.toml` | Netlify config (publishes `site/`) |

Live site: https://jashn-e-yaarana-2027.netlify.app

## Final facts (keep consistent everywhere)
- **Name:** DCE · DIT · DTU · NSIT · NSUT **World** Alumni Meet 2027
- **Dates:** April 16–18, 2027, Atlanta, Georgia, USA
- **Events:** Fri Apr 16 evening *Dhamaal* (welcome night) · Sat Apr 17 daytime *Ek Saath* (Leadership Conclave) · Sat Apr 17 evening *Jalwa* (gala and awards) · Sun Apr 18 morning *Chai Pila De* (chai and breakfast)
- **Tagline:** The years change. But the friendship stays forever.

## To do before sharing widely
- Registration/payment link: set `REGISTER_URL` in `build.py`, rebuild, redeploy
- Event timings, contact email, sponsorship contact
- Custom domain

## Re-render the flyer / pamphlet (needs Google Chrome)
```bash
cd flyer && "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --window-size=1080,1080 --virtual-time-budget=8000 --screenshot=flyer.png "file://$PWD/flyer.html"
cd sponsorship && python3 build_pamphlet.py && "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --no-pdf-header-footer --virtual-time-budget=10000 --print-to-pdf=pamphlet.pdf "file://$PWD/pamphlet.html"
```
