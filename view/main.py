import tkinter as tk
from view.buttons import ButtonManager
from view.squares import SquareManager


class MainView(tk.Tk):
    """ Main view constructor
    game_manager - game manager object
    """
    def __init__(self, game_manager, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.game_manager = game_manager
        self.square_manager = SquareManager(
            self,
            width=self.game_manager.grid_length,
            height=self.game_manager.grid_length
        )
        self.button_manager = ButtonManager(self)
