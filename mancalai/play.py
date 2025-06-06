from agents import GameState, MinimaxAgent, AlphaBetaAgent,ExpectiMax
import random

# chance of minimax agent playing for game choice 4
MINIMAX_CHANCE = 0.5

board = {'p1':[4,4,4,4,4,4,0],'p2':[4,4,4,4,4,4,0]}
turn = 'p1'
game = GameState(board,turn)
minimax = MinimaxAgent('p1')
minimax2 = MinimaxAgent('p2')
alphabeta = AlphaBetaAgent('p1')
alphabeta2 = AlphaBetaAgent('p2')
expectimax = ExpectiMax('p1')

gamechoice = int(input('Select what kind of game you want to play'
'\n 0 for human v human'
'\n 1 for human v minimax'
'\n 2 for human v alpha beta pruning'
'\n 3 for human v expectimax'
'\n 4 for human v minimax ' + str(MINIMAX_CHANCE) + ' of the time'
'\n 5 for ai v ai\n'))

if gamechoice == 0:
  while (not game.gameOver()):
    print()
    print(game.turn + "'s turn")
    game.printBoard()

    action =  input("Enter your move: ")
    action = int(action)
  

    game = game.generateSuccessor(action)

  game.printBoard()
  print(game.getScore())
elif gamechoice == 1:
    while (not game.gameOver()):
      print()
      print(game.turn + "'s turn")
      game.printBoard()
      if game.turn == 'p1':
        action =  input("Enter your move: ")
        action = int(action)
      else:
        action = minimax.getAction(game,2)

      print('Player ' + game.turn + ' took ' + str(action))
      game = game.generateSuccessor(action)

    game.printBoard()
    print(game.getScore())
elif gamechoice == 2:
  while (not game.gameOver()):
    print()
    print(game.turn + "'s turn")
    game.printBoard()
    if game.turn == 'p1':
      action =  input("Enter your move: ")
      action = int(action)
    else:
      action = alphabeta.getAction(game,3)

    print('Player ' + game.turn + ' took ' + str(action))
    game = game.generateSuccessor(action)
  game.printBoard()

  print(game.getScore())

elif gamechoice == 3:
  while (not game.gameOver()):
    print()
    print(game.turn + "'s turn")
    game.printBoard()
    if game.turn == 'p1':
      action =  input("Enter your move: ")
      action = int(action)
    else:
      action = expectimax.getAction(game,2)

    print('Player ' + game.turn + ' took ' + str(action))
    game = game.generateSuccessor(action)
  game.printBoard()

  print(game.getScore())
elif gamechoice == 4:
  while (not game.gameOver()):
      print()
      print(game.turn + "'s turn")
      game.printBoard()
      if game.turn == 'p1':
        action =  input("Enter your move: ")
        action = int(action)
      else:
        if random.random() < MINIMAX_CHANCE:
          action = minimax.getAction(game,2)
        else:
          action = random.choice(game.getLegalActions())

      print('Player ' + game.turn + ' took ' + str(action))
      game = game.generateSuccessor(action)
  game.printBoard()
  print(game.getScore())
else:
    import time

    start_time = time.time()
    while (not game.gameOver()):
      print()
      print(game.turn + "'s turn")
      game.printBoard()
      if game.turn == 'p1':
        action = alphabeta.getAction(game,2)
      else:
        action =  alphabeta2.getAction(game,2)

      print('Player ' + game.turn + ' took ' + str(action))
      game = game.generateSuccessor(action)

    game.printBoard()
    print(game.getScore())
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\nTotal execution time: {elapsed_time:.2f} seconds")




