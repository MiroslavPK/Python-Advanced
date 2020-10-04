from itertools import chain
rows, cols = input().split(', ')

matrix = []

for _ in range(int(rows)):
    matrix.append(list(map(int, input().split(', '))))

print(sum(chain(*matrix)))
print(matrix)
