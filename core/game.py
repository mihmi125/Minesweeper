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

        self.ui = Interface(on_click_callback=self.handle_cell_click)
        self.ui.set_board(self.board)

    def handle_cell_click(self, row, col, button):
        if button == 1:
            continue_game = self.board.reveal_cell(row, col)

            if not continue_game:
                print("GAME OVER")
            elif self.board.check_win():
                print("YOU WIN!")

        elif button == 3:
            self.board.toggle_flag(row, col)

    def run(self):
        self.ui.run()