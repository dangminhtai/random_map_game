def det2(matrix):
    """Tính định thức của ma trận 2x2."""
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def op_det2(matrix):
    """Tính định thức đối của ma trận 2x2."""
    return matrix[0][1] * matrix[1][0] - matrix[0][0] * matrix[1][1]


class MatrixPRNG:
    def __init__(self, matrix=None, mod=594):
        if matrix:
            self.result_matrix = [list(row) for row in matrix]
        else:
            self.result_matrix = [[7, 2], [3, 109]]
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
            
            i = self.count
            yi = op_det2([[self.result_matrix[0][i+1], xi],
                          [self.result_matrix[1][i], self.result_matrix[1][i+1]]]) % self.mod
            self.result_matrix[1].append(yi)
            
            self.queue.extend([xi, yi])
            self.count += 1

        val = self.queue.pop(0)
        return val / self.mod
