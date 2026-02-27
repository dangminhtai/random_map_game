from random_map import MatrixPRNG, det2, op_det2

def test_comparison():
    # User's logic from dds.py
    seed_matrix = [[7, 2],
                   [3, 109]]
    
    # We simulate 2 steps of the user's logic
    # Step 1
    new_matrix_1 = [row[-2:] for row in seed_matrix]
    x1 = det2(new_matrix_1) % 594
    y1 = op_det2([[seed_matrix[0][1], x1],
                  [seed_matrix[1][0], seed_matrix[1][1]]]) % 594
    
    print(f"User Logic Step 1: x={x1}, y={y1}")

    # MatrixPRNG implementation
    # We manually set the result_matrix to match user's seed_matrix
    prng = MatrixPRNG(7)
    prng.result_matrix = [[7, 2], [3, 109]]
    
    v1 = int(prng.next() * 594)
    v2 = int(prng.next() * 594)
    
    print(f"MatrixPRNG Step 1: x={v1}, y={v2}")
    
    assert x1 == v1
    assert y1 == v2
    print("Test Passed: Logic matches dds.py!")

if __name__ == "__main__":
    test_comparison()
