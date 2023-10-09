import csv
from typing import List


class Tetris:
    def __init__(self) -> None:
        # Initialized an empty grid of 10 x 10
        self.grid = [[0] * 10 for _ in range(10)]
        self.values = {
            "q": [[1, 1], [1, 1]],
            "z": [[1, 1, 0], [0, 1, 1]],
            "s": [[0, 1, 1], [1, 1, 0]],
            "t": [[1, 1, 1], [0, 1, 0]],
            "i": [[1, 1, 1, 1]],
            "L": [[1, 0], [1, 0], [1, 1]],
            "j": [[0, 1], [0, 1], [1, 1]],
        }
        self.grid_block_height = 0

    def provide_block_cell_positions(self, shape: List[List[int]], position: int):
        """Consider the block/shape to be a matrix including 0s and 1s. We create a list of all positions in cordinate format to know at which positions the 1s will be at any given time.
        For example if a Q block is entering in position 5, then the starting list would be - [(0,5),(0,6),(1,5),(1,6)]
        This is done because it would be difficult to work with a multi-dimensional array when checking the block's decent in the grid.
        """
        block_num_rows = len(shape)
        block_num_cols = len(shape[0])
        block_cell_positions = []

        for row in range(block_num_rows):
            for col in range(block_num_cols):
                if shape[row][col] == 1:
                    block_cell_positions.append((row, position + col))

        # TODO : The block is automatically placed in the first 2 rows of the grid and then moving it  down. This can be improved to have the block above the grid and move into the grid to help identify blockages in it's path in the first 2 rows.
        return block_cell_positions

    def check_position_clash(self, x, y):
        """Checks if the cell is already at the bottom, or will hit any other block if moved downwards."""
        if len(self.grid) == x + 1:
            return True
        try:
            if self.grid[x + 1][y] == 1:
                return True
        except:
            return True

    def check_topmost_occupant(self, shape: List[List[int]], position: int):
        """Core logic.
        Gets the list of cells in the shape/block. Iterates through each row and checks the decent of the block through the grid.
        If it reaches the bottom of the grid, or will clash with another block in the next iteration, then it stops and returns the final array of the position of the current block. eg : a Q block moving down the 5th position - [(3,5), (3,6),(4,5),(4,6)]
        """
        block_cell_positions = self.provide_block_cell_positions(shape, position)

        temp_curr = block_cell_positions[:]
        for idx, row in enumerate(self.grid):
            for i in range(len(temp_curr)):
                (x, y) = temp_curr[i]
                if self.check_position_clash(x, y):
                    return block_cell_positions
                temp_curr[i] = (temp_curr[i][0] + 1, temp_curr[i][1])
            block_cell_positions = temp_curr[:]

        return temp_curr

    def update_grid(self, new_values):
        """
        Using the final positions of the new block cells we obtained, we change the values at those positions to "1" in the grid.
        """
        for r_idx, row in enumerate(self.grid):
            for c_idx, cell in enumerate(row):
                if (r_idx, c_idx) in new_values:
                    self.grid[r_idx][c_idx] = 1

    def new_input(self, value: str, position: int):
        """This is the function that calls all the other functions and is triggered when a new block is added to the grid"""
        curr = self.check_topmost_occupant(self.values[value], position)
        self.update_grid(curr)
        self.check_if_row_complete()
        self.check_and_update_height()

    def check_and_update_height(self):
        """
        Calculats the updated height of blocks in the grid
        """
        height = 0
        for idx, rows in enumerate(self.grid):
            if 1 in rows:
                height += 1

        self.grid_block_height = height

    def print_occupied_height(self):
        return self.grid_block_height

    def check_if_row_complete(self):
        completed_rows = [
            idx for idx, row in enumerate(self.grid) if sum(row) == len(self.grid[0])
        ]
        if completed_rows:
            for idx in completed_rows:
                self.grid.pop(idx)

            num_completed_rows = len(completed_rows)
            for _ in range(num_completed_rows):
                self.grid.insert(0, [0] * len(self.grid[0]))


with open("input.txt") as inputFile:
    reader_obj = csv.reader(inputFile)
    tetris = Tetris()

    # For every line in the file
    for row in reader_obj:
        # for every Shape & position in the line we run the below forloop and then get the height logged
        for [shape, entry_position] in row:
            tetris.new_input(shape.lower(), int(entry_position))

        print(tetris.print_occupied_height())
