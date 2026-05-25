import pygame
import sys
import config

class Settings:
    def __init__(self, screen):
        # Assign the screen surface reference
        self.screen = screen
        
        # Set up text fonts for value labels and primary section headers
        self.font = pygame.font.SysFont("Arial", 30)
        self.title_font = pygame.font.SysFont("Arial", 50)
        
        # Map out precise coordinates for row manipulation controls (+ and - rectangles)
        self.row_minus = pygame.Rect(480, 200, 40, 40)
        self.row_plus = pygame.Rect(580, 200, 40, 40)
        
        # Map out precise coordinates for column manipulation controls (+ and - rectangles)
        self.col_minus = pygame.Rect(480, 270, 40, 40)
        self.col_plus = pygame.Rect(580, 270, 40, 40)
        
        # Map out precise coordinates for mine manipulation controls (+ and - rectangles)
        self.mine_minus = pygame.Rect(480, 340, 40, 40)
        self.mine_plus = pygame.Rect(580, 340, 40, 40)
        
        # Position the navigation BACK button to exit configuration menu
        self.back_rect = pygame.Rect(config.SCR_WIDTH // 2 - 75, 460, 150, 50)

    def draw(self):
        # Clear screen with dark background accent colors
        self.screen.fill((40, 40, 40))
        
        # Draw the settings main page header title
        title_text = self.title_font.render("SETTINGS", True, (255, 255, 255))
        self.screen.blit(title_text, (config.SCR_WIDTH // 2 - title_text.get_width() // 2, 80))
        
        # Create a clean loop dataset array containing configuration records
        labels = [
            ("Rows (Read):", config.GRID_ROWS, 200, self.row_minus, self.row_plus),
            ("Columns (Veerud):", config.GRID_COLS, 270, self.col_minus, self.col_plus),
            ("Mines (Miinid):", config.MINE_COUNT, 340, self.mine_minus, self.mine_plus)
        ]
        
        # Loop over the items array to render controls systematically
        for label_text, val, y_pos, btn_minus, btn_plus in labels:
            # Render feature name text label
            lbl = self.font.render(label_text, True, (255, 255, 255))
            self.screen.blit(lbl, (180, y_pos + 5))
            
            # Construct standard Crimson-red styled MINUS (-) button layout
            pygame.draw.rect(self.screen, (150, 50, 50), btn_minus, border_radius=5)
            m_txt = self.font.render("-", True, (255, 255, 255))
            self.screen.blit(m_txt, (btn_minus.centerx - m_txt.get_width()//2, btn_minus.centery - m_txt.get_height()//2 - 2))
            
            # Display current configuration integer values between buttons
            val_txt = self.font.render(str(val), True, (255, 255, 255))
            self.screen.blit(val_txt, (540 - val_txt.get_width()//2, y_pos + 5))
            
            # Construct standard Forest-green styled PLUS (+) button layout
            pygame.draw.rect(self.screen, (50, 150, 50), btn_plus, border_radius=5)
            p_txt = self.font.render("+", True, (255, 255, 255))
            self.screen.blit(p_txt, (btn_plus.centerx - p_txt.get_width()//2, btn_plus.centery - p_txt.get_height()//2 - 2))
            
        # Draw and display the grey navigation BACK button components
        pygame.draw.rect(self.screen, (100, 100, 100), self.back_rect, border_radius=5)
        back_txt = self.font.render("BACK", True, (255, 255, 255))
        self.screen.blit(back_txt, (self.back_rect.centerx - back_txt.get_width()//2, self.back_rect.centery - back_txt.get_height()//2))
        
        pygame.display.flip()

    def handle_events(self, game_obj):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            # Intercept left click events
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = event.pos
                
                # Check if user clicks back navigation button
                if self.back_rect.collidepoint(pos):
                    game_obj.state = "MENU"
                
                # Handle Row subtractions and additions (Enforce minimum bound of 3)
                elif self.row_minus.collidepoint(pos):
                    if config.GRID_ROWS > 3:
                        config.GRID_ROWS -= 1
                        # Safety: automatically lower mine count if it overflows the new maximum capacity
                        if config.MINE_COUNT >= config.GRID_ROWS * config.GRID_COLS:
                            config.MINE_COUNT = (config.GRID_ROWS * config.GRID_COLS) - 1
                elif self.row_plus.collidepoint(pos):
                    if config.GRID_ROWS < 18: # Hard limit preventing the window from overflowing vertically
                        config.GRID_ROWS += 1
                        
                # Handle Column subtractions and additions (Enforce minimum bound of 3)
                elif self.col_minus.collidepoint(pos):
                    if config.GRID_COLS > 3:
                        config.GRID_COLS -= 1
                        # Safety Check: keep mine count lower than available cells
                        if config.MINE_COUNT >= config.GRID_ROWS * config.GRID_COLS:
                            config.MINE_COUNT = (config.GRID_ROWS * config.GRID_COLS) - 1
                elif self.col_plus.collidepoint(pos):
                    if config.GRID_COLS < 24: # Hard limit preventing screen width overflow
                        config.GRID_COLS += 1
                        
                # Handle Mine subtractions and additions (Enforce minimum bound of 1)
                elif self.mine_minus.collidepoint(pos):
                    if config.MINE_COUNT > 1:
                        config.MINE_COUNT -= 1
                elif self.mine_plus.collidepoint(pos):
                    # Enforce strict maximum mine boundary constraint (Total cells - 1) to avoid map initialization infinite loops
                    if config.MINE_COUNT < (config.GRID_ROWS * config.GRID_COLS) - 1:
                        config.MINE_COUNT += 1