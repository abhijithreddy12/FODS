import string
from collections import Counter
def word_frequency_distribution(file_path):
    # Step 1: Read the text document
    with open(file_path, 'r') as file:
        text = file.read()
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    words = text.split()
    word_count = Counter(words)
    return word_count
file_path = 'sample_text.txt'
word_frequencies = word_frequency_distribution(file_path)

# Print the word frequency distribution
print("Word Frequency Distribution:")
for word, freq in word_frequencies.items():
    print(f"{word}: {freq}")
