#count_words.py
import string
with open('song.txt', 'r', encoding="utf-8-sig" ) as f:
    content = f.read().strip()
    translator = str.maketrans('', '', string.punctuation)
    string_without_punct = content.translate(translator)
    content = content.replace('\n',' ').replace('.', '').replace(',', '')
    content=content.lower().split(' ')
counter = 0
STOPWORDS = ['i', 'me', 'my', 'myself', 'we', 'our', 'and', 'to', ' ', 'at']


word_dict = {x:content.count(x) for x in content}
words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])


print(word_dict)
