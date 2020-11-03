def list_manipulator(nums, *args):
    command, place = args[0], args[1]
    new_list = []
    if command == 'add':
        numbers = list(args[2:])
        if place == 'beginning':
            new_list = numbers + nums
        elif place == 'end':
            new_list = nums + numbers
    if command == 'remove':
        if place == 'beginning':
            if len(args) > 2:
                cnt = args[2]
                new_list = nums[cnt:]
            else:
                new_list = nums[1:]
        elif place == 'end':
            if len(args) > 2:
                cnt = args[2]
                finish = len(nums) - cnt
                new_list = nums[:finish]
            else:
                new_list = nums[:-1]

    return new_list


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))


