
import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("375x365")
        self.root.configure(bg='#8B4513')  # Wooden color background
        self.board = [' ' for _ in range(9)]  # 3x3 board
        self.current_player = 'X'
        self.buttons = [None] * 9
        self.create_buttons()

    def create_buttons(self):
        for i in range(9):
            self.buttons[i] = tk.Button(
                self.root, text=' ', font='Arial 24', width=5, height=2,
                bg='#D2691E', fg='white', activebackground='#CD853F',
                relief='raised', bd=5, command=lambda i=i: self.make_move(i)
            )
            self.buttons[i].grid(row=i // 3, column=i % 3, padx=5, pady=5)

    def make_move(self, index):
        if self.board[index] == ' ':
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player, fg='black')
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif ' ' not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontal
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertical
            (0, 4, 8), (2, 4, 6)               # diagonal
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return True
        return False

    def reset_game(self):
        self.board = [' ' for _ in range(9)]
        for button in self.buttons:
            button.config(text=' ', fg='white')
        self.current_player = 'X'

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
