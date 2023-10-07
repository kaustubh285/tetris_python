import csv
from display import display


class Tetris:
    def __init__(self) -> None:
        # self.grid = [[0] * 10] * 10
        self.grid = [[0] * 7] * 3 + [[0] * 5 + [1] * 2] * 3 + [[0] * 3 + [1] * 4] * 3
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

    def check_topmost_occupant(self, shape, position):
        current_row = 0
        num_rows = len(shape)
        num_cols = len(shape[0])
        print(num_rows, num_cols)

        current_x = position
        current_y = 0

        current_ones = []
        for i in range(num_rows):
            for j in range(num_cols):
                if shape[i][j] == 1:
                    current_ones.append((i, j))
        temp_curr = current_ones
        print(current_ones)

        for i in range(len(current_ones)):
            current_ones[i] = (current_ones[i][0], current_ones[i][1] + 1)

        for idx, row in enumerate(self.grid):
            if sum(row):
                if row[position] == 1:
                    print("blockage at ", idx, position)
                    break
                if row[position + 1] == 1:
                    print("blockage at ", idx, position + 1)
                    break
            # block did not have any blockage, it has moved to the below row

        return current_row

    def find_down(shape):
        pass

    def new_input(self, value: str, position: int):
        print(value, position)
        self.check_topmost_occupant(self.values[value], position)
        display(self.values[value])
        display(self.grid)
        pass


with open("temp_input.txt") as inputFile:
    reader_obj = csv.reader(inputFile)
    tetris = Tetris()
    for row in reader_obj:
        for [shape, entry] in row:
            tetris.new_input(shape.lower(), int(entry))
        print("---------" * 10 + "row ended")
