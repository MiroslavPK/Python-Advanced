rows, cols = map(int, input().split())

matrix = [[str(chr(i) + chr(j) + chr(i)) for j in range(i, i + cols)] for i in range(97, 97 + rows)]
print('\n'.join([' '.join(row) for row in matrix]))
