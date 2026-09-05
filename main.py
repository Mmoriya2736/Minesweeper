import tkinter as tk
from tkinter import messagebox
import random

class Cell:
    def __init__(self):
        self.is_bomb = False
        self.is_revealed = False
        self.is_flagged = False
        self.neighbor_bombs = 0

class Board:
    def __init__(self, size, bomb_count):
        self.size = size
        self.bomb_count = bomb_count
        self.cells = [[Cell() for _ in range(size)] for _ in range(size)]
        self.place_bombs()
        self.calculate_neighbors()

    def place_bombs(self):
        bomb_positions = random.sample(range(self.size * self.size), self.bomb_count)
        for pos in bomb_positions:
            row, col = divmod(pos, self.size)
            self.cells[row][col].is_bomb = True

    def calculate_neighbors(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.cells[row][col].is_bomb:
                    continue
                count = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        nx, ny = row + dx, col + dy
                        if 0 <= nx < self.size and 0 <= ny < self.size:
                            if self.cells[nx][ny].is_bomb:
                                count += 1
                self.cells[row][col].neighbor_bombs = count

class Minesweeper:
    def __init__(self, root, size, bomb_count):
        self.root = root
        self.root.title("tk")
        self.size = size
        self.bomb_count = bomb_count
        self.board = Board(size, bomb_count)
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        for i in range(self.size):
            row_buttons = []
            for j in range(self.size):
                btn = tk.Button(self.root, width=2, height=1, bg="light gray")
                btn.config(command=self.make_left_click(i, j))
                btn.bind("<Button-3>", self.make_right_click(i, j))
                btn.grid(row=i, column=j)
                row_buttons.append(btn)
            self.buttons.append(row_buttons)

    def make_left_click(self, x, y):
        return lambda: self.reveal_cell(x, y)

    def make_right_click(self, x, y):
        return lambda event: self.toggle_flag(x, y)

    def reveal_cell(self, x, y):
        cell = self.board.cells[x][y]
        if cell.is_flagged or cell.is_revealed:
            return

        if cell.is_bomb:
            self.show_mines()
            messagebox.showinfo("Game Over", "You hit a bomb!")
            self.root.quit()
        else:
            self.reveal_recursive(x, y)
            if self.check_win():
                messagebox.showinfo("Congratulations!", "You won the game!")
                self.root.quit()

    def reveal_recursive(self, x, y):
        cell = self.board.cells[x][y]
        if cell.is_revealed or cell.is_bomb:
            return

        cell.is_revealed = True
        btn = self.buttons[x][y]
        btn.config(bg="white", state=tk.DISABLED)
        if cell.neighbor_bombs > 0:
            btn.config(text=str(cell.neighbor_bombs))
        else:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.size and 0 <= ny < self.size:
                        self.reveal_recursive(nx, ny)

    def toggle_flag(self, x, y):
        cell = self.board.cells[x][y]
        if cell.is_revealed:
            return

        cell.is_flagged = not cell.is_flagged
        btn = self.buttons[x][y]
        if cell.is_flagged:
            btn.config(text="F", bg="yellow")
        else:
            btn.config(text="", bg="light gray")

    def show_mines(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board.cells[i][j].is_bomb:
                    self.buttons[i][j].config(text="B", bg="red")

    def check_win(self):
        for i in range(self.size):
            for j in range(self.size):
                cell = self.board.cells[i][j]
                if not cell.is_bomb and not cell.is_revealed:
                    return False
        return True

if __name__ == "__main__":
    size = int(input("Enter the size of the board: "))
    bombs = int(input("Enter the number of bombs: "))
    root = tk.Tk()
    Minesweeper(root, size, bombs)
    root.mainloop()
