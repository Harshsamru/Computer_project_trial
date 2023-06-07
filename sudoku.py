from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import NumericProperty
from kivy.clock import Clock
from random import randint


class Sudoku(Screen):
    # The board will have 9x9 squares
    rows = 9
    columns = 9

    # This will be the actual board with the numbers
    board = []

    # This will be the temporary board used to check if a number is valid
    temp_board = []

    # This will be the current number that the user is selecting
    current_number = 1

    # This will be the index of the current square that the user is selecting
    current_index = [0, 0]

    # This will keep track of how many squares the user has filled in
    squares_filled = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_board()
        self.create_temp_board()

    def create_board(self):
        # Create an empty board
        self.board = [[0 for i in range(self.columns)] for j in range(self.rows)]

        # Fill in the board with random numbers
        for i in range(self.rows):
            for j in range(self.columns):
                if randint(1, 100) < 30:  # 30% chance of filling in a square
                    number = randint(1, 9)
                    if self.check_validity(i, j, number):
                        self.board[i][j] = number

        # Set the squares_filled variable to the number of squares already filled in
        self.squares_filled = sum([1 for row in self.board for square in row if square != 0])

    def create_temp_board(self):
        # Create a temporary board that is the same as the actual board
        self.temp_board = [[square for square in row] for row in self.board]

    def check_validity(self, row, column, number):
        # Check if the number is already in the same row or column
        for i in range(self.rows):
            if self.board[row][i] == number:
                return False
            if self.board[i][column] == number:
                return False

        # Check if the number is already in the same 3x3 square
        square_row = (row // 3) * 3
        square_column = (column // 3) * 3
        for i in range(square_row, square_row + 3):
            for j in range(square_column, square_column + 3):
                if self.board[i][j] == number:
                    return False

        # If the number is not in the same row, column, or square, it is valid
        return True

    def select_number(self, number):
        self.current_number = number

    def select_square(self, row, column):
        self.current_index = [row, column]

    def fill_square(self):
        # Check if the current square is empty
        if self.board[self.current_index[0]][self.current_index[1]] == 0:
            # Check if the current number is valid for the current square
            if self.check_validity(self.current_index[0], self.current_index[1], self.current_number):
                # Fill in the current square with the current number
                self.board[self.current_index[0]][self.current_index[1]] = self.current_number
                self.squares_filled += 1

