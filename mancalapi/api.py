from flask import Flask, request, jsonify
import random
import time
from mancalai.agents import GameState, MinimaxAgent, AlphaBetaAgent,ExpectiMax

app = Flask(__name__)

minimax = MinimaxAgent()
alphabeta = AlphaBetaAgent()
expectimax = ExpectiMax()

DELAY = 1.5

@app.route('/next_state', methods=['POST'])
def next_state():
    data = request.json
    board = data['game_state']['board']
    turn = data['game_state']['turn']
    game = GameState(board, turn)
  
    action = data['action']

    if action not in game.getLegalActions():
        return jsonify({'error': 'Illegal move'}), 400

    next_game = game.generateSuccessor(action)

    return jsonify({
        'board': next_game.board,
        'turn': next_game.turn
    })

@app.route('/minimax_action', methods=['POST'])
def minimax_action():
    data = request.json
    board = data['board']
    turn = data['turn']
    game = GameState(board, turn)

    time.sleep(DELAY)

    legal_moves = game.getLegalActions()
    if not legal_moves:
        return jsonify({'error': 'No legal moves'}), 400

    action = minimax.getAction(game, data['depth'])

    return jsonify({
        'action': action
    })


@app.route('/expectimax_action', methods=['POST'])
def expectimax_action():
    data = request.json
    board = data['board']
    turn = data['turn']
    game = GameState(board, turn)

    time.sleep(DELAY)

    legal_moves = game.getLegalActions()
    if not legal_moves:
        return jsonify({'error': 'No legal moves'}), 400

    action = expectimax.getAction(game, data['depth'])

    return jsonify({
        'action': action
    })

@app.route('/alphabeta_action', methods=['POST'])
def alphabeta_action():
    data = request.json
    board = data['board']
    turn = data['turn']
    game = GameState(board, turn)

    time.sleep(DELAY)

    legal_moves = game.getLegalActions()
    if not legal_moves:
        return jsonify({'error': 'No legal moves'}), 400

    action = alphabeta.getAction(game, data['depth'])

    return jsonify({
        'action': action
    })

@app.route('/minimax_half_action', methods=['POST'])
def minimax_half_action():
    data = request.json
    board = data['board']
    turn = data['turn']
    game = GameState(board, turn)

    time.sleep(DELAY)
    
    legal_moves = game.getLegalActions()
    if not legal_moves:
        return jsonify({'error': 'No legal moves'}), 400

    if random.random() < .5:
          action = minimax.getAction(game, data['depth'])
    else:
        action = random.choice(game.getLegalActions())

    return jsonify({
        'action': action
    })


if __name__ == '__main__':
    app.run(debug=True)