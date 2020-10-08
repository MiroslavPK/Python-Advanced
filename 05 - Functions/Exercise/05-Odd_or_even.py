def odd_or_even(command, nums):
    if command == 'Even':
        print(sum(num for num in nums if num % 2 == 0)*len(nums))
    else:
        print(sum(num for num in nums if num % 2 != 0) * len(nums))


command = input()
nums = list(map(int, input().split()))
odd_or_even(command, nums)
