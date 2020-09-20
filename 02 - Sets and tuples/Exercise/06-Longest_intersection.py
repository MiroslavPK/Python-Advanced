n = int(input())

intersect = set()

for _ in range(n):
    first, second = input().split('-')
    first_start, first_end = map(int, first.split(','))
    second_start, second_end = map(int, second.split(','))

    first_set = set(range(first_start, first_end + 1))
    second_set = set(range(second_start, second_end + 1))

    current_intersection = first_set & second_set
    if len(intersect) < len(current_intersection):
        intersect = current_intersection

print(f'Longest intersection is [{", ".join(map(str, intersect))}] with length {len(intersect)}')


# another solution with nested loop
# n = int(input())
# first_set = set()
# second_set = set()
# intersect = set()
#
# for _ in range(n):
#     first, second = input().split('-')
#     first_start, first_end = map(int, first.split(','))
#     second_start, second_end = map(int, second.split(','))
#
#     first_set.clear()
#     second_set.clear()
#
#     for i in range(min(first_start, second_start), max(first_end + 1, second_end + 1)):
#         if first_start <= i <= first_end:
#             first_set.add(i)
#         if second_start <= i <= second_end:
#             second_set.add(i)
#
#         current_intersection = first_set & second_set
#         if len(intersect) < len(current_intersection):
#             intersect = current_intersection
#
# print(f'Longest intersection is [{", ".join(map(str, intersect))}] with length {len(intersect)}')
