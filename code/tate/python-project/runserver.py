from flask import Flask, request, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hellosecrets'
socketio = SocketIO(app)

@app.route('/')
def session():
    return render_template('chatroom.html')

def messageReceived(methods=['GET','POST']):
    print('message received')

@socketio.on('my event')
def handle_my_custom_event(json,methods =['GET','POST']):
    print('recieved my event: ' + str(json))
    socketio.emit('my response',json,callback=messageReceived)

def just_message(methods=['POST']):
    print('\n\n\nPOST MESSAGE')
# Ideas for making it my own.
    # Allow user to change colors
    # Add a log page to view the history somehow...

if __name__ == '__main__':
    socketio.run(app, debug = True)
