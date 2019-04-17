import string
import math

def main():
    # file = "./text_files/buster_bears_twins.txt"
    file = "./text_files/gettysburg_address.txt"
    ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}
    characters = get_characters(file)
    sentences = get_sentences(file)
    words = get_words(sentences)
    ari = calculate_ari(characters, words, sentences)
    print(f"The ARI for {file} is {ari}")
    print(f"This corresponds to a {ari_scale[ari]['grade_level']} Grade level of difficulty")
    print(f"that is suitable for an average person {ari_scale[ari]['ages']}")
    



def calculate_ari(characters, words, sentences):
    ari = 4.71 * (len(characters) / len(words)) + 0.5 * (len(words)/len(sentences)) - 21.43
    ari = math.ceil(ari)
    return ari


def get_characters(file):
    characters = str()
    with open(file, 'r') as f:
        for char in f.read():
            if char not in string.punctuation and char not in string.whitespace:
                characters += char
    return characters


def get_words(sentences):
    punctuation_to_remove = "',', '\'', '\"', ':'"
    words = str()
    for sentence in sentences:
        for char in sentence:
            if char not in punctuation_to_remove:
                words += char
            elif char == ' ':
                words += ' '
            else:
                words += ''
        words += ' '
    words = words.split(' ')
    return words
        
                
def get_sentences(file):
    sentences = list()
    temp_string = str()
    with open(file, 'r') as f:
        for char in f.read():
            if char == '!' or char == '! ':
                temp_string += '.'
            elif char == '?' or char == '? ':
                temp_string += '.'
            elif char == '. ':
                temp_string += '.'
            elif char == '\n' or char == '\n ':
                temp_string += ''
            else:
                temp_string += char
    sentences = temp_string.split('.')
    return sentences

main()