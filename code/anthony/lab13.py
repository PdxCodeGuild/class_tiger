import string
def main():
    user_string = input("Enter your string to be cyphered: ")
    cypher = int(input("Enter the amount of encryption: "))
    
    encrypted_string = encrypt_string(cypher, user_string)
    print(str(encrypted_string))
def encrypt_string(num, str):
    encrypted = []
    for char in str:
        if (ord(char) + num > 122):
            encrypted.append(chr(ord(char) + (num - 26)))
        else:
            encrypted.append(chr(ord(char) + num))
    return encrypted
main()