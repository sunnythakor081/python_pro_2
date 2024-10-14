# Tic-Tac-Toe game using Python

# Function to print the board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)


def check_win(board, player):

    for row in board:
        if all([spot == player for spot in row]):
            return True
    
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    
    return False

# Function to check if the board is full
def check_full(board):
    return all([spot != " " for row in board for spot in row])

# Main function to run the game
def play_tic_tac_toe():
    # Initialize the board
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0
    
    # Game loop
    while True:
        print_board(board)
        player = players[turn % 2]
        print(f"Player {player}'s turn")
        
        # Get the player's move
        try:
            row, col = map(int, input("Enter row and column (0, 1, or 2): ").split())
            if board[row][col] != " ":
                print("That spot is already taken!")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Please enter two numbers between 0 and 2.")
            continue
        
        # Place the player's symbol on the board
        board[row][col] = player
        
        # Check for a win
        if check_win(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        
        # Check for a draw
        if check_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch turns
        turn += 1

# Run the game
if __name__ == "__main__":
    play_tic_tac_toe()
