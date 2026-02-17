# Assignment-1 — Learn Probability Density Functions (Roll-Number-Parameterized Non-Linear Model)

**Student:** Rohan Malhotra  
**Roll Number (r):** 102303437  

This repository contains the complete solution for Assignment-1:

1. Download the Kaggle India Air Quality dataset  
2. Extract NO2 as feature (x)  
3. Transform x → z using the roll-number parameterized function  
4. Learn parameters λ, μ and c for the given PDF  

---

## Dataset
Kaggle Dataset Link:  
https://www.kaggle.com/datasets/shrutibhargava94/india-air-quality-data  

Feature used: **NO2**

---

## Step-1: Transformation

Transformation function:

z = Tr(x) = x + ar * sin(br * x)

where:

ar = 0.05 * (r mod 7)  
br = 0.3 * ((r mod 5) + 1)

For roll number r = 102303437:

- r mod 7 = 5  →  ar = 0.25
- r mod 5 = 2  →  br = 0.9

So:

z = x + 0.25 * sin(0.9 * x)

---

## Step-2: PDF Parameter Learning

We estimate parameters for:

p̂(z) = c * exp( -λ * (z - μ)² )

---

## Histogram of Z and fitted curves 
<img width="786" height="470" alt="Unknown" src="https://github.com/user-attachments/assets/f57f1242-9776-4173-a92f-0705ffe4664b" />


---
## Final Estimated Parameters (Computed)

### Normalized MLE (Recommended)
- λ (lambda) = 0.0014590905  
- μ (mean)   = 25.8027083605  
- c          = 0.0215509383  

### Histogram Curve-Fit
- λ (lambda) = 0.0021884980  
- μ (mean)   = 20.3521973452  
- c          = 0.0272193072  

---

## How to Run (Notebook)
Open and run:

- `assignment1_solution_kagglehub.ipynb`

---

## How to Run (Script)

```bash
python -m pip install -r requirements.txt
python src/solve_kagglehub.py
