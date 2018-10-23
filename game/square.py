class Square:
    """ Square
    coordinates - tuple with coordinates (x, y)
    grid_length - size of board in pixels
    square_size - size of one square in pixels
    state - Current state of square
    active_color - fill color for active state
    not_active_color - fill color for not active state
    """
    def __init__(self, coordinates, grid_length, square_size, state=False, active_color='black', not_active_color='white'):
        self.coordinates = coordinates
        self.grid_length = grid_length
        self.square_size = square_size
        self.bottom_coordinates = self.get_bottom_coordinates()
        self.state = state
        self.active_color = active_color
        self.not_active_color = not_active_color
        self.neighbors = self.get_neighbors()

    """ Returns bottom right corner coordinates of square (x, y) """
    def get_bottom_coordinates(self):
        return self.coordinates[0] + self.square_size, self.coordinates[1] + self.square_size

    """ Returns fill color for square by state """
    def get_color(self):
        return self.active_color if self.state else self.not_active_color

    """ Checks if coordinates are in range of grid 
    coordinates - coordinates to check (x, y)
    """
    def check_coordinates(self, coordinates):
        (x, y) = coordinates

        min_coordinate = 0
        max_coordinate = self.grid_length-self.square_size

        return min_coordinate <= x <= max_coordinate and min_coordinate <= y <= max_coordinate

    """ Returns all neighbours of current square """
    def get_neighbors(self):
        (x, y) = self.coordinates

        return list(
            filter(self.check_coordinates, [
                (x-self.square_size, y+self.square_size), (x, y+self.square_size), (x+self.square_size, y+self.square_size),
                (x-self.square_size, y),                                           (x+self.square_size, y),
                (x-self.square_size, y-self.square_size), (x, y-self.square_size), (x+self.square_size, y-self.square_size)
            ])
        )

    """ Updates square state using active neighbors 
    count_active - count of active neighbors
    """
    def update_state(self, count_active):
        if self.state:
            if count_active < 2 or count_active > 3:
                self.state = False
        else:
            if count_active == 3:
                self.state = True

