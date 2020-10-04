def find_in_matrix(matrix, search):
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col == search:
                return i, j


size = int(input())
matrix = [list(input()) for _ in range(size)]
search = input()

found = find_in_matrix(matrix, search)

if not found:
    print(f'{search} does not occur in the matrix')
else:
    print(found)
