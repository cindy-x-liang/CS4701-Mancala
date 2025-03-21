from agents import GameState, MinimaxAgent


board = {'p1':[4,4,4,4,4,4,0],'p2':[4,4,4,4,4,4,0]}
turn = 'p1'
game = GameState(board,turn)
minimax = MinimaxAgent(2)


# while (not game.gameOver()):
#   print()
#   print(game.turn + "'s turn")
#   game.printBoard()

#   action =  input("Enter your move: ")
#   action = int(action)
 

#   game = game.generateSuccessor(action)

# print(game.getScore())


#with minimax
#ai agnet is p2
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

print(game.getScore())