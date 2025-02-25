"""
Word Occurrences
Writing Code: 15 minutes
Debugging: 10 minutes
Total: 25 minutes
"""
text = input("Text: ")
word_counts = {}
words = text.split()
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1
sorted_words = sorted(word_counts.keys())
max_word_length = max(len(word) for word in sorted_words)
for word in sorted_words:
    print(f"{word:{max_word_length}} : {word_counts[word]}")
