size = int(input())

matrix = [list(map(int, input().split())) for _ in range(size)]
primary_sum = 0
secondary_sum = 0

for i in range(size):
    primary_sum += matrix[i][i]
    secondary_sum += matrix[i][size - 1 - i]

print(abs(primary_sum - secondary_sum))
