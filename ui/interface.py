import pygame
import sys
import config

class Interface:
    def __init__(self, on_click_callback=None):
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
        
        self.board = None

        # Calculate the total grid width and height
        self.grid_width = self.cols * self.cell_size
        self.grid_height = self.rows * self.cell_size

        # Calculate the starting x and y coordinates to center the grid on the screen
        self.start_x = (self.width - (self.cols * self.cell_size)) // 2
        self.start_y = (self.height - (self.rows * self.cell_size)) // 2

        self.running = True

    def set_board(self, board):
        """
        Connects the logic Board instance to this Interface and 
        dynamically calculates grid sizes and centering offsets.
        """
        self.board = board
        
        # Dynamically update rows and columns based on the newly provided board configuration
        self.rows = board.rows
        self.cols = board.columns
        
        # Recalculate grid pixel dimensions dynamically
        self.grid_width = self.cols * self.cell_size
        self.grid_height = self.rows * self.cell_size
        
        # Recalculate starting positions to center the grid on the current screen size
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

    def events_handling(self, game_obj=None):
        """Processes user inputs (mouse clicks, key presses, closing window)."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                if game_obj:
                    game_obj.running = False

            # Left-click is used for revealing tiles
            # Right-click is used for flagging
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left Mouse Button
                    self.handle_click(event.pos, button=1)
                elif event.button == 3:  # Right Mouse Button
                    self.handle_click(event.pos, button=3)

            # Pressing 'R' key will reset the game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # 'R' key for Reset
                    # 'R' key resets the game by initiating a completely fresh board instance
                    if game_obj:
                        game_obj.start_new_game() # Tells the logic board to restart
                # ESC leads back to menu
                elif event.key == pygame.K_ESCAPE: 
                    # ESC key seamlessly transitions the player back to the main menu screen
                    if game_obj:
                        game_obj.state = "MENU"
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

    def run(self):
        """Main game loop."""
        clock = pygame.time.Clock()
        clock.tick(config.FPS)  # Limit the frame rate to FPS rate in config.py
        while self.running:
            self.events_handling()  # 1. Check for inputs
            self.update_display()   # 2. Draw everything
            clock.tick(config.FPS)  # 3. Maintain steady frame rate

        # Clean up and close the application
        pygame.quit()
        sys.exit()