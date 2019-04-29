''' Updates the my-chatroom.html '''
from runserver import clear_conversation
from selenium import webdriver
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
            comment_dict = {'User':self.user_name,'Content':user_comment.comment,'Time':user_comment.time}
            with open('templates/my-chatroom.html','a') as f:
                f.write(str(user_comment))
            update_comment_log(comment_dict)
        return user_comment

    def change_color(self):
        self.user_color = input('What would you like to change your color to? > ').lower()
        return self.user_color

def view_history():
    with open('comment-log.json','r') as f:
        comment_log = json.load(f)
    return comment_log

def login():
    pass

def update_chatroom():
    os.system('git pull')
    os.system('git add .')
    os.system('git commit -m "update from chatroom"')
    os.system('git push')

def update_comment_log(user_comment):
    ''' takes a Comment as input. Loads the current comment-log.json
        and appends the new comment to the list of comments, then
        writes the updated list of dictionaries to the .json
    '''
    with open('comment-log.json','r') as f:
        comment_log = json.load(f)
    comment_log.append(user_comment)
    with open('comment-log.json','w') as f:
        json.dump(comment_log,f)

def create_user():
    user_name = input('Hi, what is your name? > ')
    user_color = input('What is your favorite color? > ').lower()
    user = User(user_color,user_name)
    return user

def input_user_choice():
    print('What would you like to do? ')
    valid_choices = ['comment','change color','view history','clear conversation','update chatroom','refresh', 'quit']
    print('Choose:\n - ' + '\n - '.join(valid_choices) + '\n')
    user_choice = input(' > ').lower()
    while user_choice not in valid_choices:
        print('Invalid Input')
        print('Choose:\n - ' + '\n - '.join(valid_choices) + '\n')
        user_choice = input(' > ').lower()
    return user_choice

def main():
    print('Welcome ' + user.user_name)
    print(input('Press return to continue'))
    driver = webdriver.Chrome(executable_path='./chromedriver')
    driver.get("http://0.0.0.0:5000/my-chatroom")
    while True:
        os.system('clear')
        user_choice = input_user_choice()
        if user_choice == 'quit':
            print('Goodbye!')
            break
        elif user_choice == 'comment':
            user_choice = user.add_comment()
            # time.sleep(3)
            # driver.refresh()
            if user_choice == 'go back':
                continue
        elif user_choice == 'refresh':
            driver.refresh()
        elif user_choice == 'change color':
            user.change_color()
        elif user_choice == 'clear conversation':
            clear_conversation()
        elif user_choice == 'view history':
            print(view_history())
            print(input('Press return to continue'))
        elif user_choice == 'update chatroom':
            print('This will pull and push changes to github, are you sure you want to do this?')
            user_choice = input(' (y/n) > ').lower()
            if user_choice == 'y':
                print('Updating chatroom...')
                update_chatroom()
            else:
                print('Chatroom was not updated')
                print(input('Press return to continue'))


user = create_user()
main()

# payload = ()
# r = requests.post('http://0.0.0.0:8000/',data=payload)
# r = requests.post('http://0.0.0.0:5000/old-chatroom.html',data=user_input)
