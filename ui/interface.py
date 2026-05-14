import pygame
import sys


class Interface:
    def __init__(self, width=800, height=600, title="Minesweeper", rows=3, cols=3, on_click_callback=None):
        pygame.init()
        self.width = width
        self.height = height
        self.title = title
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)

        self.rows = rows
        self.cols = cols
        self.cell_size = 40

        self.on_click_callback = on_click_callback
        
        # Setup font to display numbers and mines later
        self.font = pygame.font.SysFont(None, 24)

        self.reset_grid()

        self.grid_width = self.cols * self.cell_size
        self.grid_height = self.rows * self.cell_size
        self.start_x = (self.width - (self.cols * self.cell_size)) // 2
        self.start_y = (self.height - (self.rows * self.cell_size)) // 2

        self.color_bg = (255, 255, 255)
        self.color_grid = (0, 0, 0)
        self.color_clicked = (200, 200, 200)

        self.running = True

    def reset_grid(self):
        self.grid_data = [[None for _ in range(self.cols)] for _ in range(self.rows)]

    def handle_click(self, pos):
        mouse_x, mouse_y = pos

        # 1. Check if the click is actually inside the grid area
        if (self.start_x <= mouse_x < self.start_x + self.grid_width and
            self.start_y <= mouse_y < self.start_y + self.grid_height):
            
            # 2. Calculate which row and column was clicked
            col = (mouse_x - self.start_x) // self.cell_size
            row = (mouse_y - self.start_y) // self.cell_size
            
            print(f"UI Log: Cell clicked at Row {row}, Col {col}")
            if self.on_click_callback:
                self.on_click_callback(row, col)
    
    def update_cell(self, row, col, value):
        """Logic file will call this to tell the UI what to display."""
        self.grid_data[row][col] = value

    def events_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            # Handle mouse click events
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    self.handle_click(event.pos)

            # Handle keyboard events for resetting the grid
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Detect the 'R' key
                    self.reset_grid()

    def draw_grid(self):
        for r in range(self.rows):
            for c in range(self.cols):
                x = self.start_x + (c * self.cell_size)
                y = self.start_y + (r * self.cell_size)
                rect = pygame.Rect(x, y, self.cell_size, self.cell_size)

                if self.grid_data[r][c] is not None:
                    pygame.draw.rect(self.screen, self.color_clicked, rect)
                    
                    # Render the text (e.g., "1", "2", "*")
                    text_surf = self.font.render(str(self.grid_data[r][c]), True, (0, 0, 0))
                    text_rect = text_surf.get_rect(center=rect.center)
                    self.screen.blit(text_surf, text_rect)

                pygame.draw.rect(self.screen, self.color_grid, rect, 1)

    def update_display(self):
        self.screen.fill(self.color_bg)
        self.draw_grid()
        pygame.display.flip()

    def run(self):
        while self.running:
            self.events_handling()
            self.update_display()
        pygame.quit()
        sys.exit()



if __name__ == "__main__":    
    game = Interface()
    game.run()