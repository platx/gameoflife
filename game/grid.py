from game.square import Square


class Grid:
    """ Game manager to make generations of squares and manage grid
    grid_length - size of board in pixels
    square_size - size of one square in pixels
    active_color - fill color for active squares
    not_active_color - fill color for not active squares
    """
    def __init__(self, grid_length, square_size, active_color='black', not_active_color='white'):
        self.grid_length = grid_length
        self.square_size = square_size
        self.active_color = active_color
        self.not_active_color = not_active_color

        self.squares = self.create_squares()

    """ Init squares on grid """
    def create_squares(self):
        squares = {}
        for x in range(0, self.grid_length, self.square_size):
            for y in range(0, self.grid_length, self.square_size):
                squares[(x, y)] = Square(
                    (x, y),
                    self.grid_length,
                    self.square_size,
                    False,
                    self.active_color,
                    self.not_active_color
                )

        return squares
