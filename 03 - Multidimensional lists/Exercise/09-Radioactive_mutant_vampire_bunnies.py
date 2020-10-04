def get_player_starting_position(matrix):
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 'P':
                return i, j


def move_player(matrix, direction, row, col):
    if matrix[row][col] != 'B':
        matrix[row][col] = '.'

    if direction == 'L':
            col -= 1
    elif direction == 'R':
            col += 1
    elif direction == 'U':
            row -= 1
    elif direction == 'D':
            row += 1
    player_position = row, col

    return matrix, player_position


def bunnies_positions(matrix):
    bunnies = []
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 'B':
                bunnies.append((i, j))
    return bunnies


def spread_bunny_across(matrix, bunny_coordinates):
    bunnies_multiplying_directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]
    for i, j in bunny_coordinates:
        for add_i, add_j in bunnies_multiplying_directions:
            new_i, new_j = i + add_i, j + add_j

            if 0 <= new_i < rows and 0 <= new_j < cols:
                matrix[new_i][new_j] = 'B'
    return matrix


rows, cols = map(int, input().split())
matrix = [list(input()) for _ in range(rows)]
directions = list(input())

directions.reverse()
player_i, player_j = get_player_starting_position(matrix)
win = False


while directions:
    direction = directions.pop()
    bunnies = bunnies_positions(matrix)
    matrix = spread_bunny_across(matrix, bunnies)
    matrix, player_position = move_player(matrix, direction, player_i, player_j)

    row, col = player_position

    if 0 <= col < cols and 0 <= row < rows:
        player_i, player_j = row, col
    else:
        win = True

    if win:
        if matrix[player_i][player_j] != 'B':
            matrix[player_i][player_j] = '.'
        print('\n'.join([''.join(map(str, row)) for row in matrix]))
        print(f'won: {player_i} {player_j}')
        break

    if matrix[player_i][player_j] == 'B':
        print('\n'.join([''.join(map(str, row)) for row in matrix]))
        print(f'dead: {player_i} {player_j}')
        break
