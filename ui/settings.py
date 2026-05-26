import pygame
import config

class Settings:
    def __init__(self, screen, change_state_callback):
        self.screen = screen
        self.change_state_callback = change_state_callback

        self.font = pygame.font.SysFont("Arial", 24)
        self.btn_font = pygame.font.SysFont("Arial", 30)
        self.title_font = pygame.font.SysFont("Arial", 50)

        # Left Column: Presets (from Version 1)
        self.presets = [
            {"label": "Small (8x8 - 12 Mines)", "rows": 8, "cols": 8, "mines": 12, "rect": pygame.Rect(80, 180, 280, 45)},
            {"label": "Medium (12x12 - 30 Mines)", "rows": 12, "cols": 12, "mines": 30, "rect": pygame.Rect(80, 250, 280, 45)},
            {"label": "Large (16x16 - 60 Mines)", "rows": 16, "cols": 16, "mines": 60, "rect": pygame.Rect(80, 320, 280, 45)}
        ]

        # Right Column: Custom Incremental Control Bounds (from Version 2)
        self.row_minus = pygame.Rect(620, 180, 40, 40)
        self.row_plus = pygame.Rect(720, 180, 40, 40)

        self.col_minus = pygame.Rect(620, 250, 40, 40)
        self.col_plus = pygame.Rect(720, 250, 40, 40)

        self.mine_minus = pygame.Rect(620, 320, 40, 40)
        self.mine_plus = pygame.Rect(720, 320, 40, 40)

        # Centered Back navigation layout
        self.back_btn = pygame.Rect(config.SCR_WIDTH // 2 - 100, 460, 200, 50)

    def events_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = event.pos

                # 1. Process Preset buttons
                for preset in self.presets:
                    if preset["rect"].collidepoint(pos):
                        config.GRID_ROWS = preset["rows"]
                        config.GRID_COLS = preset["cols"]
                        config.MINE_COUNT = preset["mines"]

                # 2. Process Manual Fine-Tuning Incrementals with Safety Boundary Checks
                # Row Checks
                if self.row_minus.collidepoint(pos):
                    if config.GRID_ROWS > 3:
                        config.GRID_ROWS -= 1
                        if config.MINE_COUNT >= config.GRID_ROWS * config.GRID_COLS:
                            config.MINE_COUNT = (config.GRID_ROWS * config.GRID_COLS) - 1
                elif self.row_plus.collidepoint(pos):
                    if config.GRID_ROWS < 18:
                        config.GRID_ROWS += 1

                # Column Checks
                elif self.col_minus.collidepoint(pos):
                    if config.GRID_COLS > 3:
                        config.GRID_COLS -= 1
                        if config.MINE_COUNT >= config.GRID_ROWS * config.GRID_COLS:
                            config.MINE_COUNT = (config.GRID_ROWS * config.GRID_COLS) - 1
                elif self.col_plus.collidepoint(pos):
                    if config.GRID_COLS < 24:
                        config.GRID_COLS += 1

                # Mine Multipliers Constraints
                elif self.mine_minus.collidepoint(pos):
                    if config.MINE_COUNT > 1:
                        config.MINE_COUNT -= 1
                elif self.mine_plus.collidepoint(pos):
                    if config.MINE_COUNT < (config.GRID_ROWS * config.GRID_COLS) - 1:
                        config.MINE_COUNT += 1

                # 3. Handle Navigation Exit Back
                if self.back_btn.collidepoint(pos):
                    self.change_state_callback("MENU")
        return None

    def update_display(self):
        self.screen.fill((40, 40, 40))

        # Title
        title_text = self.title_font.render("SETTINGS", True, (255, 255, 255))
        self.screen.blit(title_text, (config.SCR_WIDTH // 2 - title_text.get_width() // 2, 60))

        # Draw Left Side: Presets
        preset_header = self.btn_font.render("Quick Presets", True, (200, 200, 200))
        self.screen.blit(preset_header, (80, 130))

        for preset in self.presets:
            is_active = (config.GRID_ROWS == preset["rows"] and 
                        config.GRID_COLS == preset["cols"] and 
                        config.MINE_COUNT == preset["mines"]
                        )
            btn_color = (46, 204, 113) if is_active else (100, 110, 120)

            pygame.draw.rect(self.screen, btn_color, preset["rect"], border_radius=6)
            lbl = self.font.render(preset["label"], True, (255, 255, 255))
            self.screen.blit(lbl, (preset["rect"].centerx - lbl.get_width() // 2, preset["rect"].centery - lbl.get_height() // 2))

        # Draw Right Side: Custom Controls
        custom_header = self.btn_font.render("Manual Tuning", True, (200, 200, 200))
        self.screen.blit(custom_header, (450, 130))

        labels = [
            ("Rows:", config.GRID_ROWS, 180, self.row_minus, self.row_plus),
            ("Columns:", config.GRID_COLS, 250, self.col_minus, self.col_plus),
            ("Mines:", config.MINE_COUNT, 320, self.mine_minus, self.mine_plus)
        ]

        for label_text, val, y_pos, btn_minus, btn_plus in labels:
            lbl = self.font.render(label_text, True, (255, 255, 255))
            self.screen.blit(lbl, (450, y_pos + 8))

            # Draw Minus button
            pygame.draw.rect(self.screen, (150, 50, 50), btn_minus, border_radius=5)
            m_txt = self.btn_font.render("-", True, (255, 255, 255))
            self.screen.blit(m_txt, (btn_minus.centerx - m_txt.get_width() // 2, btn_minus.centery - m_txt.get_height() // 2 - 2))

            # Display Value Integer
            val_txt = self.btn_font.render(str(val), True, (255, 255, 255))
            self.screen.blit(val_txt, (680 - val_txt.get_width() // 2, y_pos + 5))

            # Draw Plus button
            pygame.draw.rect(self.screen, (50, 150, 50), btn_plus, border_radius=5)
            p_txt = self.btn_font.render("+", True, (255, 255, 255))
            self.screen.blit(p_txt, (btn_plus.centerx - p_txt.get_width() // 2, btn_plus.centery - p_txt.get_height() // 2 - 2))

        # Back Button Navigation
        pygame.draw.rect(self.screen, (100, 100, 100), self.back_btn, border_radius=6)
        back_text = self.btn_font.render("BACK", True, (255, 255, 255))
        self.screen.blit(back_text, (self.back_btn.centerx - back_text.get_width() // 2, self.back_btn.centery - back_text.get_height() // 2))

        pygame.display.flip()