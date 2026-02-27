def det2(matrix):
    """Calculate the determinant of a 2x2 matrix."""
    if len(matrix) != 2 or len(matrix[0]) != 2 or len(matrix[1]) != 2:
        raise ValueError("Input must be a 2x2 matrix.")

    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def op_det2(matrix):
    """Tính định thức đối của ma trận 2x2."""
    if len(matrix) != 2 or len(matrix[0]) != 2 or len(matrix[1]) != 2:
        raise ValueError("Input must be a 2x2 matrix.")

    return matrix[0][1] * matrix[1][0] - matrix[0][0] * matrix[1][1]


seed_matrix = [[7, 2],
               [3, 109]]  # ma trận tuần hoàn lặp lại

# Thêm cặp vector (x0,y0) và (x1,y1) vào ma trận result_matrix
result_matrix = seed_matrix.copy()

LOOP = 100
MOD = 594
if __name__ == "__main__":
    for i in range(LOOP):
        # Lấy 2 cột cuối cùng của ma trận result_matrix để tính xi và yi
        new_matrix = [row[len(result_matrix[0])-2:] for row in result_matrix]

        xi = det2(new_matrix)
        xi = xi % 594
        result_matrix[0].append(xi)
        yi = op_det2([[result_matrix[0][i+1], xi],
                      [result_matrix[1][i], result_matrix[1][i+1]]])
        yi = yi % 594
        result_matrix[1].append(yi)
    print(result_matrix)