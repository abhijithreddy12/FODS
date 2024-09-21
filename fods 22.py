import numpy as np
import pandas as pd
from scipy import stats
def generate_fake_reviews(num_reviews):
    np.random.seed(42)  
    return np.random.uniform(low=1.0, high=5.0, size=num_reviews)
def confidence_interval(data, confidence_level):
    mean = np.mean(data)
    std_error = stats.sem(data)
    ci = stats.t.interval(confidence_level, len(data) - 1, loc=mean, scale=std_error)
    return mean, ci

def main():
    reviews = pd.DataFrame({'rating': generate_fake_reviews(500)})
    confidence_level = float(input("Enter the confidence level (e.g., 0.95 for 95% confidence): "))
    mean_rating = reviews['rating'].mean()
    print(f"Average rating: {mean_rating:.4f}")
    mean, ci = confidence_interval(reviews['rating'], confidence_level)
    print(f"Confidence Interval: {ci[0]:.4f} to {ci[1]:.4f}")
    print(f"True population mean rating is likely between {ci[0]:.4f} and {ci[1]:.4f} at a {confidence_level*100:.0f}% confidence level.")
    
if __name__ == "__main__":
    main()
