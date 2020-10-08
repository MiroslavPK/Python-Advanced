def func_executor(*args):
    results = []
    for function in args:
        fnc = function[0]
        nums = function[1]
        results.append(fnc(*nums))
    return results


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
