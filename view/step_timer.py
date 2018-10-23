import tkinter as tk


class StepTimer:
    """ Main view constructor
    view - main view object
    """
    def __init__(self, main_view, update_freq=100):
        self.started = False
        self.update_freq = update_freq
        self.main_view = main_view

        self.timer = tk.Scale(
            self.main_view,
            from_=10,
            to=500,
            orient=tk.HORIZONTAL,
            length=self.main_view.game_manager.grid_length,
            showvalue=False,
            command=self.update_freq_changed
        )
        self.timer.set(update_freq)
        self.timer.grid(row=2, column=0, columnspan=5)

    """ Start timer """
    def start(self):
        self.started = True
        self.main_view.button_manager.buttons['play'].config(state=tk.DISABLED)
        self.main_view.button_manager.buttons['stop'].config(state=tk.ACTIVE)
        self.main_view.button_manager.buttons['next'].config(state=tk.DISABLED)
        self.main_view.button_manager.buttons['generate'].config(state=tk.DISABLED)
        self.main_view.button_manager.buttons['reset'].config(state=tk.DISABLED)

        self.main_view.after(self.update_freq, self.update)

    """ Update timer """
    def update(self):
        self.main_view.button_manager.buttons['play'].config(state=tk.ACTIVE)
        self.main_view.button_manager.buttons['stop'].config(state=tk.DISABLED)
        self.main_view.button_manager.buttons['next'].config(state=tk.ACTIVE)
        self.main_view.button_manager.buttons['generate'].config(state=tk.ACTIVE)
        self.main_view.button_manager.buttons['reset'].config(state=tk.ACTIVE)

        self.main_view.game_manager.next_generation()
        self.main_view.square_manager.update_squares()

        if self.started:
            self.start()

    """ Stop timer """
    def stop(self):
        self.started = False

    def update_freq_changed(self, value):
        self.update_freq = value
