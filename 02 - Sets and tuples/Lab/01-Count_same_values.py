# from collections import defaultdict
# numbers_occurrences = defaultdict(int)
numbers = map(float, input().split())
numbers_occurrences = {}

for num in numbers:
    if num not in numbers_occurrences:
        numbers_occurrences[num] = 0
    numbers_occurrences[num] += 1

for num, occurrences in numbers_occurrences.items():
    print(f'{num} - {occurrences} times')
