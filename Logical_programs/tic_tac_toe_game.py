import random
#  Cross Game or Tic-Tac-Toe Game  
# Write a Program to play a Cross Game or Tic-Tac-Toe Game. Player 1 
# is the Computer and the Player 2 is the user. Player 1 take Random Cell that is 
# the Column and Row.  

board = [["","",""],["","",""],["","",""]]

def cell_available(row, col,board, player):
    if player == "X":
        player = "O"
    else:
        player = "X"

    if(board[row][col] != "" and board[row][col] == player):
        return False
    return True

def show_board(board):
    for i in range(0,3):
        for j in range(0,3):
            print(board[i][j],end = "")
            if(j<2):
                print(end=" | ")
        print()
    print("------------------------------------")

def board_full(board):
    for i in range(0,3):
        for j in range(0,3):
            if(board[i][j] == ""):
                return False
    return True

def check_win(board, player):
    #check row
    for i in range(0,3):
        if(board[i][0] == player and board[i][1]==player and board[i][2] == player):
            return True
    
    #check coloumn
    for j in range(0,3):
        if(board[0][j] == player and board[1][j]==player and board[0][j] == player):
            return True
    
    #check diagonal
    if(board[0][0]==player and board[1][1]==player and board[2][2]==player):
        return True

    if(board[0][2]==player and board[1][1]==player and board[2][0]==player):
        return True
    
    return False


player = "X"
game_won = False

#computer use "X"
#user use "O"

while(not game_won):
    if(player == "X"or player == "x"):
        print("Computer's turn ----")
        row = random.randint(0,2)
        col = random.randint(0,2)
        if(board_full(board)):
            print("It's a draw!!")
        else:
            while(not cell_available(row,col,board,player)):
                row = random.randint(0,2)
                col = random.randint(0,2)
            board[row][col] = player
            show_board(board)
            if(check_win(board,player)):
                print("Computer won!!")
                game_won = True # or we can simply break the loop 
            else:
                player = "O"
    else:
        print("User's turn ----")
        user_row = int(input("Enter a row: "))
        user_col = int(input("Enter a coloumn: "))
        if(board_full(board)):
            print("It's a draw!!")
        else:
            while(not cell_available(user_row,user_col,board,player)):
                print("---- Enter a valid cell ----")
                user_row = int(input("Enter a row: "))
                user_col = int(input("Enter a coloumn: "))
            board[user_row][user_col] = player
            show_board(board)
            if(check_win(board,player)):
                print("User won!!")
                game_won = True # or break the loop by break statement
            else:
                player = "X"


