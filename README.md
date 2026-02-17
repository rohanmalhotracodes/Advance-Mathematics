# Assignment-1 — Learn Probability Density Functions using Roll-Number-Parameterized Non-Linear Model

**Student:** Rohan Malhotra  
**Roll Number (r):** 102303437  

---

## Objective
This repository solves **Assignment-1**, where we:

1. Use **NO2** values from the Kaggle India Air Quality dataset as feature **x**  
2. Transform each x into z using a roll-number-based non-linear transformation  
3. Estimate parameters **λ, μ, c** of the probability density function:

\[
\hat{p}(z)=c\,e^{-\lambda(z-\mu)^2}
\]

---

## Dataset
Kaggle Dataset: **India Air Quality Data**  
https://www.kaggle.com/datasets/shrutibhargava94/india-air-quality-data  

This solution downloads the dataset automatically using:

```python
import kagglehub
path = kagglehub.dataset_download("shrutibhargava94/india-air-quality-data")
```

---

## Step 1 — Transformation (x → z)

\[
z = T_r(x) = x + a_r \sin(b_r x)
\]

Where:

\[
a_r = 0.05 \cdot (r \bmod 7), \quad b_r = 0.3 \cdot ((r \bmod 5)+1)
\]

For **r = 102303437**:

- \(r \bmod 7 = 5 \Rightarrow a_r = 0.25\)
- \(r \bmod 5 = 2 \Rightarrow b_r = 0.9\)

So:

\[
z = x + 0.25\sin(0.9x)
\]

---

## Step 2 — Parameter Estimation (λ, μ, c)

We estimate the parameters using **Maximum Likelihood Estimation (MLE)** assuming a valid probability density function.

For a normalized PDF:

\[
\int_{-\infty}^{\infty} c e^{-\lambda(z-\mu)^2}\,dz = 1
\Rightarrow c = \sqrt{\frac{\lambda}{\pi}}
\]

---

## Final Estimated Parameters

### ✅ Normalized MLE (Recommended for Submission)
These are the values to submit in the Google Form:

- **λ (Lambda)** = `0.0014590905`
- **μ (Mean)**   = `25.8027083605`
- **c**          = `0.0215509383`

---

### Optional: Histogram Curve Fit (Extra)
This version fits the function directly to the histogram density:

- **λ (Lambda)** = `0.0021884980`
- **μ (Mean)**   = `20.3521973452`
- **c**          = `0.0272193072`

---

## What to Submit
The submission form asks:

- **Estimated value of Lambda** → submit **Normalized MLE λ**
- **Estimated value of the mean** → submit **Normalized MLE μ**

So submit:

✅ **λ = 0.0014590905**  
✅ **μ = 25.8027083605**

---

## Results Visualization (Images)

### Density Fit Plot
![Density Fit](images/density_fit.png)

---

## Repository Structure
```
assignment1_rohan_malhotra/
│── assignment1_solution.ipynb
│── src/
│   └── solve.py
│── requirements.txt
│── results.json   (generated after running)
│── images/
│   └── density_fit.png
```

---

## How to Run

### Run Notebook
Open and run:

- `assignment1_solution.ipynb`

### Run Script
```bash
pip install -r requirements.txt
python src/solve.py
```

---

## Output
The program prints:
- \(a_r, b_r\)
- estimated \(λ, μ, c\)
- number of data points used

And saves results into:
- `results.json`

---

## Submission Link
https://forms.gle/jYF3MDKozRnSCHvR8
