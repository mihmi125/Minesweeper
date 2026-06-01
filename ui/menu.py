import pygame
import config

class Menu:
    def __init__(self, screen, change_state_callback):
        self.screen = screen
        self.change_state_callback = change_state_callback

        # Typography setup
        self.font = pygame.font.SysFont("Arial", 40)
        self.title_font = pygame.font.SysFont("Arial", 60)

        # Center-aligned button layouts
        self.play_rect = pygame.Rect(config.SCR_WIDTH // 2 - 100, 220, 200, 60)
        self.settings_rect = pygame.Rect(config.SCR_WIDTH // 2 - 100, 320, 200, 60)

    def events_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.play_rect.collidepoint(event.pos):
                    self.change_state_callback("GAME")
                elif self.settings_rect.collidepoint(event.pos):
                    self.change_state_callback("SETTINGS")
        return None

    def update_display(self):
        self.screen.fill((40, 40, 40))

        # Main Title Header
        title_text = self.title_font.render("MINESWEEPER", True, (255, 255, 255))
        self.screen.blit(title_text, (config.SCR_WIDTH // 2 - title_text.get_width() // 2, 100))

        # PLAY Button components
        pygame.draw.rect(self.screen, (0, 140, 0), self.play_rect, border_radius=8)
        play_text = self.font.render("PLAY", True, (255, 255, 255))
        self.screen.blit(play_text, (self.play_rect.centerx - play_text.get_width() // 2, self.play_rect.centery - play_text.get_height() // 2))

        # SETTINGS Button components
        pygame.draw.rect(self.screen, (70, 70, 140), self.settings_rect, border_radius=8)
        settings_text = self.font.render("SETTINGS", True, (255, 255, 255))
        self.screen.blit(settings_text, (self.settings_rect.centerx - settings_text.get_width() // 2, self.settings_rect.centery - settings_text.get_height() // 2))

        pygame.display.flip()