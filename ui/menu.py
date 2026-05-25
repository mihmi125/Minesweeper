import pygame
import config


class Menu:
    def __init__(self, change_state_callback):
        self.screen = pygame.display.set_mode((config.SCR_WIDTH, config.SCR_HEIGHT))
        self.change_state_callback = change_state_callback

        self.start_btn = pygame.Rect(300, 200, 200, 50)
        self.settings_btn = pygame.Rect(300, 300, 200, 50)

        self.font = pygame.font.SysFont("Arial", 24)

    def events_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.start_btn.collidepoint(event.pos):
                    self.change_state_callback("GAME")
                elif self.settings_btn.collidepoint(event.pos):
                    self.change_state_callback("SETTINGS")
        return None

    def update_display(self):
        self.screen.fill((40, 40, 60))

        pygame.draw.rect(self.screen, (50, 150, 50), self.start_btn)
        start_text = self.font.render("Start Game", True, (255, 255, 255))
        self.screen.blit(start_text, (self.start_btn.x + 45, self.start_btn.y + 12))

        pygame.draw.rect(self.screen, (100, 100, 100), self.settings_btn)
        settings_text = self.font.render("Settings", True, (255, 255, 255))
        self.screen.blit(settings_text, (self.settings_btn.x + 55, self.settings_btn.y + 12))

        pygame.display.flip()