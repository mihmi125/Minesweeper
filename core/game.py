import pygame
import sys
import config
from logic.board import Board
from ui.interface import Interface
from ui.menu import Menu
from ui.settings import Settings

class Game:
    def __init__(self):
        # Set up the core system user interface handler
        self.ui = Interface(on_click_callback=self.handle_cell_click)
        
        # Instantiate supplementary user interface windows and supply them the main display screen
        self.menu = Menu(self.ui.screen)
        self.settings = Settings(self.ui.screen)
        
        # Initialize default launcher state setting to open into the MAIN MENU
        self.state = "MENU" 
        self.clock = pygame.time.Clock()
        self.running = True
        self.board = None

    def start_new_game(self):
        """
        Instantiates a fully generated board layout following the newest parameters set in settings.
        """
        self.board = Board(
            rows=config.GRID_ROWS,
            cols=config.GRID_COLS,
            mine_count=config.MINE_COUNT
        )
        # Link the freshly built logic board mapping back to the active Interface object
        self.ui.set_board(self.board)
        self.ui.running = True

    def handle_cell_click(self, row, col, button):
        # Handle left mouse actions (Reveal board cell coordinates)
        if button == 1:
            continue_game = self.board.reveal_cell(row, col)

            if not continue_game:
                print("GAME OVER")
            elif self.board.check_win():
                print("YOU WIN!")
                
        # Handle right mouse actions (Toggle custom flag icons)
        elif button == 3:
            self.board.toggle_flag(row, col)

    def run(self):
        """
        Master state machine game engine loop distributing tasks and draws based on current game state.
        """
        while self.running:
            if self.state == "MENU":
                self.menu.handle_events(self)
                self.menu.draw()
            elif self.state == "SETTINGS":
                self.settings.handle_events(self)
                self.settings.draw()
            elif self.state == "PLAYING":
                # Pass self argument down into events_handling to permit access to start_new_game and states
                self.ui.events_handling(self)
                self.ui.update_display()
                
                # Shutdown the app execution loops cleanly if internal UI loop triggers shutdown flags
                if not self.ui.running:
                    self.running = False
                    
            # Enforce execution time regulations utilizing target FPS definitions
            self.clock.tick(config.FPS)

        # De-allocate active module setups safely before system script exits
        pygame.quit()
        sys.exit()