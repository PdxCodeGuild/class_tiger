#Write a function check_palindrome which takes a string,
# and returns True if the string's a palindrome,
# or False if it's not.
def check_palindrome():
    Word_prompt = input(f'Enter a word ')
    if Word_prompt == Word_prompt[::-1]:
        print(f'{Word_prompt} is a palindrome')
    else:
        print(f'{Word_prompt} is not a palindrome')

check_palindrome()

#Anagram

def check_anagram():
    Word_prompt = input(f'Enter a word ')
    sentence_prompt = input(f'enter the second word ')
    #1Convert each word to lower case (lower)
    Word2 = ''
    Word1 =''
    for i in Word_prompt,sentence_prompt:
        Word1 = Word_prompt.lower()
        Word2 = sentence_prompt.lower()
    for i in Word_prompt,sentence_prompt:
        Word1 = Word1.replace(" ", "")
        Word2 = Word2.replace(" ", "")
    for i in Word_prompt,sentence_prompt:
        Word1 = sorted(Word1)
        Word2 = sorted(Word2)
    if Word1 == Word2 :
        print(f'{Word_prompt} and {sentence_prompt} are anagrams')
    else:
        print(f'{Word_prompt} and {sentence_prompt} are not anagrams')

check_anagram()