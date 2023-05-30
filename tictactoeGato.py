# Tic-Tac-Toe

# Create an empty game board
board = [[' ' for _ in range(3)] for _ in range(3)]

# Function to display the game board
def display_board():
    for row in board:
        print('|', end='')
        for cell in row:
            print(cell, end='|')
        print('\n---------')

# Function to check if a player has won
def check_win(player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player or \
       board[0][2] == board[1][1] == board[2][0] == player:
        return True
    
    return False

# Function to play the game
def play_game():
    current_player = 'X'
    game_over = False
    
    while not game_over:
        display_board()
        print("Player", current_player, "turn")
        
        # Get the player's move
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))
        
        # Update the game board with the player's move
        if board[row][col] == ' ':
            board[row][col] = current_player
        else:
            print("Invalid move. Try again.")
            continue
        
        # Check if the current player has won
        if check_win(current_player):
            display_board()
            print("Player", current_player, "wins!")
            game_over = True
            break
        
        # Check if it's a tie (board is full)
        if all(cell != ' ' for row in board for cell in row):
            display_board()
            print("It's a tie!")
            game_over = True
            break
        
        # Switch to the other player
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
play_game()