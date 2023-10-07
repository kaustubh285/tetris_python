import csv


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

    def check_topmost_occupant(self, position):
        for idx, row in enumerate(self.grid):
            if sum(row):
                if row[position - 1] == 1:
                    print("blockage at ", idx, position - 1)
                    break
                if row[position] == 1:
                    print("blockage at ", idx, position)
                    break
                if row[position + 1] == 1:
                    print("blockage at ", idx, position + 1)
                    break
        pass

    def new_input(self, value: str, position: int):
        print(value, position)
        self.check_topmost_occupant(position)
        pass


with open("temp_input.txt") as inputFile:
    reader_obj = csv.reader(inputFile)
    tetris = Tetris()
    for row in reader_obj:
        for [shape, entry] in row:
            tetris.new_input(shape.lower(), int(entry))
        print("---------" * 10 + "row ended")
