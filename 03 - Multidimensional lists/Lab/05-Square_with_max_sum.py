from itertools import chain


def get_squares(matrix):
    squares = []
    for i in range(rows - 1):
        for j in range(cols - 1):
            square = [
                [matrix[i][j], matrix[i][j+1]],
                [matrix[i+1][j], matrix[i+1][j+1]],
            ]
            squares.append(square)
    return squares


def find_max_square(squares):
    sum_max_square = 0
    max_square = []
    for square in squares:
        if sum(chain(*square)) > sum_max_square:
            sum_max_square = sum(chain(*square))
            max_square = square
    return max_square, sum_max_square


rows, cols = map(int, input().split(', '))
matrix = [list(map(int, input().split(', '))) for _ in range(rows)]

squares = get_squares(matrix)
max_square, total = find_max_square(squares)
print('\n'.join([' '.join(map(str, row)) for row in max_square]))
print(total)
