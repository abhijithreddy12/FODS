import numpy as np
import scipy.stats as stats


# Sample data for conversion rates (percentage of visitors converted)
# Group A: Conversion rates for design A
conversion_rate_A = [0.12, 0.15, 0.10, 0.14, 0.11, 0.16, 0.13, 0.12, 0.11, 0.14]

# Group B: Conversion rates for design B
conversion_rate_B = [0.18, 0.17, 0.15, 0.19, 0.16, 0.20, 0.18, 0.17, 0.16, 0.19]

# Perform the independent two-sample t-test
t_stat, p_value = stats.ttest_ind(conversion_rate_A, conversion_rate_B)

# Results
alpha = 0.05  # Significance level

print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.4f}")

if p_value < alpha:
    print("Reject the null hypothesis: There is a statistically significant difference in conversion rates.")
else:
    print("Fail to reject the null hypothesis: There is no statistically significant difference in conversion rates.")
