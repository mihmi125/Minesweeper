import pygame
import config

class Interface:
    def __init__(self, on_click_callback=None, change_state_callback=None, on_reset_callback=None):
        pygame.init()

        # Screen settings from config.py
        self.width = config.SCR_WIDTH
        self.height = config.SCR_HEIGHT
        self.title = config.TITLE
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)

        # Grid dimensions and tile size from config.py
        self.rows = config.GRID_ROWS
        self.cols = config.GRID_COLS
        self.cell_size = config.TILE_SIZE

        #The callback function sends click data to main.py/logic.py
        self.on_click_callback = on_click_callback
        self.change_state_callback = change_state_callback
        self.on_reset_callback = on_reset_callback
        
        self.board = None
        self.refresh_dimensions()

    def set_board(self, board):
        """Links logic mapping engine variables and triggers dynamic boundary math updates."""
        self.board = board
        if board:
            self.rows = getattr(board, 'rows', config.GRID_ROWS)
            self.cols = getattr(board, 'cols', getattr(board, 'columns', config.GRID_COLS))
        self.refresh_dimensions()

    def refresh_dimensions(self):
        """Calculates exact board boundaries and centers grid alignment offsets."""
        self.grid_width = self.cols * self.cell_size
        self.grid_height = self.rows * self.cell_size

        self.start_x = (self.width - self.grid_width) // 2
        self.start_y = (self.height - self.grid_height) // 2

    def handle_click(self, pos, button):
        """Converts mouse pixel coordinates into grid row and column."""
        mouse_x, mouse_y = pos

        # Check if the click coordinates are inside the grid boundaries
        if (self.start_x <= mouse_x < self.start_x + self.grid_width and
            self.start_y <= mouse_y < self.start_y + self.grid_height):
            
            # Calculate which row and column was clicked
            col = (mouse_x - self.start_x) // self.cell_size
            row = (mouse_y - self.start_y) // self.cell_size
            
            # If a callback function was provided, send the row, col and button to logic
            if self.on_click_callback:
                self.on_click_callback(row, col, button)

    def events_handling(self):
        """Processes user inputs (mouse clicks, key presses, closing window)."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"

            # Left-click is used for revealing tiles
            # Right-click is used for flagging
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left Mouse Button
                    self.handle_click(event.pos, button=1)
                elif event.button == 3:  # Right Mouse Button
                    self.handle_click(event.pos, button=3)

            # Pressing 'R' key will reset the game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Hotkey R resets game tracking data
                    if self.on_reset_callback:
                        self.on_reset_callback()
                    elif self.board:
                        self.board.reset_board() # Tells the logic board to restart

                elif event.key == pygame.K_ESCAPE:  # ESC leads back to menu selection maps
                    if self.change_state_callback:
                        self.change_state_callback("MENU")
        return None

    def draw_grid(self):
        """Loops through the logic grid and draws the corresponding images."""
        if not self.board:
            return

        for r in range(self.rows):
            for c in range(self.cols):
                # Get the Cell object from our logic board
                cell = self.board.grid[r][c]

                # Calculate the pixel position for this specific cell
                x = self.start_x + (c * self.cell_size)
                y = self.start_y + (r * self.cell_size)

                # Default image is the 'Unknown' (unrevealed) tile
                image = config.tile_unknown

                # Check the state of the logic cell to decide which image to show
                if cell.is_revealed:
                    if cell.is_mine:
                        #Gets mine image
                        image = config.tile_mine
                    elif cell.neighbor_mines == 0:
                        #Gets empty tile image
                        image = config.tile_empty
                    else:
                        # Gets mine count number image (1-8)
                        image = config.tile_numbers[cell.neighbor_mines - 1]
                elif cell.is_flagged:
                    image = config.tile_flag

                # Draw the selected image at the calculated (x, y) position
                self.screen.blit(image, (x, y))

    def update_display(self):
        """Clears the screen and draws the updated grid."""
        self.screen.fill((50, 50, 50)) #Gray background color
        self.draw_grid()              #Draw the grid on the screen
        pygame.display.flip()         #Update the display to show the new frame