import random

# imported random for use in ai to generate random number


# chose list as matrix because tic tac toe needs a 3x3 matrix     - - -
# we have a counter called turn to decide who's turn is it        - - -
# to play                                                         - - -
# we have result to show winner of the game or DRAW
# status of the game is for seeing if game has ended or no

class TicTacToe:
    def __init__(self):
        self.matrix = []
        self.turn = 0
        self.result = ""
        self.status = True
        self.initialization()

    # this method initiate list of list which will be matrix as our base data structure
    def initialization(self):
        for i in range(3):
            self.matrix.append([])
            for j in range(3):
                self.matrix[i].append("-")

    # check to see who's turn it is base on our turn
    def playerTurn(self):
        if self.turn % 2 == 0:
            return "X"
        else:
            return "O"
    # check position sent by player to see if its a base on matrix , is correct index , and if no player marked that position

    def positionValidator(self,position):
      if(len(position) != 2 ):
        print("\n there need 2 be 2 number seperated by space \n")
        return False

      row = int(position[0])
      col = int(position[1])
      if(row < 0 or row > 2 or col < 0 or col > 2  ):
        print("\n the numbers need to be [0,2] \n")
        return False
      elif (self.matrix[row][col] != "-") :
        print("\n this position already been marked \n")
        return False
      else:
        return True    
        
    # base method of the game which checks first if there is ANY ROW which all cols are base on the player
    # diagonal check diagonal primary and secondary
    # third condition will check if there is ANY column rows have certain value | | |
    def isWon(self,player):

      firstCondition = any ( (all(col == player for col in rows)) == True for rows in self.matrix  )

      primaryDiagonal = [ self.matrix[i][i] for i in range(len(self.matrix)) ]
      secondaryDiagonal = [self.matrix[i][len(self.matrix[i]) - 1 - i] for i in range(len(self.matrix)) ]


      secondCondition = all( value == player for value in primaryDiagonal ) or all(value == player  for value in secondaryDiagonal)


      thirdCondition = any ( all( self.matrix[row][col] == player for row in range(len(self.matrix))  )  for col in range(len(self.matrix))  )
    # -first sol for row check -    
      return firstCondition or secondCondition or thirdCondition
              
    # draw check if all of row and cols are anything else rather than "-" (which we defiend as empty for ourselves)
    def isDraw(self):
      return all( all( self.matrix[row][col] != "-" for col in range(len(self.matrix)) )  for row in range(len(self.matrix))  )


    # the method for ai to play base on conditions to be smart
    def aiPlay(self):

        # Check for AI's winning move
        for i in range(3):
            for j in range(3):
                if self.matrix[i][j] == "-":
                    self.matrix[i][j] = "O"
                    if self.isWon("O"):
                        self.matrix[i][j] = "-"
                        return [str(i), str(j)]
                    self.matrix[i][j] = "-"


        # Check if AI can block
        for i in range(3):
            for j in range(3):
                if self.matrix[i][j] == "-":
                    self.matrix[i][j] = "X"
                    if self.isWon("X"):
                        self.matrix[i][j] = "-"
                        return [str(i), str(j)]
                    self.matrix[i][j] = "-"

        # Take center
        if self.matrix[1][1] == "-":
            return ["1", "1"]

        # Take a corner
        corners = [[0, 0], [0, 2], [2, 0], [2, 2]]
        available_corners = [corner for corner in corners if self.matrix[corner[0]][corner[1]] == "-"]
        if available_corners:
            move = random.choice(available_corners)
            return [str(move[0]), str(move[1])]

        # chose random position
        number1 = random.randint(0, 2)
        number2 = random.randint(0, 2)

        while self.matrix[number1][number2] != "-":
            number1 = random.randint(0, 2)
            number2 = random.randint(0, 2)

        return [str(number1), str(number2)]







