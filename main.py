import os
import sys
from random_map import generate_map, print_map

class Game:
    def __init__(self, width=20, height=10):
        self.width = width
        self.height = height
        self.map_data = []
        self.player_pos = (0, 0)
        self.treasure_pos = (0, 0)
        self.steps = 0
        self.running = True
        self.message = "Welcome to Seed Explorer! Find the 'X' (Treasure). Avoid '~' (Water)."

    def start(self):
        try:
            seed_input = input("Enter a Seed (number): ")
            seed = int(seed_input)
        except ValueError:
            print("Invalid seed. Using default 42.")
            seed = 42
        
        self.map_data, self.player_pos, self.treasure_pos = generate_map(self.width, self.height, seed)
        self.game_loop()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def render(self):
        self.clear_screen()
        print(f"--- SEED EXPLORER --- Steps: {self.steps}")
        print_map(self.map_data)
        print(f"\nMessage: {self.message}")
        print("Controls: W (Up), S (Down), A (Left), D (Right), Q (Quit)")

    def handle_input(self):
        action = input("Move: ").lower()
        if action == 'q':
            self.running = False
            return None
        
        move_map = {
            'w': (0, -1),
            's': (0, 1),
            'a': (-1, 0),
            'd': (1, 0)
        }
        return move_map.get(action)

    def update(self, move):
        if not move:
            return

        nx = self.player_pos[0] + move[0]
        ny = self.player_pos[1] + move[1]

        # Check boundaries
        if 0 <= nx < self.width and 0 <= ny < self.height:
            target_tile = self.map_data[ny][nx]

            # Check for Water (Game Over)
            if target_tile == "~":
                self.message = "OH NO! You fell into the water and drowned. GAME OVER."
                self.running = False
                return

            # Check for Win
            if (nx, ny) == self.treasure_pos:
                self.message = f"CONGRATULATIONS! You found the treasure in {self.steps + 1} steps!"
                self.running = False
                # Update map for visual
                self.map_data[self.player_pos[1]][self.player_pos[0]] = "."
                self.player_pos = (nx, ny)
                self.map_data[ny][nx] = "P"
                return

            # Normal Move
            # Clear old pos (assume it becomes land '.')
            # In a more complex game, we'd store the tile beneath the player
            self.map_data[self.player_pos[1]][self.player_pos[0]] = "."
            self.player_pos = (nx, ny)
            self.map_data[ny][nx] = "P"
            self.steps += 1
            self.message = "Moving..."
        else:
            self.message = "Ouch! You hit a wall."

    def game_loop(self):
        while self.running:
            self.render()
            move = self.handle_input()
            self.update(move)
        
        # Final render for result
        self.render()
        print("\nPress Enter to exit.")
        input()

if __name__ == "__main__":
    game = Game()
    game.start()
