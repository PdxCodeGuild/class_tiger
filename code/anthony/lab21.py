import string

def main():
    filename = "./text_files/buster_bears_twins.txt"
    
    user_input = input("Enter a word to be searched: ")
    
    words = import_text(filename)
    
    words = remove_punctuation(words)
    
    words = make_lower(words)
    
    user_word = find_words(words, user_input)
    double_words = make_double_dict(words)
    words = make_dict(words)
    
    user_word = sort_dict(user_word)
    double_words = sort_dict(double_words)
    words = sort_dict(words)
    print("----------------------------")
    print(f"\n {filename[13:len(filename)-4]} \n")
    print("----------------------------")
    print("Most common used words:")
    print_results(words)
    print("----------------------------")
    print("Most common used word pairs: ")
    print_results(double_words)
    if len(user_word) > 0:
        print("----------------------------")
        print(f"Most common words to follow {user_input}: ")
        print_results(user_word)
    else:
        print("----------------------------")
        print("The word entered did not exist.")


def import_text(filename):
    '''
    Imports text from a file into a string
    '''
    text_string = str()
    with open(filename, 'r') as f:
        for char in f:
            text_string += char
    return text_string

def remove_punctuation(text):
    '''
    Removes punctuation from string with the exception of '
    '''
    punctuation = r"""!"#$%&()*+,-./:;<=>?@[\]^_`{|}~"""
    translator = str.maketrans('', '', punctuation)
    text = text.translate(translator)
    return text

def make_lower(text):
    '''
    Converts string to all lowercase characters
    '''
    translator = str.maketrans(string.ascii_uppercase, string.ascii_lowercase)
    text = text.translate(translator)
    return text

def make_dict(text):
    '''
    Takes string as input then converts to a dictionary. 
    During the conversion process counts number of times same words are added.
    '''
    text_dict = {}
    text = text.split()
    for word in text:
        if word not in text_dict:
            text_dict[word] = 1
        else:
            text_dict[word] += 1
    return text_dict

def make_double_dict(text):
    '''
    Makes a dictionary of pairs of words and counts them.
    '''
    double_dict = {}
    text = text.split()
    for i in range(len(text)-1):
        temp_string = str(text[i]) + " " + str(text[i+1])
        if temp_string not in double_dict:
            double_dict[temp_string] = 1
        else:
            double_dict[temp_string] += 1
    return double_dict

def sort_dict(text):
    '''
    Sorts dictionary into decending order
    '''
    word_list = list(text.items())
    word_list.sort(key=lambda tup: tup[1], reverse = True)
    return word_list

def print_results(text):
    counter = 0
    stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
   
    for i in range(len(text)):
        if text[i][0] not in stop_words:
            print(text[i][0], text[i][1])
            counter += 1
        if counter >= 10:
            break

def find_words(text, user_input):
    new_dict = {}
    text = text.split()
    for i in range(len(text)-1):
        if text[i] == user_input:
            temp_string = str(text[i]) + " " + str(text[i+1])
            if temp_string not in new_dict:
                new_dict[temp_string] = 1
            else:
                new_dict[temp_string] += 1
    return new_dict

main()