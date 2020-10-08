from itertools import combinations

names = input().split(', ')
n = int(input())

for comb in combinations(names, n):
    print(', '.join(list(comb)))