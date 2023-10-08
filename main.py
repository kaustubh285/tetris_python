import copy
import csv
from display import display


class Tetris:
    def __init__(self) -> None:
        # self.grid = [[0] * 10 for _ in range(10)]
        self.grid = [[0] * 10 for _ in range(10)]
        # self.grid[:3] = [[0] * 7 for _ in range(3)]
        # self.grid[3:6] = [[0] * 6 + [1] * 1 for _ in range(3)]
        # self.grid[6:] = [[0] * 3 + [1] * 4 for _ in range(4)]
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

    def provide_current_ones(self, shape, position):
        num_rows = len(shape)
        num_cols = len(shape[0])
        current_ones = []
        for i in range(num_rows):
            for j in range(num_cols):
                if shape[i][j] == 1:
                    current_ones.append((i, position + j))
        return current_ones

    def check_position_clash(self, x, y):
        if len(self.grid) == x + 1:
            return True
        try:
            if self.grid[x + 1][y] == 1:
                return True
        except:
            return True

    def check_topmost_occupant(self, shape, position):
        current_ones = self.provide_current_ones(shape, position)

        temp_curr = copy.deepcopy(current_ones)
        for idx, row in enumerate(self.grid):
            for i in range(len(temp_curr)):
                (x, y) = temp_curr[i]
                print(x, y)
                if self.check_position_clash(x, y):
                    print("CLASHHHHH at", x, y)
                    return current_ones
                temp_curr[i] = (temp_curr[i][0] + 1, temp_curr[i][1])
            current_ones = copy.deepcopy(temp_curr)

        return temp_curr

    def update_grid(self, new_values):
        for r_idx, row in enumerate(self.grid):
            for c_idx, cell in enumerate(row):
                if (r_idx, c_idx) in new_values:
                    self.grid[r_idx][c_idx] = 1
        display(self.grid, [])

    def new_input(self, value: str, position: int):
        print(value, position)
        curr = self.check_topmost_occupant(self.values[value], position)
        print("current_ones_results - ", curr)
        display(self.values[value], curr=[])
        display(self.grid, curr)
        self.update_grid(curr)
        # display(self.grid, [])
        pass


with open("temp_input.txt") as inputFile:
    reader_obj = csv.reader(inputFile)
    tetris = Tetris()
    for row in reader_obj:
        for [shape, entry] in row:
            tetris.new_input(shape.lower(), int(entry))
        print("---------" * 10 + "row ended")
