import numpy as np
from scipy import stats

def generate_random_data(size, mean, std_dev):
    # Generate synthetic data (e.g., normally distributed)
    return np.random.normal(loc=mean, scale=std_dev, size=size)

def sample_data(data, sample_size):
    # Randomly sample data from the dataset
    return np.random.choice(data, size=sample_size, replace=False)

def point_estimate(sample):
    # Calculate the mean of the sample
    return np.mean(sample)

def confidence_interval(sample, confidence_level):
    # Calculate the confidence interval for the mean
    mean = np.mean(sample)
    std_error = stats.sem(sample)
    ci = stats.t.interval(confidence_level, len(sample) - 1, loc=mean, scale=std_error)
    return ci

def estimate_precision(ci):
    # Estimate the precision as the range of the confidence interval
    return ci[1] - ci[0]

def main():
    # User provides the data or we can generate random data for testing
    # Uncomment below line if you want to use predefined data:
    # data = np.array([1.5, 2.1, 2.5, 1.9, 3.2, 2.7, 2.0, 2.8, 1.8, 2.4])
    
    # Or generate random data for testing (mean=2.0, std_dev=0.5, size=1000):
    data = generate_random_data(size=1000, mean=2.0, std_dev=0.5)

    # Get user inputs
    sample_size = int(input("Enter the sample size: "))
    confidence_level = float(input("Enter the confidence level (e.g., 0.95 for 95% confidence): "))
    desired_precision = float(input("Enter the desired level of precision: "))
    
    # Draw a random sample
    sample = sample_data(data, sample_size)
    
    # Calculate point estimate
    mean_estimate = point_estimate(sample)
    print(f"Point estimate of the mean: {mean_estimate:.4f}")
    
    # Calculate confidence interval
    ci = confidence_interval(sample, confidence_level)
    precision = estimate_precision(ci)
    print(f"Confidence Interval: {ci[0]:.4f} to {ci[1]:.4f}")
    print(f"Precision (CI range): {precision:.4f}")
    
    # Check if the desired precision is met
    if precision <= desired_precision:
        print(f"The precision is within the desired level of {desired_precision:.4f}.")
    else:
        print(f"The precision is not within the desired level. Consider increasing the sample size.")
    
if __name__ == "__main__":
    main()
