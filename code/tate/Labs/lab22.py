'''
Lab 22: Compute Automated Readability Index

Formula : 4.71 * (characters/words) + 0.5 * ( words / sentences ) - 21.43

'''
import string
import math

my_file = 'jungle-book.txt'

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

def read_file():
    with open(my_file,'r') as f:
        contents = f.read()
    return contents

def remove_punc(my_s):
    translator_remove_punc = str.maketrans('','',string.punctuation)
    my_s = my_s.translate(translator_remove_punc)
    return my_s

def remove_spaces(my_s):
    translator_remove_spaces = str.maketrans('','',' ')
    my_s = my_s.translate(translator_remove_spaces)
    return my_s

def remove_newlines(my_s):
    translator_remove_newlines = str.maketrans('','','\n')
    my_s = my_s.translate(translator_remove_newlines)
    return my_s

def get_characters():
    #function for getting the characters from the gettysburg-address.txt
    contents = read_file()
    contents = remove_punc(contents)
    contents = remove_spaces(contents)
    contents = remove_newlines(contents)
    contents_list = list(contents)
    character_count = len(contents_list)
    return character_count

def get_words():
    #function for getting the words from the gettysburg-address.txt
    contents = read_file()
    contents = remove_punc(contents)
    replace_newlines = str.maketrans('\n',' ')
    contents = contents.translate(replace_newlines)
    contents_list = contents.split(' ')
    contents_list = [x for x in contents_list if x != '']
    return len(contents_list)

def get_sentences():
    contents = read_file()
    contents = remove_newlines(contents)
    contents = contents.replace('. . .','')
    contents = contents.replace('...','')
    contents = contents.replace('?','.')
    contents = contents.replace('!','.')
    contents_list = contents.split('.')
    contents_list = [x for x in contents_list if x != '']
    contents_list = [x for x in contents_list if x != ' ']
    return len(contents_list)

sentences = get_sentences()
characters = get_characters()
words = get_words()

ari = 4.71 * (characters/words) + 0.5 * ( words / sentences ) - 21.43
ari = math.ceil(ari)
grade_level = ari_scale[ari]['grade_level']
ages = ari_scale[ari]['ages']
print(f'The ARI for {my_file} is {ari}\nThis corresponds to a {grade_level} level of difficulty\nthat is suitable for an average person of {ages}')
