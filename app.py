from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO, emit
from gomoku import Gomoku

app = Flask(__name__)
socketio = SocketIO(app)

game = Gomoku()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set_size', methods=['POST'])
def set_size():
    data = request.json
    size = data['size']
    global game
    game = Gomoku(size)
    response = {'board': game.board, 'message': None}
    socketio.emit('update', response)
    return jsonify(response)

@app.route('/move', methods=['POST'])
def move():
    data = request.json
    x, y = data['x'], data['y']
    result = game.make_move(x, y)
    if result:
        response = {'board': game.board, 'message': result}
        game.reset_board()
    else:
        response = {'board': game.board, 'message': None}
    socketio.emit('update', response)
    return jsonify(response)

@socketio.on('connect')
def handle_connect():
    emit('update', {'board': game.board, 'message': None})

if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port=5001, debug=False)

