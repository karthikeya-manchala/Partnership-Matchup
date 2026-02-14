"""Export pivots + baseline to JSON for the GitHub Pages tool.

Run this in the same environment where you computed:
  run_pivot, wicket_pivot, balls_pivot, baseline (dict), BOWL_WEIGHTS (dict)

It will write JSON files into ./data for the web app:
  data/run_pivot.json
  data/wicket_pivot.json
  data/balls_pivot.json
  data/baseline.json
  data/weights.json

Tip: keep only batters above your sample threshold before exporting if files are huge.
"""

import json
from pathlib import Path

OUT = Path("data")
OUT.mkdir(exist_ok=True)

def pivot_to_nested_json(pivot_df):
    bats = pivot_df.index.tolist()
    bowl_types = pivot_df.columns.tolist()
    values = {}
    for bat in bats:
        row = pivot_df.loc[bat].to_dict()
        # ensure plain floats for json
        values[bat] = {bt: float(row.get(bt, 0) or 0) for bt in bowl_types}
    return {"bats": bats, "bowl_types": bowl_types, "values": values}

# --- REQUIRED ---
run_payload = pivot_to_nested_json(run_pivot)
wk_payload  = pivot_to_nested_json(wicket_pivot)

(OUT / "run_pivot.json").write_text(json.dumps(run_payload, ensure_ascii=False), encoding="utf-8")
(OUT / "wicket_pivot.json").write_text(json.dumps(wk_payload, ensure_ascii=False), encoding="utf-8")

# --- OPTIONAL BUT RECOMMENDED ---
if "balls_pivot" in globals():
    balls_payload = pivot_to_nested_json(balls_pivot)
    (OUT / "balls_pivot.json").write_text(json.dumps(balls_payload, ensure_ascii=False), encoding="utf-8")

# --- REQUIRED ---
(OUT / "baseline.json").write_text(json.dumps(baseline, ensure_ascii=False), encoding="utf-8")

# --- REQUIRED (weights used for overall compatibility) ---
if "BOWL_WEIGHTS" in globals():
    (OUT / "weights.json").write_text(json.dumps(BOWL_WEIGHTS, ensure_ascii=False), encoding="utf-8")
else:
    # fallback: equal weights
    bowl_types = run_pivot.columns.tolist()
    w = {bt: 1/len(bowl_types) for bt in bowl_types}
    (OUT / "weights.json").write_text(json.dumps(w, ensure_ascii=False), encoding="utf-8")

print("Wrote JSON files to:", OUT.resolve())
