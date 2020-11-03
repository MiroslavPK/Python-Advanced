from collections import deque


def best_list_pureness(nums, k):
    nums = deque(nums)
    highest_pureness = 0
    count_rotations = 0

    for rotation in range(k + 1):
        pureness = sum([i * num for i, num in enumerate(nums)])
        if pureness > highest_pureness:
            highest_pureness = pureness
            count_rotations = rotation
        nums.rotate(1)

    return f'Best pureness {highest_pureness} after {count_rotations} rotations'
