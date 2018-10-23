import tkinter as tk
from lib import numbers


class SquareManager(tk.Canvas):
    """ Squares view manager
    main_view - main_view object
    """
    def __init__(self, main_view, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
        self.main_view = main_view
        self.grid(row=0, column=0, columnspan=5)
        self.squares = self.create_squares()
        self.prev = None

    """ Create squares on canvas """
    def create_squares(self):
        squares = {}

        for square in self.main_view.game_manager.grid.squares.values():
            squares[square.coordinates] = self.create_rectangle(
                square.coordinates[0],
                square.coordinates[1],
                square.bottom_coordinates[0],
                square.bottom_coordinates[1],
                fill=square.get_color()
            )
            self.tag_bind(
                squares[square.coordinates],
                '<Button-1>',
                lambda event, coordinates=square.coordinates: self.square_clicked(coordinates)
            )

        self.bind(
            '<B1-Motion>',
            self.square_motion
        )

        return squares

    """ Update all squares state on canvas """
    def update_squares(self):
        for square in self.main_view.game_manager.grid.squares.values():
            self.update_square(square)

    """ Update specific square state on canvas 
    square - square object to update state
    """
    def update_square(self, square):
        self.itemconfig(self.squares[square.coordinates], fill=square.get_color())

    """ Callback for click on square to change state """
    def square_clicked(self, coordinates):
        self.main_view.game_manager.set_state(coordinates)
        self.update_square(self.main_view.game_manager.grid.squares[coordinates])

    """ Callback for mouse motion on square to change state """
    def square_motion(self, event):
        coordinates = (
            numbers.round_int(event.x, self.main_view.game_manager.square_size),
            numbers.round_int(event.y, self.main_view.game_manager.square_size)
        )

        if self.prev != coordinates and coordinates in self.main_view.game_manager.grid.squares.keys():
            self.main_view.game_manager.set_state(coordinates)
            self.update_square(self.main_view.game_manager.grid.squares[coordinates])
            self.prev = coordinates
