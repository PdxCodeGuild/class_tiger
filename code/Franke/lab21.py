import string, re, math #math rounds up
from collections import Counter #simple way to count word occurence
import nltk #
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize #creates a list of words

with open('busterbeartwins.txt', 'r', encoding= 'utf-8') as f: # this is because my file is already in this folder
    book = f.read()# gives one big string
    translator = str.maketrans('', '', string.punctuation)  # removes all punctuation
    no_punct = book.translate(translator)
    low_format = no_punct.lower()
    word_list = low_format.split() #list of each word ignores white spaces

def dict_word_and_count():
    d = {}
    for word in word_list:
        if word not in d:
            d[word] = 0
        d[word] += 1
    return d

def top_10_words_no_filter():
    words = list(d.items()) # .items() returns a list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
            print(words[i])

def filtering():
    stop_words = set(stopwords.words('english'))
#word_tokens = word_tokenize(low_format) same as text.split
    filtered_sentence = [w for w in word_list if not w in stop_words]
    return filtered_sentence

def top_10_words_with_filter():
#using counter module in collection
    b = Counter(filtering()).most_common() # returns list of tuple with count
    b.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(b))):  # print the top 10 words, or all of them, whichever is smaller
        print(b[i])

#words = re.findall('\w+', low_format) same as .split

def word_pairs():
    pair = zip(filtering(),filtering()[1:])
    pairs = list(pair)
    return pairs

def count_word_pairs():
    dict_pairs = {}
    for i in word_pairs():
        if i not in dict_pairs:
            dict_pairs[i] = 0
    dict_pairs[i] += 1
    g = Counter(dict_pairs).most_common() # returns list of tuple with count
    g.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(g))):  # print the top 10 words, or all of them, whichever is smaller
        print(g[i])



