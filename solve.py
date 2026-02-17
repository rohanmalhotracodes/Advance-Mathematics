#!/usr/bin/env python3
"""
Assignment-1 solver (script):
- Loads Kaggle India Air Quality dataset CSV(s) from --data_dir
- Extracts NO2 as x
- Computes z = x + ar*sin(br*x) for roll number r
- Estimates (lambda, mu, c) for p(z) = c * exp(-lambda (z-mu)^2)

Outputs:
- Prints parameters
- Writes results.json
"""

from __future__ import annotations
import argparse, json, math, os
from pathlib import Path
import numpy as np
import pandas as pd

ROLL_NUMBER = 102303437

def ar_br(r: int) -> tuple[float, float]:
    ar = 0.05 * (r % 7)
    br = 0.3 * ((r % 5) + 1)
    return ar, br

def find_csv_with_no2(data_dir: Path) -> tuple[Path, str]:
    csvs = sorted([p for p in data_dir.glob("*.csv")])
    if not csvs:
        raise FileNotFoundError(f"No .csv found in {data_dir.resolve()}. Put Kaggle CSV(s) in data/.")
    for p in csvs:
        try:
            df = pd.read_csv(p, nrows=5)
        except Exception:
            continue
        cols = {c.lower(): c for c in df.columns}
        if "no2" in cols:
            return p, cols["no2"]
    raise ValueError("Couldn't find a CSV containing a 'NO2' column (case-insensitive).")

def load_no2_series(csv_path: Path, no2_col: str) -> np.ndarray:
    df = pd.read_csv(csv_path)
    x = pd.to_numeric(df[no2_col], errors="coerce").to_numpy(dtype=float)
    x = x[np.isfinite(x)]
    if x.size == 0:
        raise ValueError(f"NO2 column '{no2_col}' has no numeric values after cleaning.")
    return x

def transform_x_to_z(x: np.ndarray, ar: float, br: float) -> np.ndarray:
    return x + ar * np.sin(br * x)

def estimate_params_mle(z: np.ndarray) -> tuple[float, float, float]:
    # Normalized density: p(z) = c * exp(-lambda (z-mu)^2), where c = sqrt(lambda/pi)
    mu = float(np.mean(z))
    s2 = float(np.mean((z - mu) ** 2))  # MLE variance (divide by n)
    if s2 <= 0:
        raise ValueError("Variance is non-positive after cleaning; cannot estimate lambda.")
    lam = 1.0 / (2.0 * s2)
    c = math.sqrt(lam / math.pi)
    return lam, mu, c

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data_dir", default="data", help="Folder containing the Kaggle CSV(s).")
    ap.add_argument("--roll", type=int, default=ROLL_NUMBER, help="University roll number r.")
    ap.add_argument("--out", default="results.json", help="Output JSON filename.")
    args = ap.parse_args()

    data_dir = Path(args.data_dir)
    csv_path, no2_col = find_csv_with_no2(data_dir)

    x = load_no2_series(csv_path, no2_col)
    ar, br = ar_br(args.roll)
    z = transform_x_to_z(x, ar, br)

    lam, mu, c = estimate_params_mle(z)

    results = {
        "student": "Rohan Malhotra",
        "roll_number": args.roll,
        "csv_used": str(csv_path),
        "no2_column": no2_col,
        "ar": ar,
        "br": br,
        "lambda": lam,
        "mu": mu,
        "c": c,
        "n_points_used": int(z.size),
    }

    print("=== Assignment-1 Parameter Estimates ===")
    print(f"CSV used      : {csv_path}")
    print(f"NO2 column    : {no2_col}")
    print(f"ar, br        : {ar:.6f}, {br:.6f}")
    print(f"lambda (λ)    : {lam:.10f}")
    print(f"mu (μ)        : {mu:.10f}")
    print(f"c             : {c:.10f}")
    print(f"n points used : {z.size}")

    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    main()
