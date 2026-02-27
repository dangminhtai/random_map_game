import pygame
import sys
from random_map import generate_map

# Constants
TILE_SIZE = 40
FPS = 30

# Colors
COLOR_BG = (30, 30, 30)
COLOR_TEXT = (255, 255, 255)

class SeedExplorerGUI:
    def __init__(self):
        pygame.init()
        self.width_tiles = 20
        self.height_tiles = 12
        self.screen_width = self.width_tiles * TILE_SIZE
        self.screen_height = (self.height_tiles * TILE_SIZE) + 120 # Extra space for UI
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Seed Explorer - 🌊🌳🟩 (Advanced Matrix Mode)")
        
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = "START" # START, PLAYING, WON, LOST
        self.last_message = ""
        self.steps = 0
        
        # Font setup
        try:
            self.emoji_font = pygame.font.SysFont("Segoe UI Emoji", TILE_SIZE - 10)
            self.ui_font = pygame.font.SysFont("Arial", 24)
            self.small_font = pygame.font.SysFont("Arial", 18)
        except:
            self.emoji_font = pygame.font.SysFont(None, TILE_SIZE - 10)
            self.ui_font = pygame.font.SysFont(None, 24)
            self.small_font = pygame.font.SysFont(None, 18)

        # Matrix and MOD inputs
        self.inputs = {
            "m00": "7", "m01": "2",
            "m10": "3", "m11": "109",
            "mod": "594"
        }
        self.input_order = ["m00", "m01", "m10", "m11", "mod"]
        self.focus_idx = 0

        self.map_data = []
        self.player_pos = (0, 0)
        self.treasure_pos = (0, 0)

        self.tiles = {
            "~": "🌊",
            "T": "🌳",
            ".": "🟩",
            "P": "🚶",
            "X": "💎"
        }

    def start_game(self):
        try:
            matrix = [
                [int(self.inputs["m00"]), int(self.inputs["m01"])],
                [int(self.inputs["m10"]), int(self.inputs["m11"])]
            ]
            mod = int(self.inputs["mod"]) if self.inputs["mod"] else 594
        except ValueError:
            # Fallback to defaults
            matrix = [[7, 2], [3, 109]]
            mod = 594
        
        self.map_data, self.player_pos, self.treasure_pos = generate_map(
            self.width_tiles, self.height_tiles, matrix=matrix, mod=mod
        )
        self.steps = 0
        self.state = "PLAYING"
        self.last_message = "Exploring the matrix..."

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if self.state == "START":
                if event.type == pygame.KEYDOWN:
                    active_field = self.input_order[self.focus_idx]
                    
                    if event.key == pygame.K_RETURN:
                        self.start_game()
                    elif event.key == pygame.K_TAB:
                        self.focus_idx = (self.focus_idx + 1) % len(self.input_order)
                    elif event.key == pygame.K_BACKSPACE:
                        self.inputs[active_field] = self.inputs[active_field][:-1]
                    else:
                        if event.unicode.isdigit():
                            self.inputs[active_field] += event.unicode
            
            elif self.state == "PLAYING":
                if event.type == pygame.KEYDOWN:
                    move = None
                    if event.key in [pygame.K_UP, pygame.K_w]: move = (0, -1)
                    if event.key in [pygame.K_DOWN, pygame.K_s]: move = (0, 1)
                    if event.key in [pygame.K_LEFT, pygame.K_a]: move = (-1, 0)
                    if event.key in [pygame.K_RIGHT, pygame.K_d]: move = (1, 0)
                    
                    if move:
                        self.update_player(move)
            
            elif self.state in ["WON", "LOST"]:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.state = "START"

    def update_player(self, move):
        nx = self.player_pos[0] + move[0]
        ny = self.player_pos[1] + move[1]

        if 0 <= nx < self.width_tiles and 0 <= ny < self.height_tiles:
            target_tile = self.map_data[ny][nx]
            
            if target_tile == "~":
                self.state = "LOST"
                self.last_message = "Drowned in 🌊! Press R to Restart."
                return

            if (nx, ny) == self.treasure_pos:
                self.state = "WON"
                self.last_message = f"Found 💎 in {self.steps + 1} steps! Press R."
                # Visual update
                self.map_data[self.player_pos[1]][self.player_pos[0]] = "."
                self.player_pos = (nx, ny)
                self.map_data[ny][nx] = "P"
                return

            # Move
            self.map_data[self.player_pos[1]][self.player_pos[0]] = "."
            self.player_pos = (nx, ny)
            self.map_data[ny][nx] = "P"
            self.steps += 1
            self.last_message = "Moving..."

    def draw(self):
        self.screen.fill(COLOR_BG)

        if self.state == "START":
            title = self.ui_font.render("ADVANCED MATRIX SEEDER", True, (200, 255, 100))
            self.screen.blit(title, (self.screen_width // 2 - title.get_width() // 2, 40))

            # Draw 2x2 Matrix Input
            mx, my = self.screen_width // 2 - 100, 100
            cell_w, cell_h = 80, 40
            
            for i in range(2):
                for j in range(2):
                    field = f"m{i}{j}"
                    rect = pygame.Rect(mx + j * (cell_w + 10), my + i * (cell_h + 10), cell_w, cell_h)
                    
                    # Focus highlight
                    color = (255, 255, 255) if self.input_order[self.focus_idx] == field else (100, 100, 100)
                    pygame.draw.rect(self.screen, color, rect, 2)
                    
                    val_surf = self.ui_font.render(self.inputs[field], True, COLOR_TEXT)
                    self.screen.blit(val_surf, (rect.x + 5, rect.y + 5))

            # MOD Input
            mod_label = self.small_font.render("MODULUS:", True, (150, 150, 150))
            self.screen.blit(mod_label, (mx, my + 110))
            mod_rect = pygame.Rect(mx + 90, my + 105, 100, 40)
            mod_focus = (self.input_order[self.focus_idx] == "mod")
            pygame.draw.rect(self.screen, (255, 255, 255) if mod_focus else (100, 100, 100), mod_rect, 2)
            mod_surf = self.ui_font.render(self.inputs["mod"], True, COLOR_TEXT)
            self.screen.blit(mod_surf, (mod_rect.x + 5, mod_rect.y + 5))

            hint1 = self.small_font.render("TAB to switch fields", True, (120, 120, 120))
            hint2 = self.ui_font.render("Press ENTER to Start Exploration", True, COLOR_TEXT)
            self.screen.blit(hint1, (self.screen_width // 2 - hint1.get_width() // 2, my + 160))
            self.screen.blit(hint2, (self.screen_width // 2 - hint2.get_width() // 2, my + 200))

        else:
            # Draw Map
            for y, row in enumerate(self.map_data):
                for x, char in enumerate(row):
                    emoji = self.tiles.get(char, " ")
                    surf = self.emoji_font.render(emoji, True, COLOR_TEXT)
                    rect = surf.get_rect(center=(x * TILE_SIZE + TILE_SIZE // 2, y * TILE_SIZE + TILE_SIZE // 2))
                    self.screen.blit(surf, rect)

            # Draw UI area
            ui_y = self.height_tiles * TILE_SIZE + 10
            steps_surf = self.ui_font.render(f"Steps: {self.steps}", True, COLOR_TEXT)
            msg_surf = self.ui_font.render(self.last_message, True, (200, 255, 200))
            
            self.screen.blit(steps_surf, (10, ui_y))
            self.screen.blit(msg_surf, (10, ui_y + 40))

            if self.state == "WON":
                overlay = self.ui_font.render("YOU WIN! 💎", True, (255, 215, 0))
                self.screen.blit(overlay, (self.screen_width // 2 - overlay.get_width() // 2, ui_y + 10))
            elif self.state == "LOST":
                overlay = self.ui_font.render("GAME OVER 💧", True, (255, 50, 50))
                self.screen.blit(overlay, (self.screen_width // 2 - overlay.get_width() // 2, ui_y + 10))

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()

if __name__ == "__main__":
    game = SeedExplorerGUI()
    game.run()
