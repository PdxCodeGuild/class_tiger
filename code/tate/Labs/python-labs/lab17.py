'''
Lab 17 : Palindrome and anagram checker

'''
import string

def test_palindrome(input_string):
    if input_string == input_string[::-1]:
        return f'\n{input_string} is a Palindrome\n'
    else:
        return f'\n{input_string} is not a Palindrome\n'

def string_clean(my_string):
    my_string = my_string.replace(' ','')

    for punctuation in (string.punctuation):
        my_string = my_string.replace(punctuation,'')

    list_my_string = list(my_string.lower())
    list_my_string.sort()
    return list_my_string

def anagram_checker(input_string1,input_string2):
    string1 = string_clean(input_string1)
    string2 = string_clean(input_string2)

    if string1 == string2:
        return ("\nThe strings you entered are anagrams!\n")
    else:
        return ("\nThe strings you entered are not anagrams!\n")

while True:
    print('What would you like to do?')
    user_choice = input('Type; \'Check Palindrome\', \'Check Anagram\', or \'Exit\' > ')

    if user_choice.lower() == 'exit':
        print('\nGoodbye! \n',)
        break
    elif user_choice.lower() == 'check palindrome':
        input_string = input('Enter the string you would like to check > ')
        print(test_palindrome(input_string))
    elif user_choice.lower() == 'check anagram':
        input_string1 = input('Enter first string > ')
        input_string2 = input('Enter second string > ')
        print(anagram_checker(input_string1,input_string2))
    else:
        print('Invalid input, try again')
        continue
