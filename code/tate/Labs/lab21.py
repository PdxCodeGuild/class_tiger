'''
lab21: Count words
'''
import string

my_file = 'jungle-book.txt'

stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

def read_file():
    with open(my_file,'r') as f:
        contents = f.read()
    return contents

def remove_punc(my_s):
    ''' input a string, returns a string without punctuation'''
    translator_remove_punc = str.maketrans('','',string.punctuation)
    return my_s.translate(translator_remove_punc)
def remove_newlines(my_s):
    ''' input a string, returns a string without \\n'''
    return my_s.replace('\n',' ')

def get_words():
    '''
    uses the function read_file() to read the text file my_file.
    Out puts the list of words without punctuation, removes newlines
    spaces, as well as stopwords (CURRRENTLY TURNED OFF)
    '''
    contents = read_file()
    contents = contents.lower()
    contents = remove_punc(contents)
    contents = remove_newlines(contents)
    contents_list = contents.split(' ')
    contents_list = [x for x in contents_list if x != '']
    contents_list = [x for x in contents_list if x != ' ']
    # contents_list = [x for x in contents_list if x not in stopwords]
    return contents_list

def get_words_dict(word_list):
    '''
    Takes in a list, returns a dictionary where the values are the number of
    times each item of the list occurs
    '''
    word_dict = {}
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict.update({word:1})
    return word_dict

def get_frequent(input_dict):
    '''
    For an input dictionary, sorts the most frequent keys based off their number of occurances
    returns a list of tuples of each word and its number of appearences in the dictionary
    '''
    # print(input_dict)
    frequent_words = []
    words = list(input_dict.items()) # .items() returns a list of tuples'

    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
        frequent_words.append(words[i])
    return frequent_words

def get_uniques(words):
    '''
    For an input list of words,
    returns dictionary of unique pairs of adjacent words separated by spaces
    and their relative number of occurances
    '''
    unique_pairs_dict= {}
    for word in range(len(words)):
        try:
            word_pair = words[word] + ' ' + words[word + 1]
            # print(word_pair)
            if word_pair not in unique_pairs_dict:
                unique_pairs_dict.update({word_pair:1})
            elif word_pair in unique_pairs_dict:
                unique_pairs_dict[word_pair] += 1
        except IndexError:
            return unique_pairs_dict

def check_input(input_word):
    '''
    Takes an input word, and checks it against the words word_list
    outputs the input word and each word that follows the input and the number
    of times that occurance happens in a dictionary
    '''
    words = get_words()
    word_matches_dict = {}
    for word in range(len(words)):
        try:
            if words[word] == input_word:
                word_match = words[word] + ' ' + words[word+1]
                if (word_match) not in word_matches_dict:
                    word_matches_dict.update({word_match:1})
                elif (word_match) in word_matches_dict:
                    word_matches_dict[word_match] += 1
        except IndexError:
            print('outside index')
            return word_matches_dict
    return word_matches_dict

words = get_words()
word_dict = get_words_dict(words)
unique_pairs_dict = get_uniques(words)
frequent_words = get_frequent(word_dict)
frequent_uniques = get_frequent(unique_pairs_dict)
user_input = input('\n Input a word, result will show the words that most frequently follow \n >> ')
user_input_matches = check_input(user_input)
frequent_input = get_frequent(user_input_matches)
print(frequent_input)
