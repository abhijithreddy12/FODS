from collections import Counter
import string
import matplotlib.pyplot as plt

# Sample customer feedback dataset (embedded in the code)
feedback_data = [
    "This product is amazing! Highly recommend it.",
    "The product could be better, but it works okay.",
    "I don't like the product. It broke after one use.",
    "The customer service was excellent. The product is great!",
    "Terrible experience! The product arrived broken and customer service was unhelpful.",
    "Good product, but shipping was slow.",
    "I'm very happy with the product. Works perfectly!",
    "The product is not what I expected. Disappointing.",
    "Fantastic product, exceeded my expectations!",
    "Not satisfied at all, wouldn't buy again."
]

# Stopwords to remove
stop_words = set([
    "i", "me", "my", "we", "you", "your", "he", "she", "it", "they", "them", "this", 
    "that", "is", "am", "are", "was", "were", "be", "been", "the", "a", "an", "and", 
    "but", "if", "or", "because", "as", "at", "for", "with", "about", "by", "on", "in", "to", "of"
])

# Function to preprocess and clean the feedback
def preprocess(feedback):
    # Convert to lowercase, remove punctuation, and split into words
    feedback = feedback.lower().translate(str.maketrans('', '', string.punctuation))
    words = feedback.split()
    # Remove stopwords
    return [word for word in words if word not in stop_words]

# Collect all words from the feedback dataset
all_words = []
for feedback in feedback_data:
    all_words.extend(preprocess(feedback))

# Count the frequency of each word
word_count = Counter(all_words)

# Get top N most frequent words
N = 10
top_words = word_count.most_common(N)

# Display the top N words and their frequencies
print(f"Top {N} Most Frequent Words:")
for word, freq in top_words:
    print(f"{word}: {freq}")

# Plot a bar graph of the top N words
words, frequencies = zip(*top_words)
plt.bar(words, frequencies)
plt.xlabel('Words')
plt.ylabel('Frequencies')
plt.title(f'Top {N} Most Frequent Words')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
