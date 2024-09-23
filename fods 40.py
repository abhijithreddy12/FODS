import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = {
    'player_name': [f'Player_{i}' for i in range(1, 101)],
    'age': np.random.randint(18, 40, 100),
    'goals_scored': np.random.randint(0, 50, 100),
    'weekly_salary': np.random.uniform(5000, 200000, 100),
    'position': np.random.choice(['Forward', 'Midfielder', 'Defender', 'Goalkeeper'], 100)
}
df = pd.DataFrame(data)
top_goals = df.nlargest(5, 'goals_scored')
print("Top 5 players with highest goals scored:")
print(top_goals[['player_name', 'goals_scored']])
top_salaries = df.nlargest(5, 'weekly_salary')
print("\nTop 5 players with highest salaries:")
print(top_salaries[['player_name', 'weekly_salary']])
average_age = df['age'].mean()
print(f"\nAverage Age of Players: {average_age:.2f}")
above_average_age = df[df['age'] > average_age]
print("\nPlayers above the average age:")
print(above_average_age[['player_name', 'age']])


plt.figure(figsize=(8, 6))
sns.countplot(x='position', data=df)
plt.title('Distribution of Players by Position')
plt.xlabel('Position')
plt.ylabel('Number of Players')
plt.show()
