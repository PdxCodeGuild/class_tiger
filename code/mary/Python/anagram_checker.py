# anagram_checker.py
import os
in_letters = input('Enter first word. >')
in_letters2 = input('Enter second word. >')
in_letters = in_letters.replace(' ','')
in_letters2 = in_letters2.replace(' ','')
print(in_letters)
print(in_letters2)
letter_list = list(in_letters.lower())
letter_list2 = list(in_letters2.lower())
letter_list.sort()
letter_list2.sort()
print(letter_list)
print(letter_list2)
if letter_list == letter_list2:
    print("Good.")
else:
    print("Try again.")


#palindrome.py
pal_word = input("Enter a word.")
pal_word = list(pal_word)
print(pal_word)
print(list(reversed(pal_word)))
if pal_word == list(reversed(pal_word)):
    print("True")
else:
    print("False")
