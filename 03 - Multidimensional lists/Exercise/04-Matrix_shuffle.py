def is_valid(command, tokens):
    if command != 'swap' or len(tokens) != 4:
        return False

    row1, col1, row2, col2 = map(int, tokens)
    if (0 <= row1 and row2 < rows) and (0 <= col1 and col2 < cols):
        return True


def swap_values(matrix, tokens):
    row1, col1, row2, col2 = map(int, tokens)

    temp = matrix[row1][col1]
    matrix[row1][col1] = matrix[row2][col2]
    matrix[row2][col2] = temp

    return matrix


rows, cols = map(int, input().split())
matrix = [input().split() for _ in range(rows)]

while True:
    tokens = input().split()
    command = tokens[0]

    if command == 'END':
        break

    if not is_valid(command, tokens[1:]):
        print('Invalid input!')
        continue

    matrix = swap_values(matrix, tokens[1:])
    print('\n'.join([' '.join(row) for row in matrix]))
