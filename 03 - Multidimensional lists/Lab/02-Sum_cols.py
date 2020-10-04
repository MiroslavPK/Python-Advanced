rows, cols = input().split(', ')

matrix = [list(map(int, input().split())) for _ in range(int(rows))]

for col in zip(*matrix):
    print(sum(col))


# for j in range(int(cols)):
#     col_sum = 0
#     for row in matrix:
#         col_sum += row[j]
#     print(col_sum)
