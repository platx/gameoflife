from game.grid import Grid
import random


class GameManager:
    """ Game manager to make generations of squares and manage grid
    board_length - size of board in pixels
    square_size - size of one square in pixels
    """
    def __init__(self, grid_length, square_size):
        self.grid_length = grid_length
        self.square_size = square_size
        self.grid = Grid(grid_length=self.grid_length, square_size=self.square_size)

    """ Sets state of square by coordinates
    coordinates - coordinates of needed square (x, y)
    """
    def set_state(self, coordinates):
        if self.grid.squares[coordinates].state:
            self.grid.squares[coordinates].state = False
        else:
            self.grid.squares[coordinates].state = True

    """ Resets squares state """
    def reset_state(self):
        for square in self.grid.squares.values():
            square.state = False

    """ Makes new generation of squares using neighbors state """
    def next_generation(self):
        for square in self.grid.squares.values():
            square.update_state(self.check_neighbors(square))

    """ Makes random state of squares """
    def random_generation(self):
        for square in self.grid.squares.values():
            square.state = bool(random.getrandbits(1))

    """ Returns count of active neighbours for square 
    square - square object to check neighbors
    """
    def check_neighbors(self, square):
        count_active = 0

        for neighbor_coordinates in square.neighbors:
            if neighbor_coordinates in self.grid.squares.keys() and self.grid.squares[neighbor_coordinates].state:
                count_active += 1

        return count_active
