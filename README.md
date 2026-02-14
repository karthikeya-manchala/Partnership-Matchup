# Partnership Matchup Ratings (GitHub Pages)

This folder is a ready-to-host static site.

## Files
- `index.html` — the web app
- `export_pivots.py` — helper script to export your Python pivots/baseline to JSON
- `data/` — put these JSON files here:
  - `run_pivot.json` (required)
  - `wicket_pivot.json` (required)
  - `baseline.json` (required)
  - `weights.json` (required)
  - `balls_pivot.json` (optional)

## How to generate data JSON
1. In the environment where you computed `run_pivot`, `wicket_pivot`, `balls_pivot`, and `baseline`,
   copy `export_pivots.py` next to your notebook/script and run it.
2. It will create a `data/` folder with the JSON files.
3. Copy those JSON files into this site's `data/` folder.

## Deploy on GitHub Pages
1. Create a repo (e.g. `partnership-matchup-tool`).
2. Upload **index.html** and the **data/** folder to the repo root.
3. GitHub repo → Settings → Pages:
   - Source: `Deploy from a branch`
   - Branch: `main` / `(root)`
4. Open the Pages URL.

## Local test
Because the app uses `fetch()` for JSON, run a simple local server:

- Python: `python -m http.server 8000`
- Then open: `http://localhost:8000`

## Logic parity with your Python
- `run_pair = alpha*max(A_run,B_run) + (1-alpha)*min(A_run,B_run)`
- `wicket_pair = alpha*min(A_wk,B_wk) + (1-alpha)*max(A_wk,B_wk)`
- z-scores computed per bowl type using `baseline.json`
- weighted overall scores computed using `weights.json`
