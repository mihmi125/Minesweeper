import sys
import pygame
import config
from logic.board import Board
from ui.interface import Interface
from ui.menu import Menu
from ui.settings import Settings

class Game:
    def __init__(self):
        self.current_state = "MENU"
        self.running = True
        self.clock = pygame.time.Clock()

        self.game_ui = Interface(
            on_click_callback=self.handle_cell_click,
            change_state_callback=self.change_state,
            on_reset_callback=self.start_fresh_board
        )

        self.menu_ui = Menu(screen=self.game_ui.screen, change_state_callback=self.change_state)
        self.settings_ui = Settings(screen=self.game_ui.screen, change_state_callback=self.change_state)

        self.board = None
        self.start_fresh_board()

    def start_fresh_board(self):
        self.board = Board(
            rows=config.GRID_ROWS,
            cols=config.GRID_COLS,
            mine_count=config.MINE_COUNT
        )
        self.game_ui.set_board(self.board)
        self.board.reset_board()

    def change_state(self, new_state):
        self.current_state = new_state
        if new_state == "GAME":
            self.start_fresh_board()

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
        while self.running:
            active_ui = None

            if self.current_state == "MENU":
                active_ui = self.menu_ui
            elif self.current_state == "SETTINGS":
                active_ui = self.settings_ui
            elif self.current_state == "GAME":
                active_ui = self.game_ui

            signal = active_ui.events_handling()
            if signal == "QUIT":
                self.running = False
                break

            active_ui.update_display()
            self.clock.tick(config.FPS)

        pygame.quit()
        sys.exit()