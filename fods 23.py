import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

def generate_trial_data(size_control, size_treatment, mean_control, mean_treatment, std_dev=1.0):
    control_group = np.random.normal(loc=mean_control, scale=std_dev, size=size_control)
    treatment_group = np.random.normal(loc=mean_treatment, scale=std_dev, size=size_treatment)
    return control_group, treatment_group
def hypothesis_test(control_group, treatment_group):
    t_stat, p_value = stats.ttest_ind(treatment_group, control_group)
    return t_stat, p_value
def plot_data(control_group, treatment_group, p_value):
    plt.figure(figsize=(10, 6))
    plt.hist(control_group, bins=20, alpha=0.5, label='Control Group (Placebo)', color='blue')
    plt.hist(treatment_group, bins=20, alpha=0.5, label='Treatment Group (New Drug)', color='green')
    plt.title(f"Clinical Trial Data (p-value: {p_value:.4f})", fontsize=16)
    plt.xlabel('Effectiveness Measure')
    plt.ylabel('Frequency')
    plt.legend(loc='upper right')
    plt.show()

def main():
    size_control = 100  
    size_treatment = 100  
    mean_control = 50  
    mean_treatment = 55 
    std_dev = 10
    
    control_group, treatment_group = generate_trial_data(size_control, size_treatment, mean_control, mean_treatment, std_dev)

    t_stat, p_value = hypothesis_test(control_group, treatment_group)
    print(f"T-statistic: {t_stat:.4f}, P-value: {p_value:.4f}")
    alpha = 0.05  # Significance level
    if p_value < alpha:
        print("The result is statistically significant. The new treatment shows a significant effect compared to the placebo.")
    else:
        print("The result is not statistically significant. No evidence of a significant effect of the new treatment compared to the placebo.")
    plot_data(control_group, treatment_group, p_value)

if __name__ == "__main__":
    main()
