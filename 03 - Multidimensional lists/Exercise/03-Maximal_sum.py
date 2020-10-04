from itertools import chain


def get_rectangles(matrix):
    rectangles = []
    for i in range(rows - 2):
        for j in range(cols - 2):
            rectangle = [
                [matrix[i][j], matrix[i][j + 1], matrix[i][j + 2]],
                [matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2]],
                [matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]],
            ]
            rectangles.append(rectangle)
    return rectangles


def get_max_rectangle(rectangles):
    max_rectangle = []
    max_sum = None
    for rectangle in rectangles:
        total = get_rectangle_sum(rectangle)
        if max_sum is None or total > max_sum:
            max_sum = total
            max_rectangle = rectangle
    return max_rectangle


def get_rectangle_sum(rectangle):
    return sum(chain(*rectangle))


rows, cols = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(rows)]

rectangles = get_rectangles(matrix)
rectangle = get_max_rectangle(rectangles)

print(f'Sum = {get_rectangle_sum(rectangle)}')
print('\n'.join([' '.join(map(str, row)) for row in rectangle]))
