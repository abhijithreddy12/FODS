import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

data = {
    'study_time': np.random.uniform(1, 10, 100),
    'exam_score': np.random.uniform(50, 100, 100)
}
df = pd.DataFrame(data)

plt.figure(figsize=(8, 6))
sns.scatterplot(x='study_time', y='exam_score', data=df)
plt.title('Study Time vs Exam Scores')
plt.xlabel('Study Time (hours)')
plt.ylabel('Exam Score')
plt.show()

correlation, _ = pearsonr(df['study_time'], df['exam_score'])
print(f"Pearson Correlation: {correlation:.2f}")
