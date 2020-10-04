from itertools import chain


def get_starting_position(matrix):
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == 's':
                return i, j


def count_coals(matrix):
    tmp = tuple(chain(*matrix))
    coals = tmp.count('c')
    return coals


def check_direction(direction, row, col):
    if direction == 'left':
        if col - 1 >= 0:
            col -= 1
    if direction == 'right':
        if col + 1 < size:
            col += 1
    if direction == 'up':
        if row - 1 >= 0:
            row -= 1
    if direction == 'down':
        if row + 1 < size:
            row += 1
    return row, col


def move(matrix, row, col):
    game_over = False
    if matrix[row][col] == 'c':
        matrix[row][col] = '*'
    elif matrix[row][col] == 'e':
        game_over = True
    return game_over


size = int(input())
directions = input().split()
matrix = [input().split() for _ in range(size)]

directions.reverse()
row_index, col_index = get_starting_position(matrix)

while directions:
    direction = directions.pop()
    row, col = check_direction(direction, row_index, col_index)
    if (row, col) == (row_index, col_index):
        continue

    row_index, col_index = row, col
    game_over = move(matrix, row_index, col_index)
    coals = count_coals(matrix)

    if coals == 0:
        print(f'You collected all coals! ({row_index}, {col_index})')
        break

    if game_over:
        print(f'Game over! ({row_index}, {col_index})')
        break

    if not directions:
        print(f'{coals} coals left. ({row_index}, {col_index})')
