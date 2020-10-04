size = int(input())

matrix = [list(map(int, input().split())) for _ in range(size)]
total = [matrix[i][i] for i in range(size)]

print(total)
