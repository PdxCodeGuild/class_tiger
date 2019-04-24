''' Updates the index.html '''

import requests

class User:
    def __init__(self,user_color,user_name):
        self.user_name = user_name
        self.user_color = user_color

    def __repr__(self):
        return f'User name: {self.user_name} \nFavorite Color: {self.user_color}'

user_name = input('Hi, what is your name? > ')
user_color = input('What is your favorite color? > ').lower()

user = User(user_color,user_name)

print(user)

def main():
    # payload = {user.user_name: user.user_color}
    # r = requests.post('http://0.0.0.0:8000/',data=payload)

    while True:

        user_input = input('What would you like to say? > ')
        if user_input.lower() == 'quit':
            print('Goodbye!')
            break
        user_input = f'\n<h3 style="color:{user.user_color}"> {user.user_name} says: ' + user_input + '</h3>\n'
        r = requests.post('http://0.0.0.0:5000/',data=user_input)

        # with open('templates/index.html','a') as f:
        #     f.write(user_input)

main()
