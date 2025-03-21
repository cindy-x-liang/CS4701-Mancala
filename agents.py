import copy
class GameState:
  def __init__(self,board,turn):
    #board represents the wells for each player. Inidces 0-5 represent the 
    #pits and index 6 is the mancala
    self.board = board
    self.turn = turn
  
  def start(self):
    self.board = {'p1':[4,4,4,4,4,4,0],'p2':[4,4,4,4,4,4,0]}
    self.turn = 'p1'
  
  def getLegalActions(self):
    sol = []
    for i in range(6):
      if self.board[self.turn][i] > 0:
        sol.append(i)
    return sol
  
  def generateSuccessor(self,action):
    board_copy = copy.deepcopy(self.board)
    # board_copy = {}
    # board_copy['p1'] = self.board['p1']
    # board_copy['p2'] = self.board['p2']

    stone_count = self.board[self.turn][action]
    board_copy[self.turn][action] = 0

    curr_index = action+1
    curr_side = self.turn
    while stone_count > 0:
      #placing down a stone at the current position
      board_copy[curr_side][curr_index] += 1
      stone_count -=1

       #for the capturing rule
      if stone_count == 0 and curr_index != 6 and board_copy[self.turn][curr_index] == 1 and curr_side == self.turn:
        # print('capture')
        board_copy[self.turn][6]+=1
        opp_side = 'p2' if self.turn == 'p1' else 'p1'
        board_copy[self.turn][6]+=board_copy[opp_side][5-curr_index]
        board_copy[opp_side][5-curr_index] = 0

      #generating the next position
      if curr_index == 6 and curr_side == self.turn:
        curr_index = 0
        if self.turn == 'p1':
          curr_side = 'p2'
        else:
          curr_side = 'p1'
      elif curr_index == 5 and curr_side != self.turn:
        curr_index = 0
        if self.turn == 'p1':
          curr_side = 'p1'
        else:
          curr_side = 'p2'
      else:
        curr_index +=1

        


    if curr_side != self.turn and curr_index == 0:
       return GameState(board_copy,self.turn)
    else:
       return GameState(board_copy,'p2' if self.turn == 'p1' else 'p1')

          
  #printboard function is taken by chatgpt
  def printBoard(self):
    """
    Prints the Mancala board in a readable format.
    """
    p1 = self.board['p1']
    p2 = self.board['p2']

    # Print P2's side (reversed for correct Mancala layout)
    print("\n      (0)(1)(2)(3)(4)(5)")
    print(f"P1   [ {'  '.join(map(str, p1[:6]))} ] {p1[6]}")

    # Print P1's side
    print(f"P2 {p2[6]} [ {'  '.join(map(str, p2[:6][::-1]))} ]")
    print("      (5)(4)(3)(2)(1)(0)\n")

     
  def gameOver(self):
    check = 0
    for i in range(6):
      check +=  self.board['p1'][i]
    if check == 0:
       return True
    check = 0
    for i in range(6):
      check +=  self.board['p2'][i]
    if check == 0:
       return True
    return False
  
  def getScore(self):
     return [self.board['p1'][6],self.board['p2'][6]]
  

# i dont think you will need agent index?
#check that you don't need nextAgnet index
class MinimaxAgent:
    def __init__(self,depth):
       self.depth = depth

    def getAction(self, gameState: GameState):
        
        action,score = self.max_value(gameState,self.depth * 2)
        return action
        "*** END YOUR CODE HERE ***"
    def value(self,state,depth):
        # print(depth)
        # state.printBoard()
        # print(state.turn)
        if depth == 0 or state.gameOver():
            return None,state.getScore()[1]
        if state.turn == 'p2':
            action,score = self.max_value(state,depth)
            return action,score
        else:
            action,score =  self.min_value(state,depth)
            return None,score
    def max_value(self,state,depth):
        v = float('-inf')
        actionFinal = None
        for action in state.getLegalActions():
            successor = state.generateSuccessor(action)
            a,newVal = self.value(successor,depth-1) 
            if newVal > v:
                v = newVal
                actionFinal = action
        return actionFinal,v
    

    def min_value(self,state,depth):
        v = float('inf')
        actionFinal = None
        
        for action in state.getLegalActions():
            successor= state.generateSuccessor(action)
            a,newVal = self.value(successor,depth-1 )
            if newVal < v:
                v = newVal
                actionFinal = action
        return actionFinal,v
