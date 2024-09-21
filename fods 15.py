import pandas as pd

data = {'post_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'likes': [100, 150, 100, 200, 150, 150, 100, 250, 200, 300]}

interaction_data = pd.DataFrame(data)


likes_frequency_distribution = interaction_data['likes'].value_counts()


print("Frequency Distribution of Likes:")
print(likes_frequency_distribution)
