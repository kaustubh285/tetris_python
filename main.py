import csv


class Tetris:
    def __init__(self) -> None:
        self.grid = [[0] * 10] * 10
        self.values = {
            "q": [[1, 1], [1, 1]],
            "z": [[1, 1, 0], [0, 1, 1]],
            "s": [[0, 1, 1], [1, 1, 0]],
            "t": [[1, 1, 1], [0, 1, 0]],
            "i": [[1, 1, 1, 1]],
            "L": [[1, 0], [1, 0], [1, 1]],
            "j": [[0, 1], [0, 1], [1, 1]],
        }
        pass

    def print_grid(self):
        print(self.grid)

    def new_input(self, value, position):
        pass


# with open('input.txt') as inputFile:
