from itertools import product, chain

numbers = input().split(', ')
n = len(numbers)

combinations = [list(num) for num in product('+-', repeat=n)]

for combination in combinations:
    elems = [''.join(item) for item in list(zip(combination, numbers))]
    expression = ''.join(elems)
    print(f'{expression}={eval(expression)}')
