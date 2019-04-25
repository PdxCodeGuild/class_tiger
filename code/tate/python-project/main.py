''' Updates the index.html '''

import requests
import os

class User:
    def __init__(self,user_color,user_name):
        self.user_name = user_name
        self.user_color = user_color

    def __repr__(self):
        return f'User name: {self.user_name} \nFavorite Color: {self.user_color}'

user_name = input('Hi, what is your name? > ')
user_color = input('What is your favorite color? > ').lower()

user = User(user_color,user_name)

def add_comment():
    os.system('clear')
    print('Type comments here, or type \'go back\' to go back\n')
    user_input = input('What would you like to say? > ')
    if user_input.lower() == 'quit':
        return False
    elif user_input.lower() == 'go back':
        return True
    user_input = f'\n<h3 style="color:{user.user_color}"> {user.user_name} says: ' + user_input + '</h3>\n'

    with open('templates/my-chatroom.html','a') as f:
        f.write(user_input)

def login():
    pass

def create_user():
    pass

def view_history():
    pass

def change_color():
    user_color = input('What would you like to change your color to? > ').lower()
    return user_color

def input_user_choice():
    print('What would you like to do? ')
    print('Choose: comment, change color, view history, quit')
    user_choice = input(' > ').lower()
    valid_choices = ['comment','change color','view history','quit']
    while user_choice not in valid_choices:
        print('Invalid Input')
        print('Choose: comment, view history, quit')
        user_choice = input(' > ').lower()

    return user_choice

def main():

    print('Welcome ' + user.user_name)
    with open('templates/my-chatroom.html','w') as f:
        f.write('<h1>Welcome <hr></h1>')

    while True:
        os.system('clear')
        user_choice = input_user_choice()

        if user_choice == 'quit':
            print('Goodbye!')
            break
        elif user_choice == 'comment':
            add_comment()
            if add_comment() == False:
                print('Goodbye!')
                break
            elif add_comment() == True:
                continue
        elif user_choice == 'change color':
            user.user_color = change_color()
        elif user_choice == 'view history':
            view_history()

main()




# payload = {user.user_name: user.user_color}
# r = requests.post('http://0.0.0.0:8000/',data=payload)
# r = requests.post('http://0.0.0.0:5000/old-chatroom.html',data=user_input)
