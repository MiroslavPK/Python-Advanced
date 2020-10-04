def find_knights(matrix):
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == 'K':
                check_knights_in_range(matrix, row, col)


def check_knights_in_range(matrix, row, col):
    knights_in_range = 0
    if row + 2 < size and col + 1 < size:
        if matrix[row + 2][col + 1] == 'K':
            knights_in_range += 1
    if row + 2 < size and col - 1 >= 0:
        if matrix[row + 2][col - 1] == 'K':
            knights_in_range += 1
    if row - 2 >= 0 and col + 1 < size:
        if matrix[row - 2][col + 1] == 'K':
            knights_in_range += 1
    if row - 2 >= 0 and col - 1 >= 0:
        if matrix[row - 2][col - 1] == 'K':
            knights_in_range += 1
    if row + 1 < size and col + 2 < size:
        if matrix[row + 1][col + 2] == 'K':
            knights_in_range += 1
    if row + 1 < size and col - 2 >= 0:
        if matrix[row + 1][col - 2] == 'K':
            knights_in_range += 1
    if row - 1 >= 0 and col + 2 < size:
        if matrix[row - 1][col + 2] == 'K':
            knights_in_range += 1
    if row - 1 >= 0 and col - 2 >= 0:
        if matrix[row - 1][col - 2] == 'K':
            knights_in_range += 1
    if knights_in_range >= 1:
        knights.append([(row, col), knights_in_range])


def remove_knights(knights):
    i, j = list(knights[0][0])
    knights_in_range = knights[0][1]
    if knights_in_range >= 1:
        matrix[i][j] = '0'
        knights = []
        return knights


size = int(input())
matrix = [list(input()) for _ in range(size)]
knights = []
knights_removed = 0

find_knights(matrix)

while knights:
    knights_removed += 1
    knights.sort(key=lambda knights_in_range: -knights_in_range[1])
    knights = remove_knights(knights)
    find_knights(matrix)

print(knights_removed)
