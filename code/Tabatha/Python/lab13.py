

import string

def encrypt_letters(word):
    letters = [char for char in string.ascii_lowercase]
    numbers = [x+1 for x in range(len(letters))]
    normal = dict(zip(letters, numbers))
    letters2 = [char for char in string.ascii_lowercase]
    # crypt_key = len(word) % 26
    numbers2 = [(x+13) % 26 for x in range(0,26)]
    cipher = dict(zip(numbers2, letters2))
    output = []
    for char in word:
        x = normal[char]
        y = cipher[x]
        output.append(y)
    return "".join(output)
    

print(encrypt_letters('computer'))


