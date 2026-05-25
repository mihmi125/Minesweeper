import pygame
import config


class Settings:
    def __init__(self, change_state_callback):
        self.screen = pygame.display.set_mode((config.SCR_WIDTH, config.SCR_HEIGHT))
        self.change_state_callback = change_state_callback

        self.back_btn = pygame.Rect(300, 400, 200, 50)
        self.font = pygame.font.SysFont("Arial", 24)

    def events_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.back_btn.collidepoint(event.pos):
                    self.change_state_callback("MENU")
        return None

    def update_display(self):
        self.screen.fill((60, 40, 40))

        title_text = self.font.render("Settings Menu (Placeholder)", True, (255, 255, 255))
        self.screen.blit(title_text, (260, 200))

        pygame.draw.rect(self.screen, (150, 50, 50), self.back_btn)
        back_text = self.font.render("Back to Menu", True, (255, 255, 255))
        self.screen.blit(back_text, (self.back_btn.x + 40, self.back_btn.y + 12))

        pygame.display.flip()