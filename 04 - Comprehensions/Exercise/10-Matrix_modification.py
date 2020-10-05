size = int(input())
matrix = [list(map(int, input().split())) for _ in range(size)]

while True:
    tokens = input()
    if tokens == 'END':
        print('\n'.join(' '.join(map(str, row)) for row in matrix))
        break

    command, row, col, value = tokens.split()
    row, col, value = int(row), int(col), int(value)
    if 0 > (row or col) or size <= (row or col):
        print('Invalid coordinates')
        continue

    if command == 'Add':
        matrix[row][col] += value
    elif command == 'Subtract':
        matrix[row][col] -= value
