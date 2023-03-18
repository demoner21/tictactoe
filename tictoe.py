import tkinter as tk
import random

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic-Tac-Toe")
        self.board = [' ']*9

        self.buttons = [[tk.Button(self.master, width=8, height=4, font=('Arial', 20), command=lambda i=i, j=j: self.make_move(i, j)) for j in range(3)] for i in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].grid(row=i, column=j, padx=5, pady=5)

        self.players = random.sample(['X', 'O'], 2)
        self.current_player = self.players[0]

        self.status = tk.Label(self.master, text=f"Player {self.current_player}'s turn", font=('Arial', 14))
        self.status.grid(row=3, column=0, columnspan=3, pady=10)

    def make_move(self, row, col):
        index = row*3 + col
        if self.board[index] == ' ':
            self.buttons[row][col].config(text=self.current_player)
            self.board[index] = self.current_player
            if self.check_win(self.current_player):
                self.status.config(text=f"Player {self.current_player} wins!")
                for button_row in self.buttons:
                    for button in button_row:
                        button.config(state=tk.DISABLED)
            elif all(x != ' ' for x in self.board):
                self.status.config(text="It's a tie!")
            else:
                self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]
                self.status.config(text=f"Player {self.current_player}'s turn")

    def check_win(self, player):
        wins = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        for win in wins:
            if all(self.board[i] == player for i in win):
                return True
        return False

if __name__ == '__main__':
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
