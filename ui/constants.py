import pygame

# Constants
TILE_SIZE = 40
FPS = 30

# Colors
COLOR_BG = (30, 30, 30)
COLOR_TEXT = (255, 255, 255)
COLOR_HIGHLIGHT = (200, 255, 100)
COLOR_DIM = (100, 100, 100)
COLOR_HINT = (150, 150, 150)
COLOR_SUCCESS = (200, 255, 200)
COLOR_WIN_TEXT = (255, 215, 0)
COLOR_LOSE_TEXT = (255, 50, 50)

# Emojis
TILES = {
    "~": "🌊",
    "T": "🌳",
    ".": "🟩",
    "P": "🚶",
    "X": "💎"
}

# Fonts (Loaded dynamically)
FONTS = {
    "emoji": None,
    "ui": None,
    "small": None
}

def init_fonts():
    # Only initialize fonts after pygame.init()
    try:
        FONTS["emoji"] = pygame.font.SysFont("Segoe UI Emoji", TILE_SIZE - 10)
        FONTS["ui"] = pygame.font.SysFont("Arial", 24)
        FONTS["small"] = pygame.font.SysFont("Arial", 18)
    except:
        FONTS["emoji"] = pygame.font.SysFont(None, TILE_SIZE - 10)
        FONTS["ui"] = pygame.font.SysFont(None, 24)
        FONTS["small"] = pygame.font.SysFont(None, 18)
