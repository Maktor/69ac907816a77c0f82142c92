import pandas as pd
import numpy as np

df = pd.read_csv("forbes2000-2022.csv")

print("=" * 60)
print("STEP 1: Load and preview raw data")
print("=" * 60)
print(f"Total rows loaded: {len(df)}")
print(f"Columns: {list(df.columns)}")
print()

print("=" * 60)
print("STEP 2: Clean 'profit' and 'assets' columns")
print("         (strip $, B, spaces and convert to float)")
print("=" * 60)

def clean_currency(series):
    s = series.astype(str).str.strip().str.replace(r'[$,\s]', '', regex=True)
    numeric = s.str.replace(r'[BMbm]$', '', regex=True).replace('', np.nan)
    suffix  = s.str.extract(r'([BMbm])$', expand=False).str.upper()
    values  = pd.to_numeric(numeric, errors='coerce')
    values  = np.where(suffix == 'M', values / 1000, values)
    return pd.Series(values, index=series.index, dtype=float)

df['profit_clean'] = clean_currency(df['profit '])
df['assets_clean'] = clean_currency(df['assets'])

print(f"Sample cleaned profits : {df['profit_clean'].head(5).tolist()}")
print(f"Sample cleaned assets  : {df['assets_clean'].head(5).tolist()}")
print()

before = len(df)
df = df.dropna(subset=['profit_clean', 'assets_clean'])
df = df[df['assets_clean'] != 0]
after = len(df)

print("=" * 60)
print("STEP 3: Drop rows with missing/zero assets or missing profit")
print("=" * 60)
print(f"Rows before cleaning : {before}")
print(f"Rows after  cleaning : {after}")
print(f"Rows dropped         : {before - after}")
print()

print("=" * 60)
print("STEP 4: Calculate ROA = Profit / Assets  (per company)")
print("=" * 60)

df['ROA'] = df['profit_clean'] / df['assets_clean']

print("First 10 companies with ROA:")
print(f"{'Company':<35} {'Profit':>12} {'Assets':>14} {'ROA':>18}")
print("-" * 82)
for _, row in df.head(10).iterrows():
    print(f"{str(row['global company']):<35} "
          f"{row['profit_clean']:>12.10f} "
          f"{row['assets_clean']:>14.10f} "
          f"{row['ROA']:>18.10f}")
print(f"  ... ({after} companies total)")
print()

print("=" * 60)
print("STEP 5: Calculate Mean ROA")
print("         Mean = Sum(ROA) / N")
print("=" * 60)

roa_sum  = df['ROA'].sum()
n        = len(df['ROA'])
mean_roa = roa_sum / n

print(f"  Sum of all ROA values : {roa_sum:.10f}")
print(f"  Number of companies   : {n}")
print(f"  Mean ROA              : {mean_roa:.10f}")
print()

print("=" * 60)
print("STEP 6: Calculate Standard Deviation of ROA (sample, ddof=1)")
print("         Std = sqrt( Sum((ROA_i - Mean)^2) / (N-1) )")
print("=" * 60)

df['ROA_minus_mean']  = df['ROA'] - mean_roa
df['squared_dev']     = df['ROA_minus_mean'] ** 2

sum_sq_dev = df['squared_dev'].sum()
variance   = sum_sq_dev / (n - 1)
std_roa    = np.sqrt(variance)

print(f"  Sum of squared deviations : {sum_sq_dev:.10f}")
print(f"  Variance (sum / (N-1))    : {variance:.10f}")
print(f"  Standard Deviation        : {std_roa:.10f}")
print()

print("=" * 60)
print("STEP 7: Calculate Coefficient of Variation (CV)")
print("         CV = (Std / Mean) x 100  [expressed as %]")
print("=" * 60)

cv = (std_roa / mean_roa) * 100

print(f"  Standard Deviation : {std_roa:.10f}")
print(f"  Mean ROA           : {mean_roa:.10f}")
print(f"  CV (raw)           : {cv:.10f}")
print()

print("=" * 60)
print("FINAL ANSWER")
print("=" * 60)
print(f"  Coefficient of Variation (CV) of ROA = {cv:.2f}%")
print("=" * 60)
