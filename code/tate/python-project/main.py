''' Updates the my-chatroom.html '''

import requests
import os
import datetime
import json


class Comment:
    def __init__(self,user,comment,time):
        self.user = user
        self.comment = comment
        self.time = time

    def __repr__(self):
        return self
        # '\nuser: {0},\n comment: {1},\n time:{2}'.format(self.user.user_name,self.comment,self.time)

    def __str__(self):
        return f'\n<h3 style="color:{self.user.user_color}"> {self.user.user_name} says: ' + self.comment + '</h3>\n'

class User:
    def __init__(self,user_color,user_name):
        self.user_name = user_name
        self.user_color = user_color

    def __repr__(self):
        return f'User name: {self.user_name} \nFavorite Color: {self.user_color}'


    def add_comment(self):
        os.system('clear')
        while True:
            time = str(datetime.datetime.now())
            print('Type comments here, or type \'go back\' to go back\n')
            user_input = input('What would you like to say? > ')

            if user_input.lower() == 'go back':
                break
            user_comment = Comment(self,user_input,time)

            with open('templates/my-chatroom.html','a') as f:
                f.write(str(user_comment))
            with open('comment-log.json','a') as f:
                json.dump(user_comment,f)

        return user_comment

    def change_color(self):
        self.user_color = input('What would you like to change your color to? > ').lower()
        return self.user_color

def view_history():
    pass

def login():
    pass

def create_user():
    user_name = input('Hi, what is your name? > ')
    user_color = input('What is your favorite color? > ').lower()
    user = User(user_color,user_name)
    return user

def input_user_choice():
    print('What would you like to do? ')
    valid_choices = ['comment','change color','view history','clear conversation', 'quit']
    print('Choose:\n - ' + '\n - '.join(valid_choices) + '\n')
    user_choice = input(' > ').lower()
    while user_choice not in valid_choices:
        print('Invalid Input')
        print('Choose:\n - ' + '\n - '.join(valid_choices) + '\n')
        user_choice = input(' > ').lower()
    return user_choice

def main():
    print('Welcome ' + user.user_name)
    print(input('Press any key to continue'))

    while True:
        os.system('clear')
        user_choice = input_user_choice()

        if user_choice == 'quit':
            print('Goodbye!')
            break
        elif user_choice == 'comment':
            user_choice = user.add_comment()
            if user_choice == 'go back':
                continue
        elif user_choice == 'change color':
            user.change_color()
        elif user_choice == 'view history':
            view_history()

user = create_user()
main()

# payload = ()
# r = requests.post('http://0.0.0.0:8000/',data=payload)
# r = requests.post('http://0.0.0.0:5000/old-chatroom.html',data=user_input)
