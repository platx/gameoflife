import tkinter as tk
from PIL import ImageTk, Image
from resources.manager import ResourceManager
from view.step_timer import StepTimer


class ButtonManager:
    """ Buttons class
    main_view - main view object
    """
    def __init__(self, main_view):
        self.main_view = main_view
        self.step_timer = StepTimer(self.main_view)

        self.resource_manager = ResourceManager()

        self.images = self.init_images()

        self.buttons = self.init_buttons()

        column = 0
        for button in self.buttons.values():
            button.grid(row=1, column=column, sticky='we')
            column += 1

    """ Init images for buttons """
    def init_images(self):
        return {
            'play': ImageTk.PhotoImage(Image.open(self.resource_manager.get_image_path('play.png'))),
            'stop': ImageTk.PhotoImage(Image.open(self.resource_manager.get_image_path('stop.png'))),
            'next': ImageTk.PhotoImage(Image.open(self.resource_manager.get_image_path('next.png'))),
            'generate': ImageTk.PhotoImage(Image.open(self.resource_manager.get_image_path('shuffle.png'))),
            'reset': ImageTk.PhotoImage(Image.open(self.resource_manager.get_image_path('reset.png'))),
        }

    """ Init list of buttons """
    def init_buttons(self):
        return {
            'play': tk.Button(self.main_view, image=self.images['play'], command=self.start_timer),
            'stop': tk.Button(self.main_view, image=self.images['stop'], command=self.stop_timer, state=tk.DISABLED),
            'next': tk.Button(self.main_view, image=self.images['next'], command=self.next_step),
            'generate': tk.Button(self.main_view, image=self.images['generate'], command=self.generate_state),
            'reset': tk.Button(self.main_view, image=self.images['reset'], command=self.reset_state),
        }

    """ Next generation of squares callback """
    def next_step(self):
        self.main_view.game_manager.next_generation()
        self.main_view.square_manager.update_squares()

    """ Loop generation of squares callback """
    def start_timer(self):
        self.step_timer.start()

    """ Stop loop generation """
    def stop_timer(self):
        self.step_timer.stop()

    """ Random generation of squares state callback """
    def generate_state(self):
        self.main_view.game_manager.random_generation()
        self.main_view.square_manager.update_squares()

    """ Reset squares state callback """
    def reset_state(self):
        self.main_view.game_manager.reset_state()
        self.main_view.square_manager.update_squares()
