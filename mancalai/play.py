from agents import GameState, MinimaxAgent, AlphaBetaAgent,ExpectiMax
import random

board = {'p1':[4,4,4,4,4,4,0],'p2':[4,4,4,4,4,4,0]}
turn = 'p1'
game = GameState(board,turn)
minimax = MinimaxAgent(2)
minimax2 = MinimaxAgent(2,1)
alphabeta = AlphaBetaAgent(2)
expectimax = ExpectiMax(2)

gamechoice = int(input('Select what kind of game you want to play'
'\n 0 for human v human'
'\n 1 for human v minimax'
'\n 2 for human v alpha beta pruning'
'\n 3 for human v expectimax'
'\n 4 for human v minimax half of the time\n'
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
        action = minimax.getAction(game)

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
      action = alphabeta.getAction(game)

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
      action = expectimax.getAction(game)

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
        if random.random() < .5:
          action = minimax.getAction(game)
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
        action = minimax2.getAction(game)
      else:
        action =  expectimax.getAction(game)

      print('Player ' + game.turn + ' took ' + str(action))
      game = game.generateSuccessor(action)

    game.printBoard()
    print(game.getScore())
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\nTotal execution time: {elapsed_time:.2f} seconds")




