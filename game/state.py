from core.map_generator import generate_map

class GameState:
    def __init__(self, width=20, height=12):
        self.width_tiles = width
        self.height_tiles = height
        
        self.state = "START" # START, PLAYING, WON, LOST
        self.last_message = ""
        self.steps = 0
        
        self.map_data = []
        self.player_pos = (0, 0)
        self.treasure_pos = (0, 0)

    def start_game(self, matrix, mod):
        self.map_data, self.player_pos, self.treasure_pos = generate_map(
            self.width_tiles, self.height_tiles, matrix=matrix, mod=mod
        )
        self.steps = 0
        self.state = "PLAYING"
        self.last_message = "Exploring the matrix..."

    def process_move(self, dx, dy):
        """Updates player position if valid and checks win/loss conditions."""
        if self.state != "PLAYING":
            return

        nx = self.player_pos[0] + dx
        ny = self.player_pos[1] + dy

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

            # Normal Move
            self.map_data[self.player_pos[1]][self.player_pos[0]] = "."
            self.player_pos = (nx, ny)
            self.map_data[ny][nx] = "P"
            self.steps += 1
            self.last_message = "Moving..."
