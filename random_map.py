import random

class SimplePRNG:
    def __init__(self, seed):
        self.state = seed

    def next(self):
        # Linear Congruential Generator (LCG)
        self.state = (1103515245 * self.state + 12345) % (2**31)
        return self.state / (2**31)


def generate_map(width, height, seed):
    prng = SimplePRNG(seed)
    game_map = []

    # Generate base terrain
    for _ in range(height):
        row = []
        for _ in range(width):
            r = prng.next()
            if r < 0.1:
                tile = "~"      # water
            elif r < 0.3:
                tile = "T"      # forest
            else:
                tile = "."      # land
            row.append(tile)
        game_map.append(row)

    # Place Player (P) and Treasure (X) on land ('.')
    def get_random_land_coord():
        while True:
            # Use PRNG for coordinates to keep it seed-deterministic
            x = int(prng.next() * width)
            y = int(prng.next() * height)
            if game_map[y][x] == ".":
                return x, y

    px, py = get_random_land_coord()
    game_map[py][px] = "P"

    tx, ty = get_random_land_coord()
    # Ensure treasure is not on player's spot
    while (tx, ty) == (px, py):
        tx, ty = get_random_land_coord()
    game_map[ty][tx] = "X"

    return game_map, (px, py), (tx, ty)


def print_map(game_map):
    for row in game_map:
        print(" ".join(row))


if __name__ == "__main__":
    m, player_pos, treasure_pos = generate_map(20, 10, seed=42)
    print_map(m)
    print(f"Player at: {player_pos}, Treasure at: {treasure_pos}")