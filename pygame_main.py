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
        self.screen_height = (self.height_tiles * TILE_SIZE) + 100 # Extra space for UI
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Seed Explorer - 🌊🌳🟩")
        
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = "START" # START, PLAYING, WON, LOST
        self.last_message = ""
        self.steps = 0
        
        # Font setup - Segoe UI Emoji is best for Windows
        try:
            self.emoji_font = pygame.font.SysFont("Segoe UI Emoji", TILE_SIZE - 10)
            self.ui_font = pygame.font.SysFont("Arial", 24)
        except:
            self.emoji_font = pygame.font.SysFont(None, TILE_SIZE - 10)
            self.ui_font = pygame.font.SysFont(None, 24)

        self.seed_text = "42"
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
            seed = int(self.seed_text)
        except ValueError:
            seed = 42
        
        self.map_data, self.player_pos, self.treasure_pos = generate_map(self.width_tiles, self.height_tiles, seed)
        self.steps = 0
        self.state = "PLAYING"
        self.last_message = "Exploring the wild..."

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if self.state == "START":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.start_game()
                    elif event.key == pygame.K_BACKSPACE:
                        self.seed_text = self.seed_text[:-1]
                    else:
                        if event.unicode.isdigit():
                            self.seed_text += event.unicode
            
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
                        self.seed_text = ""

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
            title = self.ui_font.render("SEED EXPLORER", True, COLOR_TEXT)
            prompt = self.ui_font.render(f"Enter Seed: {self.seed_text}_", True, COLOR_TEXT)
            hint = self.ui_font.render("Press ENTER to Start", True, (150, 150, 150))
            
            self.screen.blit(title, (self.screen_width // 2 - title.get_width() // 2, 100))
            self.screen.blit(prompt, (self.screen_width // 2 - prompt.get_width() // 2, 200))
            self.screen.blit(hint, (self.screen_width // 2 - hint.get_width() // 2, 300))

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
