# rot_cipher.py
#
import string

user_input = ''
rotation_input = 0
rot_list = []
abc_list = list(string.ascii_lowercase)

def rot_encrypt(my_string, num):
    list_my_string = list(my_string)

    for letter in list_my_string:
        if letter == ' ':
            rot_list.append(' ')
            continue

        if letter in string.punctuation:
            rot_list.append(letter)
            continue

        user_indexed = int(abc_list.index(letter)) + num

        if user_indexed > 25:
            user_indexed = user_indexed % 26
        rot_list.append(abc_list[user_indexed])

    return rot_list

def rot_decrypt(my_string,num):
        rot_encrypt(my_string,26 - num)

while True:
    rot_list = []

    print('Would you like to encrypt or decrypt something? Or type \'quit\' to exit ')
    continue_choice = input('respond "encrypt" or "decrypt" : ')

    if continue_choice == 'encrypt':
        user_input = (input('What would you like to encrypt?: ').lower())
        rotation_input = int(input('With how much rotation would you like to encrypt?: '))
        rot_encrypt(user_input,rotation_input)
        print(''.join(rot_list))
        continue
    elif continue_choice == 'decrypt':
        user_input = (input('What would you like to decrypt?: ').lower())
        rotation_input = int(input('With how much rotation was this encrypted?: '))
        rot_decrypt(user_input,rotation_input)
        print(''.join(rot_list))
        continue
    elif continue_choice.lower() == 'quit':
        print('Goodbye!')
        break
    else:
        print('I\'m sorry I did not understand that, please try again')
        print('Would you like to encrypt or decrypt something? Or type \'quit\' to exit ')
        continue_choice = input('respond "encrypt" or "decrypt" : ')
        continue
