import random

Rows = 6 # These are the dimensions of the board in the CLi
Columns = 7

def inception(): # we need to instigate a board with the empty spaces 
    board = []
    for _ in range(Rows):
        row = []
        for _ in range(Columns):
            row.append(' ') # referenced empty space coded here
        board.append(row)
    return board

def display(board): # now we're displaying the board in an intuitive way

    for r, row in enumerate(board):
        print(f"Row {r+1}: " + ' | '.join(row))
        print('-' * (4 * Columns - 1))
    print("   " + "   ".join(str(i) for i in range(1, Columns + 1))) 

def validitychecker(board, col): # we want to confirm a column's valid by checking whether it's full
    if col < 0 or col >= Columns:
        return False
    return board[0][col] == ' '

def lrow(board, col): 
    r = Rows - 1
    while r >= 0:
        if board[r][col] == ' ':
            return r
        r -= 1

def dtp(board, row, col, piece): #this will drop the piece in
    board[row][col] = piece

def valuingacombo(combo, piece): # calculates a score for a series of pieces 
 
    score = 0
    opp_piece = 'X' if piece == 'O' else 'O'
    
    if combo.count(piece) == 4:
        score += 110  # win scenario
    elif combo.count(piece) == 3 and combo.count(' ') == 1:
        score += 4  # possible win scenario
    elif combo.count(piece) == 2 and combo.count(' ') == 2:
        score += 1  # average move
    
    if combo.count(opp_piece) == 3 and combo.count(' ') == 1:
        score -= 5  # strategic block of opponent's move

    return score

def valuingaposition(board, piece): # calculate score of a position given the population of a board

    score = 0

    center_array = [board[r][Columns // 2] for r in range(Rows)] #need to incentive the center of the board for the AI given the strategic edge
    center_count = center_array.count(piece)
    score += center_count * 2  # Center column preference

    # horizontal combos
    for r in range(Rows):
        row_array = [board[r][c] for c in range(Columns)]
        for c in range(Columns - 3):
            combo = row_array[c:c+4]
            score += valuingacombo(combo, piece)

    # vertical combos
    for c in range(Columns):
        col_array = [board[r][c] for r in range(Rows)]
        for r in range(Rows - 3):
            combo = col_array[r:r+4]
            score += valuingacombo(combo, piece)

    # positive diagonal combos
    for r in range(Rows - 3):
        for c in range(Columns - 3):
            combo = [board[r+i][c+i] for i in range(4)]
            score += valuingacombo(combo, piece)

    # negative diagonal combos
    for r in range(Rows - 3):
        for c in range(Columns - 3):
            combo = [board[r+3-i][c+i] for i in range(4)]
            score += valuingacombo(combo, piece)

    return score

def movemaker(board, piece): #selects the best move 

    valid_locations = [c for c in range(Columns) if validitychecker(board, c)]
    best_score = -float('inf')
    best_col = random.choice(valid_locations)

    for col in valid_locations: #determines best score by using previous functions and then inputs it
        row = lrow(board, col)
        temp_board = [r[:] for r in board] 
        dtp(temp_board, row, col, piece)
        score = valuingaposition(temp_board, piece)
        if score > best_score:
            best_score = score
            best_col = col

    return best_col

def check_win_move_exists(board, piece): #checks all 'combos' for a win scenario

    for r in range(Rows):
        for c in range(Columns):
            if r < Rows - 3 and c < Columns - 3:
                if all(board[r+i][c+i] == piece for i in range(4)):
                    return True
            if r >= 3 and c < Columns - 3:
                if all(board[r-i][c+i] == piece for i in range(4)):
                    return True
            if c < Columns - 3:
                if all(board[r][c+i] == piece for i in range(4)):
                    return True
            if r < Rows - 3:
                if all(board[r+i][c] == piece for i in range(4)):
                    return True
    return False

def genesis(): # actually runs the game

    board = inception()  
    display(board)
    game_over = False
    turn = random.randint(0, 1)  # randomizes who starts due to its inherent advantage

    while not game_over:
        if turn == 0:
            col = int(input("Player 1, choose your column (1-7): ")) - 1
            piece = 'X'
        else:
            col = movemaker(board, 'O')
            print(f"Computer selects column {col + 1}")
            piece = 'O'

        if validitychecker(board, col):
            row = lrow(board, col)
            dtp(board, row, col, piece)

            if check_win_move_exists(board, piece):
                display(board)
                print(f"Player {turn + 1} wins!")
                game_over = True
            else:
                display(board)
                turn = (turn + 1) % 2
        else:
            print("Column is full. Try again.")

if __name__ == "__main__":
    genesis()
