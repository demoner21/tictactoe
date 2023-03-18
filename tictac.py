import random

board = [' ' for _ in range(9)]  # Initialize the board with empty spaces

def print_board():
    print("-------------")
    for i in range(3):
        print(f"| {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} |")
        print("-------------")

def check_win(player):
    for i in range(0, 9, 3):
        if all(board[i+j] == player for j in range(3)):
            return True  # check rows
    for i in range(3):
        if all(board[i+j] == player for j in range(0, 7, 3)):
            return True  # check columns
    if all(board[i] == player for i in range(0, 9, 4)):
        return True  # check diagonal 1
    if all(board[i] == player for i in range(2, 7, 2)):
        return True  # check diagonal 2
    return False

def make_move(player):
    while True:
        move = input(f"Player {player}, make a move (1-9): ")
        if move.isdigit() and int(move) in range(1, 10) and board[int(move)-1] == ' ':
            board[int(move)-1] = player
            break
        else:
            print("Invalid move. Please try again.")
            continue

def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()
    players = ['X', 'O']
    random.shuffle(players)
    while True:
        for player in players:
            make_move(player)
            print_board()
            if check_win(player):
                print(f"Congratulations! Player {player} wins!")
                return
            if all(x != ' ' for x in board):
                print("Game over! It's a tie!")
                return

if __name__ == '__main__':
    play_game()
