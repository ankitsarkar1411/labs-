from collections import Counter

filename = input("Enter the filename: ")

with open(filename, 'r') as file:
    text = file.read()

words = text.lower().split()

word_counts = Counter(words)

most_common_words = word_counts.most_common(10)

print("10 Most Frequently Appearing Words:")
for word, count in most_common_words:
    print(f"{word}: {count}")
