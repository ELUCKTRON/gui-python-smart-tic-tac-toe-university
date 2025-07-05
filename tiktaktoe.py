import random

# imported random for use in ai to generate random number


# chose list as matrix because tic tac toe needs a 3x3 matrix     - - -
# we have a counter called turn to decide who's turn is it        - - -
# to play                                                         - - -
# we have result to show winner of the game or DRAW
# status of the game is for seeing if game has ended or no

matrix = []
turn = 0
result = ""
status = True


# this method initiate list of list which will be matrix as our base data structure

def initialazation():
  for i in range(3):
    matrix.append([])
    for j in range(3):
      matrix[i].append("-")


# this will create our ui in every call
def ui():
  print(" \n turn : ",turn," | status : ",("running" if status else "finished and winner is "),result)
  print("  0 1 2")

  for i in range(len(matrix)):
    print(i, *matrix[i])

    # *matrix[i]  unpacking operator of python

  # for row in matrix:
  #   for column in row:
  #     print(column,end=" ")
  #   print()


# check to see who's turn it is base on our turn
def playerTurn():
  return ("X" if turn % 2 == 0 else "O")


# check position sent by player to see if its a base on matrix , is correct index , and if no player marked that position

def positionValidator(position):
  if(len(position) != 2 ):
    print("\n there need 2 be 2 number seperated by space \n")
    return False

  row = int(position[0])
  col = int(position[1])
  if(row < 0 or row > 2 or col < 0 or col > 2  ):
    print("\n the numbers need to be [0,2] \n")
    return False
  elif (matrix[row][col] != "-") :
    print("\n this position already been marked \n")
    return False
  else:
    return True

# base method of the game which checks first if there is ANY ROW which all cols are base on the player
# diagonal check diagonal primary and secondary
# third condition will check if there is ANY column rows have certain value | | |
def isWon(player):

  firstCondition = any ( (all(col == player for col in rows)) == True for rows in matrix  )

  primaryDiagonal = [ matrix[i][i] for i in range(len(matrix)) ]
  secondaryDiagonal = [matrix[i][len(matrix[i]) - 1 - i] for i in range(len(matrix)) ]


  secondCondition = all( value == player for value in primaryDiagonal ) or all(value == player  for value in secondaryDiagonal)


  thirdCondition = any ( all( matrix[row][col] == player for row in range(len(matrix))  )    for col in range(len(matrix))  )


  # -first sol for column check -
  # thirdCondition = False
  # for col in range(len(matrix)):
  #   if( all( (row[col]) == player for row in matrix )   ):
  #     thirdCondition = True
  #     break

  return firstCondition or secondCondition or thirdCondition

# draw check if all of row and cols are anything else rather than "-" (which we defiend as empty for ourselves)
def isDraw():
   return all( all( matrix[row][col] != "-" for col in range(len(matrix)) )  for row in range(len(matrix))  )


# the method for ai to play base on conditions to be smart
def aiPlay():

    # Check for AI's winning move
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == "-":
                matrix[i][j] = "O"
                if isWon("O"):
                    matrix[i][j] = "-"
                    return [str(i), str(j)]
                matrix[i][j] = "-"


    # Check if AI can block
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == "-":
                matrix[i][j] = "X"
                if isWon("X"):
                    matrix[i][j] = "-"
                    return [str(i), str(j)]
                matrix[i][j] = "-"

    # Take center
    if matrix[1][1] == "-":
        return ["1", "1"]

    # Take a corner
    corners = [[0, 0], [0, 2], [2, 0], [2, 2]]
    available_corners = [corner for corner in corners if matrix[corner[0]][corner[1]] == "-"]
    if available_corners:
        move = random.choice(available_corners)
        return [str(move[0]), str(move[1])]

    # chose random position
    number1 = random.randint(0, 2)
    number2 = random.randint(0, 2)

    while matrix[number1][number2] != "-":
        number1 = random.randint(0, 2)
        number2 = random.randint(0, 2)

    return [str(number1), str(number2)]


# runing method which access and change global values status turn and result
def main():
  global status
  global turn
  global result

  while status:

    try:
      ui()
      player = playerTurn()
      userInput = input(f"\n player {player} choose your row and collumn (example : 2 1) \n").strip().split(" ") if player == "X" else aiPlay()
      while not positionValidator(userInput):
        userInput = input(f" \n player {player} choose your row and collumn (example : 2 1) \n").strip().split(" ") if player == "X" else aiPlay()

      row = int(userInput[0])
      col = int(userInput[1])

      matrix[row][col] = player
      turn += 1

      if(isWon(player)):
        status = False
        result = player
        ui()
        break

      if(isDraw()):
         status = False
         result = "DRAW"
         ui()
         break

    except IndexError:
      print("\n ERROR : do not put more than 2 input only: row column \n")
    except ValueError:
      print(" \n ERROR : only input numbers \n")



# initializing the data structure and starting it
initialazation()
main()






