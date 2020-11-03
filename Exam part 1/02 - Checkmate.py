def find_king():
    king = [[i, row_elements.index('K')] for i, row_elements in enumerate(matrix) if 'K' in row_elements]
    return king[0]


def find_queens():
    queens = []
    for i, row_elements in enumerate(matrix):
        if 'Q' in row_elements:
            for j in range(len(row_elements)):
                if matrix[i][j] == 'Q':
                    queens.append([i, j])
    return queens


def get_direction():
    new_direction = ""
    queen_x, queen_y = queen[0], queen[1]
    king_x, king_y = king_pos[0], king_pos[1]

    if queen_y == king_y:
        if queen_x > king_x:
            new_direction = "up"
        elif queen_x < king_x:
            new_direction = "down"
    elif queen_x == king_x:
        if queen_y > king_y:
            new_direction = "left"
        elif queen_y < king_y:
            new_direction = "right"
    elif queen_x > king_x and queen_y > king_y:
        new_direction = "left up"
    elif queen_x > king_x and queen_y < king_y:
        new_direction = "right up"
    elif queen_x < king_x and queen_y > king_y:
        new_direction = "left down"
    elif queen_x < king_x and queen_y < king_y:
        new_direction = "right down"

    return new_direction


matrix = [input().split(' ') for _ in range(8)]

king_pos = find_king()
queen_pos = find_queens()

king_enemies = []
queen_directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left":  (0, -1),
    "right": (0, 1),
    "left up": (-1, -1),
    "right up": (-1, 1),
    "left down": (1, -1),
    "right down": (1, 1),
}

for queen in queen_pos:
    row, col = queen[0], queen[1]
    direction = get_direction()

    current_row, current_col = row, col
    for _ in range(8):
        new_row, new_col = current_row + queen_directions[direction][0], current_col + queen_directions[direction][1]

        if 8 > new_row >= 0 and 8 > new_row >= 0:
            current_row, current_col = new_row, new_col
            if matrix[current_row][current_col] == 'Q':
                break
            elif matrix[current_row][current_col] == 'K':
                king_enemies.append([row, col])
                break

if len(king_enemies) > 0:
    [print(queen) for queen in king_enemies]
else:
    print('The king is safe!')
