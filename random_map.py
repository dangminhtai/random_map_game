import random

def det2(matrix):
    """Calculate the determinant of a 2x2 matrix."""
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def op_det2(matrix):
    """Tính định thức đối của ma trận 2x2."""
    return matrix[0][1] * matrix[1][0] - matrix[0][0] * matrix[1][1]


class MatrixPRNG:
    def __init__(self, seed, mod=594):
        # Derive a 2x2 starting matrix from a single seed
        # We use a simple scheme to populate the initial 2x2 matrix
        self.result_matrix = [
            [seed, (seed * 31 + 7) % mod],
            [(seed * 17 + 11) % mod, (seed * 13 + 109) % mod]
        ]
        self.mod = mod
        self.count = 0
        self.queue = []

    def next(self):
        # The algorithm generates pairs (xi, yi), we queue them up
        if not self.queue:
            # Lấy 2 cột cuối cùng của ma trận result_matrix để tính xi và yi
            new_matrix = [row[-2:] for row in self.result_matrix]

            xi = det2(new_matrix) % self.mod
            self.result_matrix[0].append(xi)
            
            # yi uses result_matrix[0][i+1], xi, result_matrix[1][i], result_matrix[1][i+1]
            # Since we just appended xi, it's at result_matrix[0][-1]
            # i+1 is len(result_matrix[0]) - 2
            i = self.count
            yi = op_det2([[self.result_matrix[0][i+1], xi],
                          [self.result_matrix[1][i], self.result_matrix[1][i+1]]]) % self.mod
            self.result_matrix[1].append(yi)
            
            self.queue.extend([xi, yi])
            self.count += 1

        val = self.queue.pop(0)
        return val / self.mod


def generate_map(width, height, seed):
    prng = MatrixPRNG(seed)
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