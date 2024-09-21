import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy.stats as stats

# Creating the dataset
data = {
    'Age': [23, 25, 28, 30, 33, 35, 36, 38, 40, 42, 45, 47, 50, 52, 55, 58, 60, 62],
    '%Fat': [12.3, 10.8, 21.2, 19.3, 22.2, 23.4, 24.1, 25.2, 27.3, 28.4, 29.2, 30.1, 
             31.4, 32.2, 33.5, 34.8, 36.0, 37.3]
}

# Create DataFrame
df = pd.DataFrame(data)

# 1. Calculate the mean, median, and standard deviation
mean_age = df['Age'].mean()
median_age = df['Age'].median()
std_age = df['Age'].std()

mean_fat = df['%Fat'].mean()
median_fat = df['%Fat'].median()
std_fat = df['%Fat'].std()

print(f"Mean Age: {mean_age}, Median Age: {median_age}, Standard Deviation Age: {std_age}")
print(f"Mean %Fat: {mean_fat}, Median %Fat: {median_fat}, Standard Deviation %Fat: {std_fat}")

# 2. Draw the boxplots for age and %fat
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
sns.boxplot(data=df['Age'])
plt.title('Boxplot of Age')

plt.subplot(1, 2, 2)
sns.boxplot(data=df['%Fat'])
plt.title('Boxplot of %Fat')

plt.tight_layout()
plt.show()

# 3. Scatter plot
plt.figure(figsize=(6, 6))
plt.scatter(df['Age'], df['%Fat'], color='blue')
plt.title('Scatter plot of Age vs %Fat')
plt.xlabel('Age')
plt.ylabel('%Fat')
plt.grid(True)
plt.show()

# 4. Q-Q plot
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
stats.probplot(df['Age'], dist="norm", plot=plt)
plt.title('Q-Q Plot of Age')

plt.subplot(1, 2, 2)
stats.probplot(df['%Fat'], dist="norm", plot=plt)
plt.title('Q-Q Plot of %Fat')

plt.tight_layout()
plt.show()
