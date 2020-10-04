def get_bomb_perimeter(i, j):
    if i - 1 >= 0:
        start_row = i - 1
    else:
        start_row = i
    if i + 1 < size:
        end_row = i + 1
    else:
        end_row = i
    if j - 1 >= 0:
        start_col = j - 1
    else:
        start_col = j
    if j + 1 < size:
        end_col = j + 1
    else:
        end_col = j

    return start_row, end_row, start_col, end_col


def explosion(matrix, bomb_coordinate_i, bomb_coordinate_j):
    bomb = matrix[bomb_coordinate_i][bomb_coordinate_j]
    start_i, end_i, start_j, end_j = get_bomb_perimeter(bomb_coordinate_i, bomb_coordinate_j)

    if bomb > 0:
        for i in range(start_i, end_i + 1):
            for j in range(start_j, end_j + 1):
                if matrix[i][j] > 0:
                    matrix[i][j] -= bomb
    return matrix


size = int(input())
matrix = [list(map(int, input().split())) for _ in range(size)]
bombs = [map(int, bomb.split(',')) for bomb in input().split()]

for bomb in bombs:
    if size > 0:
        bomb_coordinate_i, bomb_coordinate_j = bomb
        matrix = explosion(matrix, bomb_coordinate_i, bomb_coordinate_j)


positive_matrix = [value for row in matrix for value in row if value > 0]

print(f'Alive cells: {len(positive_matrix)}')
print(f'Sum: {sum(positive_matrix)}')
print('\n'.join([' '.join(map(str, cell)) for cell in matrix]))
