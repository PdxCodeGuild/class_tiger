from flask import Flask, request, render_template
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hellosecrets'
socketio = SocketIO(app)

@app.route('/')
def display_index():
    return render_template('index.html')

@app.route('/my-chatroom')
def my_chatroom():
    print("\n\n\nUser in chatroom")
    # action_counter += 1
    with open('templates/my-chatroom.html','a') as f:
        f.write('<p style="position:absolute;top:10px;left:70%;">User actions: ' + str(action_counter) +  '</p>')
    return render_template('my-chatroom.html')

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
    action_counter = 0
    socketio.run(app, debug = True)
