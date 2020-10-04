def get_squares(matrix):
    squares = []
    for i in range(rows - 1):
        for j in range(cols - 1):
            square = [
                matrix[i][j], matrix[i][j + 1], matrix[i + 1][j], matrix[i + 1][j + 1]
            ]
            squares.append(square)
    return squares


def check_2x2_squares(squares):
    squares_2x2 = 0
    for square in squares:
        checker = square[0]
        dup_elements_cnt = tuple(square).count(checker)
        if dup_elements_cnt == len(square):
            squares_2x2 += 1
    print(squares_2x2)


rows, cols = map(int, input().split())
matrix = [list(input().split()) for _ in range(rows)]

squares = get_squares(matrix)
check_2x2_squares(squares)
