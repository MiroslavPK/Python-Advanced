string = list(input())
reversed_string = ''

while string:
    reversed_string += string.pop()

print(reversed_string)
