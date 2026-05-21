import config
from logic.board import Board
from ui.interface import Interface

class Game:
    def __init__(self):
        self.board = Board(
            rows=config.GRID_ROWS,
            cols=config.GRID_COLS,
            mine_count=config.MINE_COUNT
        )

        self.ui = Interface(
            width=config.SCR_WIDTH,
            height=config.SCR_HEIGHT,
            title=config.TITLE,
            rows=config.GRID_ROWS,
            cols=config.GRID_COLS,
        )

        self.ui.cell_size = config.TILE_SIZE
        self.sync_ui_with_board()