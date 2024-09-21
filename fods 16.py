from collections import Counter
import string
reviews = [
    "This product is great! I love it.",
    "The product is okay, but it could be better.",
    "I am not satisfied with this product.",
    "Amazing product, I will definitely recommend it to my friends!",
    "Terrible! The product broke after one week."
]
reviews_combined = ' '.join(reviews)
reviews_combined = reviews_combined.lower()
words = reviews_combined.split()
table = str.maketrans('', '', string.punctuation)
words = [word.translate(table) for word in words]
stop_words = set([
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", 
    "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", 
    "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", 
    "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", 
    "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", 
    "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", 
    "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", 
    "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", 
    "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", 
    "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", 
    "now"
])
words_filtered = [word for word in words if word not in stop_words and word != '']
word_freq = Counter(words_filtered)
print("Word Frequency Distribution:")
for word, freq in word_freq.most_common():
    print(f"{word}: {freq}")


