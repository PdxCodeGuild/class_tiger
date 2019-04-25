from flask import Flask, request, render_template
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hellosecrets'
socketio = SocketIO(app)
action_counter = 0

with open('templates/my-chatroom.html','w') as f:
    f.write('<h1>Welcome <hr></h1>')


@app.route('/')
def display_index():
    return render_template('index.html')

def update_counter():
    global action_counter
    action_counter += 1
    counter_string =str(action_counter)
    print('my-chatroom requests: ' + str(action_counter))
    return counter_string

def comment_log():
    pass


@app.route('/my-chatroom')
def my_chatroom():
    print("\n\n\nUser in chatroom")
    counter_string = update_counter()
    return render_template('my-chatroom.html', counter_string = counter_string)

@app.route('/log')
def info_log():
    counter_string = update_counter()
    return render_template('log.html', counter_string = counter_string)


####### Chatroom Example
@app.route('/chatroom-example')
def session():
    return render_template('chatroom.html')

def messageReceived(methods=['GET','POST']):
    print('message received')

@socketio.on('my event')
def handle_my_custom_event(json,methods =['GET','POST']):
    print('recieved my event: ' + str(json))
    socketio.emit('my response',json,callback=messageReceived)
#######

if __name__ == '__main__':
    socketio.run(app, debug = True)
