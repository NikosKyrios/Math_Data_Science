import scipy.stats as stats
import numpy as np

### Task Group 1 ###
## Task 1: 
lam = 9

## Task 2:
print(stats.poisson.pmf(lam, lam))

## Task 3:
print(stats.poisson.cdf(2, lam))

## Task 4:
print(1 - stats.poisson.cdf(6, lam))

### Task Group 2 ###
## Task 5:
year_defects = stats.poisson.rvs(lam, size = 365)


## Task 6:
print(year_defects[:7])
## Task 7:

## Task 8:
print(sum(year_defects))
## Task 9:
print(np.mean(year_defects))
## Task 10:
print(year_defects.max())
## Task 11:
print(1 - stats.poisson.cdf(29, 10))

### Extra Bonus ###
# Task 12

print(stats.poisson.ppf(0.65,9))

# Task 13
print(sum(year_defects >= 20) / len(year_defects))