start = int(input())
end = int(input())

lst = [num for num in range(start, end + 1) if any([num % digit == 0 for digit in range(2, 11)])]
print(lst)
