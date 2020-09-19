expr = input()
stack = []

for char in range(len(expr)):
    if expr[char] == '(':
        stack.append(char)

    if expr[char] == ')':
        start = stack.pop()
        print(expr[start: char + 1])
