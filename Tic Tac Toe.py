import random

def display_board(board):
    print("\n")
    print(" Olympic Tic-Tac-Toe Stadium:")
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print("---|---|---")
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print("---|---|---")
    print(f' {board[6]} | {board[7]} | {board[8]} ')
    print("\n")

def goldchecker(board, contender):
    podium_spots = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]
    for wombocombo in podium_spots:
        if all(board[spot] == contender for spot in wombocombo):
            return True
    return False

def capacitychecker(board):
    return all(spot != ' ' for spot in board)


def athlete_move(board):
    while True:
        try:
            move = int(input("Choose your position on the board (1-9): ")) - 1
            if 0 <= move < 9 and board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("Sorry mate! That spot's already taken by HAL")
        except ValueError:
            print("Sorry mate! That spot's out of bounds")

def hal_move(board):

    empty_spots = [i for i in range(9) if board[i] == ' ']
    move = random.choice(empty_spots)
    board[move] = 'O'
    print("HAL moved")


def olympic_tic_tac_toe():
    board = [' '] * 9
    print("Welcome to the Olympic Tic-Tac-Toe event!")
    display_board(board)

    while True:
        athlete_move(board)
        display_board(board)
        if goldchecker(board, 'X'):
            print("Congrats! You've secured the gold medal! Full disclosure, the champage was already on ice")
            break
        if capacitychecker(board):
            print("It's a tie! Both athletes have aggreed to share the podium.")
            break

        hal_move(board)
        display_board(board)
        if goldchecker(board, 'O'):
            print("HAL 9000 has won the gold! Humanity goes home devastated.")
            break
        if capacitychecker(board):
            print("It's a tie! Both athletes have aggreed to share the podium.")
            break

if __name__ == "__main__":
    olympic_tic_tac_toe()
