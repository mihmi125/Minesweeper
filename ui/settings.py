import pygame
import config


class Settings:
    def __init__(self, change_state_callback):
        self.screen = pygame.display.set_mode((config.SCR_WIDTH, config.SCR_HEIGHT))
        self.change_state_callback = change_state_callback

        self.font = pygame.font.SysFont("Arial", 24)
        self.title_font = pygame.font.SysFont("Arial", 32)

        self.presets = [
            {"label": "Small (8x8 - 12 Mines)", "rows": 8, "cols": 8, "mines": 12, "rect": pygame.Rect(250, 180, 300, 40)},
            {"label": "Medium (12x12 - 30 Mines)", "rows": 12, "cols": 12, "mines": 30, "rect": pygame.Rect(250, 240, 300, 40)},
            {"label": "Large (16x16 - 60 Mines)", "rows": 16, "cols": 16, "mines": 60, "rect": pygame.Rect(250, 300, 300, 40)}
        ]

        self.back_btn = pygame.Rect(300, 420, 200, 50)

    def events_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for preset in self.presets:
                    if preset["rect"].collidepoint(event.pos):
                        config.GRID_ROWS = preset["rows"]
                        config.GRID_COLS = preset["cols"]
                        config.MINE_COUNT = preset["mines"]

                if self.back_btn.collidepoint(event.pos):
                    self.change_state_callback("MENU")
        return None

    def update_display(self):
        self.screen.fill((40, 45, 50))

        title_text = self.title_font.render("Select Board Difficulty", True, (255, 255, 255))
        self.screen.blit(title_text, (config.SCR_WIDTH // 2 - title_text.get_width() // 2, 80))

        for preset in self.presets:
            is_active = (config.GRID_ROWS == preset["rows"] and config.MINE_COUNT == preset["mines"])
            btn_color = (46, 204, 113) if is_active else (100, 110, 120)

            pygame.draw.rect(self.screen, btn_color, preset["rect"], border_radius=6)

            lbl = self.font.render(preset["label"], True, (255, 255, 255))
            self.screen.blit(lbl, (preset["rect"].x + (preset["rect"].width // 2 - lbl.get_width() // 2), preset["rect"].y + 8))

        pygame.draw.rect(self.screen, (150, 50, 50), self.back_btn, border_radius=6)
        back_text = self.font.render("Back to Menu", True, (255, 255, 255))
        self.screen.blit(back_text, (self.back_btn.x + (self.back_btn.width // 2 - back_text.get_width() // 2), self.back_btn.y + 12))

        pygame.display.flip()