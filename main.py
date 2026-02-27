import pygame
import sys
from ui.constants import TILE_SIZE, FPS, init_fonts
from ui.input_box import InputController
from ui.renderer import GameRenderer
from game.state import GameState

def main():
    pygame.init()
    init_fonts()

    # Game Config
    width_tiles = 20
    height_tiles = 12
    screen_width = width_tiles * TILE_SIZE
    screen_height = (height_tiles * TILE_SIZE) + 120

    # Initialize Modules (Wiring dependencies)
    renderer = GameRenderer(screen_width, screen_height)
    game_state = GameState(width_tiles, height_tiles)
    
    # Input box setup for the START screen
    default_inputs = {
        "m00": "7", "m01": "2",
        "m10": "3", "m11": "109",
        "mod": "594"
    }
    input_ctrl = InputController(default_inputs)
    
    clock = pygame.time.Clock()
    running = True

    while running:
        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if game_state.state == "START":
                if input_ctrl.handle_event(event): # Returns True on ENTER key
                    # Extract matrix and mod
                    try:
                        matrix = [
                            [int(input_ctrl.inputs["m00"]), int(input_ctrl.inputs["m01"])],
                            [int(input_ctrl.inputs["m10"]), int(input_ctrl.inputs["m11"])]
                        ]
                        mod = int(input_ctrl.inputs["mod"]) if input_ctrl.inputs["mod"] else 594
                    except ValueError:
                        matrix = [[7, 2], [3, 109]]
                        mod = 594
                    game_state.start_game(matrix, mod)
            
            elif game_state.state == "PLAYING":
                if event.type == pygame.KEYDOWN:
                    dx, dy = 0, 0
                    if event.key in [pygame.K_UP, pygame.K_w]: dy = -1
                    if event.key in [pygame.K_DOWN, pygame.K_s]: dy = 1
                    if event.key in [pygame.K_LEFT, pygame.K_a]: dx = -1
                    if event.key in [pygame.K_RIGHT, pygame.K_d]: dx = 1
                    
                    if dx != 0 or dy != 0:
                        game_state.process_move(dx, dy)
            
            elif game_state.state in ["WON", "LOST"]:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    game_state.state = "START"

        # Rendering
        if game_state.state == "START":
            renderer.draw_start_screen(input_ctrl)
        else:
            renderer.draw_game_screen(game_state)

        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
