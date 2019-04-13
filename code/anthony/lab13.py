import string
def main():
    user_string = input("Enter your string to be cyphered: ")
    while True:
        try:
            cypher = int(input("Enter the amount of encryption: "))
            break
        except:
            print("Try again")
            
    
    encrypted_string = encrypt_string(cypher, user_string)
    print(str(encrypted_string))
def encrypt_string(num, str):
    encrypted = []
    for char in str:
        while (ord(char)) + num > 122:
            num = num - 26
        encrypted.append(chr(ord(char) + num))
    return encrypted
main()