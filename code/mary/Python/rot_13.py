#rot_13.py
import string
word_input = ''
word_input = input("Enter a word or phrase.")
abc ='abcdefghijklmnopqrstuvwxyz'

def rot_13(word_input):
    word_output = ''
    for char in word_input:
        word_output += abc[(abc.find(char)+13)%26]
    return word_output



print(rot_13(word_input))
rot_13(word_input)
