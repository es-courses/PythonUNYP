
def display_board(board):
    for r in range(0, 3):
        for c in range(0, 3): 
            print(board[r][c], end=' ')
        print()

# Initialization

board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

current_user = 'X'

# LOOP 
while True:
    display_board(board)

    print(f"{current_user} plays")
    row = int(input("Row: "))
    col = int(input("Col: "))

    # Check if row cok in valid range
    if row > 0 and row < 4 and col > 0 and col < 4:
        # Check if cell is empty
        if board[row-1][col-1] == '-':
            board[row-1][col-1] = current_user

            if current_user == 'X':
                current_user = 'O'
            else:
                current_user = 'X'

            # CHECK FOR WINNER

            # CHECK FOR TIE
            
        else:
            print(f"Cell at {row}:{col} is not available")
    else:
        print(f"Invalid row/col")
    