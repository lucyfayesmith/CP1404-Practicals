"""
CP1404 Practical
Do from scratch exercise - Word Counter
"""
word_count = {}
text = input("Text: ")

words = text.split()

for word in words:
    count = word_count.get(word, 0)
    word_count[word] = count + 1

words = list(word_count.keys())
words.sort()

word_length = max((len(word) for word in words))
"""struggled with ^, used solutions as reference"""

for word in words:
    print("{:{}} : {}".format(word, word_length, word_count[word]))

