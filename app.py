from view.main import MainView
from game.manager import GameManager

grid_length = 800
square_size = 25
title = 'Game of life'

game_manager = GameManager(grid_length, square_size)

main_view = MainView(game_manager)
main_view.wm_title(title)
main_view.mainloop()
