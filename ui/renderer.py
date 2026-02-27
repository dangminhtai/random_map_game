import pygame
from .constants import (
    COLOR_BG, COLOR_TEXT, COLOR_HINT, COLOR_SUCCESS, COLOR_WIN_TEXT, COLOR_LOSE_TEXT,
    TILES, FONTS, TILE_SIZE
)

class GameRenderer:
    def __init__(self, screen_width, screen_height):
        # We assume pygame.init() and init_fonts() have been called in main.py
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Seed Explorer - Advanced Matrix SRP Mode")

    def draw_start_screen(self, input_controller):
        self.screen.fill(COLOR_BG)
        
        title = FONTS["ui"].render("ADVANCED MATRIX SEEDER", True, COLOR_SUCCESS)
        self.screen.blit(title, (self.screen_width // 2 - title.get_width() // 2, 40))

        mx, my = self.screen_width // 2 - 100, 100
        cell_w, cell_h = 80, 40
        
        for i in range(2):
            for j in range(2):
                field = f"m{i}{j}"
                rect = pygame.Rect(mx + j * (cell_w + 10), my + i * (cell_h + 10), cell_w, cell_h)
                
                pygame.draw.rect(self.screen, input_controller.get_color(field), rect, 2)
                val_surf = FONTS["ui"].render(input_controller.inputs[field], True, COLOR_TEXT)
                self.screen.blit(val_surf, (rect.x + 5, rect.y + 5))

        mod_label = FONTS["small"].render("MODULUS:", True, COLOR_HINT)
        self.screen.blit(mod_label, (mx, my + 110))
        mod_rect = pygame.Rect(mx + 90, my + 105, 100, 40)
        
        pygame.draw.rect(self.screen, input_controller.get_color("mod"), mod_rect, 2)
        mod_surf = FONTS["ui"].render(input_controller.inputs["mod"], True, COLOR_TEXT)
        self.screen.blit(mod_surf, (mod_rect.x + 5, mod_rect.y + 5))

        hint1 = FONTS["small"].render("TAB to switch fields", True, COLOR_DIM if 'COLOR_DIM' in globals() else (120, 120, 120))
        hint2 = FONTS["ui"].render("Press ENTER to Start Exploration", True, COLOR_TEXT)
        self.screen.blit(hint1, (self.screen_width // 2 - hint1.get_width() // 2, my + 160))
        self.screen.blit(hint2, (self.screen_width // 2 - hint2.get_width() // 2, my + 200))

        pygame.display.flip()

    def draw_game_screen(self, game_state):
        self.screen.fill(COLOR_BG)

        # Draw Map
        for y, row in enumerate(game_state.map_data):
            for x, char in enumerate(row):
                emoji = TILES.get(char, " ")
                surf = FONTS["emoji"].render(emoji, True, COLOR_TEXT)
                rect = surf.get_rect(center=(x * TILE_SIZE + TILE_SIZE // 2, y * TILE_SIZE + TILE_SIZE // 2))
                self.screen.blit(surf, rect)

        # Draw UI area
        ui_y = game_state.height_tiles * TILE_SIZE + 10
        steps_surf = FONTS["ui"].render(f"Steps: {game_state.steps}", True, COLOR_TEXT)
        msg_surf = FONTS["ui"].render(game_state.last_message, True, COLOR_SUCCESS)
        
        self.screen.blit(steps_surf, (10, ui_y))
        self.screen.blit(msg_surf, (10, ui_y + 40))

        if game_state.state == "WON":
            overlay = FONTS["ui"].render("YOU WIN! 💎", True, COLOR_WIN_TEXT)
            self.screen.blit(overlay, (self.screen_width // 2 - overlay.get_width() // 2, ui_y + 10))
        elif game_state.state == "LOST":
            overlay = FONTS["ui"].render("GAME OVER 💧", True, COLOR_LOSE_TEXT)
            self.screen.blit(overlay, (self.screen_width // 2 - overlay.get_width() // 2, ui_y + 10))

        pygame.display.flip()
