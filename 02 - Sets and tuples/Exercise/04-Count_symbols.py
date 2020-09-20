# using tuple for exercise, although string does the job too
text = tuple(input())
chars = set(text)

for char in sorted(chars):
    print(f'{char}: {text.count(char)} time/s')

# another solution using dict
# char_occurrences = {}
#
# for char in text:
#     if char not in char_occurrences:
#         char_occurrences[char] = 0
#     char_occurrences[char] += 1
#
# [print(f'{char}: {occurrences} time/s') for char, occurrences in sorted(char_occurrences.items())]
