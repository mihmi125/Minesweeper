import pygame
import sys
import config

class Menu:
    def __init__(self, screen):
        # Assign the active drawing screen surface
        self.screen = screen
        
        # Instantiate typography and fonts for titles and interactable buttons
        self.font = pygame.font.SysFont("Arial", 40)
        self.title_font = pygame.font.SysFont("Arial", 60)
        
        # Define structural boundary boxes (rectangles) for menu button layouts centered horizontally
        self.play_rect = pygame.Rect(config.SCR_WIDTH // 2 - 100, 220, 200, 60)
        self.settings_rect = pygame.Rect(config.SCR_WIDTH // 2 - 100, 320, 200, 60)

    def draw(self):
        # Clear background canvas using a modern dark-grey color palette
        self.screen.fill((40, 40, 40)) 
        
        # Render and draw the main game title banner
        title_text = self.title_font.render("MINESWEEPER", True, (255, 255, 255))
        self.screen.blit(title_text, (config.SCR_WIDTH // 2 - title_text.get_width() // 2, 100))
        
        # Render and position the PLAY button components (Background + Label Text)
        pygame.draw.rect(self.screen, (0, 140, 0), self.play_rect, border_radius=8)
        play_text = self.font.render("PLAY", True, (255, 255, 255))
        self.screen.blit(play_text, (self.play_rect.centerx - play_text.get_width() // 2, self.play_rect.centery - play_text.get_height() // 2))
        
        # Render and position the SETTINGS button components (Background + Label Text)
        pygame.draw.rect(self.screen, (70, 70, 140), self.settings_rect, border_radius=8)
        settings_text = self.font.render("SETTINGS", True, (255, 255, 255))
        self.screen.blit(settings_text, (self.settings_rect.centerx - settings_text.get_width() // 2, self.settings_rect.centery - settings_text.get_height() // 2))
        
        # Refresh the entire display surface to update drawings on screen
        pygame.display.flip()

    def handle_events(self, game_obj):
        # Scan through the window's ongoing event queues
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Detect left click actions from user mouse inputs
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # If play button boundary is clicked, launch a new board and enter PLAYING state
                if self.play_rect.collidepoint(event.pos):
                    game_obj.start_new_game()
                    game_obj.state = "PLAYING"
                # If settings button boundary is clicked, swap to SETTINGS menu state
                elif self.settings_rect.collidepoint(event.pos):
                    game_obj.state = "SETTINGS"