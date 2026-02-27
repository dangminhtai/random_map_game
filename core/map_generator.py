from .prng import MatrixPRNG

def generate_map(width, height, matrix=None, mod=594):
    prng = MatrixPRNG(matrix=matrix, mod=mod)
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
