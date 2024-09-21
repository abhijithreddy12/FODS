import numpy as np
import scipy.stats as stats

# Sample data (example values for the reduction in blood pressure)
drug_group = [12, 10, 14, 11, 9, 15, 13, 8, 12, 10, 14, 11, 9, 10, 13, 12, 9, 10, 11, 15, 13, 14, 12, 10, 11]
placebo_group = [4, 5, 3, 6, 4, 5, 3, 4, 2, 3, 5, 3, 4, 2, 5, 3, 4, 3, 5, 2, 4, 3, 5, 2, 3]

# Function to calculate confidence interval
def confidence_interval(data, confidence=0.95):
    n = len(data)  # sample size
    mean = np.mean(data)  # sample mean
    std_err = stats.sem(data)  # standard error of the mean
    h = std_err * stats.t.ppf((1 + confidence) / 2., n-1)  # margin of error
    return mean, mean-h, mean+h

# Confidence interval for drug group
mean_drug, lower_drug, upper_drug = confidence_interval(drug_group)
print(f"Drug Group: Mean = {mean_drug:.2f}, 95% CI = [{lower_drug:.2f}, {upper_drug:.2f}]")

# Confidence interval for placebo group
mean_placebo, lower_placebo, upper_placebo = confidence_interval(placebo_group)
print(f"Placebo Group: Mean = {mean_placebo:.2f}, 95% CI = [{lower_placebo:.2f}, {upper_placebo:.2f}]")
