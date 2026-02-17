# Assignment-1 — Learn Probability Density Functions (Roll-Number-Parameterized Non-Linear Model)

**Student:** Rohan Malhotra  
**Roll Number (r):** 102303437  

This repo solves **Assignment-1**:

1. Load the India Air Quality dataset (Kaggle) and extract **NO2** as feature **x**.  
2. Transform each value via:  
   \[
   z = T_r(x) = x + a_r \sin(b_r x)
   \]
   where  
   \[
   a_r = 0.05 \cdot (r \bmod 7), \quad b_r = 0.3 \cdot ((r \bmod 5)+1)
   \]
3. Estimate parameters \(\lambda, \mu, c\) for:  
   \[
   \hat{p}(z) = c\, e^{-\lambda (z-\mu)^2}
   \]

## Parameters for r = 102303437
- \(r \bmod 7 = 5\) → \(a_r = 0.25\)
- \(r \bmod 5 = 2\) → \(b_r = 0.9\)

## Dataset
Kaggle: `india-air-quality-data`  
Place the dataset CSV(s) inside `data/`.

This solution auto-detects a CSV containing a `NO2` column (case-insensitive).  
Common file name in this dataset is often `city_day.csv`.

## Run (script)
```bash
python -m pip install -r requirements.txt
python src/solve.py --data_dir data
```

It prints \(\lambda, \mu, c\) and writes `results.json`.

## Run (notebook)
Open and run: `assignment1_solution.ipynb`

## Notes on estimation
We use **MLE for a normalized density**:
- \(\mu\) = sample mean of \(z\)
- variance MLE: \(\sigma^2 = \frac{1}{n}\sum (z-\mu)^2\)
- \(\lambda = \frac{1}{2\sigma^2}\)
- normalization implies \(c = \sqrt{\frac{\lambda}{\pi}}\)

(Optionally, the notebook also shows how to fit \(c\) directly to a histogram via non-linear least squares.)
