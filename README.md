============================================================
STEP 1: Load and preview raw data
============================================================
Total rows loaded: 2000
Columns: ['rank ', 'global company', 'country', 'sales ', 'profit ', 'assets', 'market value']

============================================================
STEP 2: Clean 'profit' and 'assets' columns
         (strip $, B, spaces and convert to float)
============================================================
Sample cleaned profits : [89.8, 54.03, 105.36, 42.12, 46.89]
Sample cleaned assets  : [958.78, 5518.51, 576.04, 3954.69, 4746.95]

============================================================
STEP 3: Drop rows with missing/zero assets or missing profit
============================================================
Rows before cleaning : 2000
Rows after  cleaning : 2000
Rows dropped         : 0

============================================================
STEP 4: Calculate ROA = Profit / Assets  (per company)
============================================================
First 10 companies with ROA:
Company                                   Profit         Assets                ROA
----------------------------------------------------------------------------------
Berkshire Hathaway                  89.8000000000 958.7800000000       0.0936606938
ICBC                                54.0300000000 5518.5100000000       0.0097906863
Saudi Arabian Oil Company (Saudi Aramco) 105.3600000000 576.0400000000       0.1829039650
JPMorgan Chase                      42.1200000000 3954.6900000000       0.0106506452
China Construction Bank             46.8900000000 4746.9500000000       0.0098779216
Amazon                              33.3600000000 420.5500000000       0.0793246939
Apple                               100.5600000000 381.1900000000       0.2638054513
Agricultural Bank of China          37.3800000000 4561.0500000000       0.0081954813
Bank of America                     31.0000000000 3238.2200000000       0.0095731606
Toyota Motor                        28.1500000000 552.4600000000       0.0509539152
  ... (2000 companies total)

============================================================
STEP 5: Calculate Mean ROA
         Mean = Sum(ROA) / N
============================================================
  Sum of all ROA values : 155.6866763786
  Number of companies   : 2000
  Mean ROA              : 0.0778433382

============================================================
STEP 6: Calculate Standard Deviation of ROA (sample, ddof=1)
         Std = sqrt( Sum((ROA_i - Mean)^2) / (N-1) )
============================================================
  Sum of squared deviations : 611.5267013589
  Variance (sum / (N-1))    : 0.3059163088
  Standard Deviation        : 0.5530970158

============================================================
STEP 7: Calculate Coefficient of Variation (CV)
         CV = (Std / Mean) x 100  [expressed as %]
============================================================
  Standard Deviation : 0.5530970158
  Mean ROA           : 0.0778433382
  CV (raw)           : 710.5258184165

============================================================
FINAL ANSWER
============================================================
  Coefficient of Variation (CV) of ROA = 710.53%
============================================================
