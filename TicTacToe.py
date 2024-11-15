import random

"""
Tic Tac Toe
-The game includes two input parameters 'X' and 'O'.
-The two users input their parameters until the game is draw or someone wins
-1. Display information
-2. Take user input
-3. Validation of user input
-4. Build the game
"""

"""Step 1: Write a function that can print out a board.Set up your board as a list, where each index 1 - 9 corresponds 
with a number on a number pad, so you get a 3 by 3 board representation.
"""
def display_board(board):
    print('\n'*100)
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[7] + '|' + board[8] + '|' + board[9])

# Step 2: Choose the marker for the players
def player_input():
    """
    :return: (Player1 marker, player2 marker)
    """
    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input("Player 1, Choose X or O: ").upper()

    if marker == 'X':
        return('X','O')
    else:
        return('O','X')

"""Step 3: Write a function that takes in the board list object, # a marker ('X' or 'O'), and a desired position (number 1-9) 
 and assigns it to the board.
"""
def place_marker(board, marker, position):
    board[position] = marker

#Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won.
def win_check(board, marker):
    """
    How to decide who won in TIC TAC TOE
    IF ALL ROWS or COLUMNS or DIAGONALS share the same marker, it is a win
    """
    # All rows
    return((board[1] == board[2] == board[3] == marker) or
        (board[4] == board[5] == board[6] == marker) or
        (board[7] == board[8] == board[9] == marker) or
        (board[1] == board[4] == board[7] == marker) or
        (board[2] == board[5] == board[8] == marker) or
        (board[3] == board[6] == board[9] == marker) or
        (board[1] == board[5] == board[9] == marker) or
        (board[3] == board[5] == board[7] == marker))

""" Step 5: Write a function that uses the random module to randomly decide which player goes first. 
 You may want to lookup random.randint() Return a string of which player went first.
"""
def choose_first():

    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

# Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.
def space_check(board,position):
    return board[position] == ' '

# Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    #when board is full return true
    return True

""" Step 8: Write a function that asks for a player's next position (as a number 1-9)and then uses the function from 
step 6 to check if it's a free position. If it is, then return the position for later use.
"""
def player_choice(board):

    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input("Input your position(1-9): "))

    print("Your position is: " + str(position))
    return position

# Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.
def replay():

    choice = input("Do you want to play again? Yes/No: ").upper()
    return choice == 'YES' or choice == 'Y'

# Step 10: Run the game
print("Welcome to Tic Tac Toe")

#while loop to keep the game continued
while True:
    # Play the game

    # Set up the following parameters >> Board, 1st player, markers (X,O)
    play_board = [' ']*10
    player1_marker, player2_marker = player_input()
    print("Marker of player 1 is: "+player1_marker)
    print("Marker of player 2 is: "+player2_marker)

    turn = choose_first()
    print(turn + " will go first!")
    play = ''
    # game_on = False
    while play != 'Y' and play != 'N':
        play = input("Are you ready to play the game? Y/N").upper()

    if play == 'Y':
        game_on = True
    else:
        game_on = False

    while game_on:
    # Player 1 turn
        if turn == 'Player 1':
        # Step 1: Show the board
            display_board(play_board)
        #Step 2: Choose the position
            position = player_choice(play_board)
        #Step 3: Place marker on the position
            place_marker(play_board, player1_marker, position)
        #Step 4: Check if win?
            if win_check(play_board,player1_marker):
                display_board(play_board)
                print("*****Player 1 has won!*****")
                game_on = False
        #Step 5: Check if tie?
            else:
                if full_board_check(play_board):
                    display_board(play_board)
                    print("*****It is a tie!*****")
                    game_on = False
                else:
                # Step 6: If no win or tie? Next player's turn
                    turn = 'Player 2'


        # Player 2 turn
        else:
            display_board(play_board)
        #Step 2: Choose the position
            position = player_choice(play_board)
        #Step 3: Place marker on the position
            place_marker(play_board, player2_marker, position)
        #Step 4: Check if win?
            if win_check(play_board,player2_marker):
                display_board(play_board)
                print("*****Player 2 has won!*****")
                game_on = False
        #Step 5: Check if tie?
            else:
                if full_board_check(play_board):
                    display_board(play_board)
                    print("*****It is a tie!*****")
                    game_on = False
                else:
                # Step 6: If no win or tie? Next player's turn
                    turn = 'Player 1'

    if not replay():
        print("***END***")
        break
    #break out of while loop after replay()