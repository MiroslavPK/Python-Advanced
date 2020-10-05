size = int(input())
matrix = [list(map(int, input().split(', '))) for _ in range(size)]

primary_diagonal = [matrix[i][i] for i in range(size)]
secondary_diagonal = [matrix[i][size - i - 1] for i in range(size)]

print(f'First diagonal: {", ".join(map(str, primary_diagonal))}. Sum: {sum(primary_diagonal)}')
print(f'Second diagonal: {", ".join(map(str, secondary_diagonal))}. Sum: {sum(secondary_diagonal)}')