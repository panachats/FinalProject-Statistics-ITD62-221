import numpy as np
from scipy.stats import ttest_ind_from_stats
t_stat, p_value = ttest_ind_from_stats(
	mean1=120, std1=5.5, nobs1=100,
	mean2=170, std2=6.5, nobs2=100)

print("T-statistic value: ", t_stat)  
print("P-Value:",  p_value)
if p_value <= 0.05:
    print("Conclusion Reject H0")
else:
    print("Conclusion Do Not Reject H0")