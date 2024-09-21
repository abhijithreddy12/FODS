import numpy as np
student_scores = np.array([
    [85, 92, 78, 90],
    [88, 76, 85, 93],
    [75, 85, 89, 80],
    [90, 88, 92, 84]
])
subject_averages = np.mean(student_scores, axis=0)
subjects = ['Math', 'Science', 'English', 'History']
max_avg_index = np.argmax(subject_averages)
best_subject = subjects[max_avg_index]
print("Average scores for each subject:")
for i, subject in enumerate(subjects):
    print(f"{subject}: {subject_averages[i]:.2f}")

print(f"\nThe subject with the highest average score is: {best_subject}")
