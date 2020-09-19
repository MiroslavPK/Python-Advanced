n = int(input())
stack = []

for _ in range(n):
    tokens = input().split()
    command = int(tokens[0])

    if command == 1:
        stack.append(int(tokens[1]))

    if stack:
        if command == 2:
            stack.pop()

        elif command == 3:
            print(max(stack))

        elif command == 4:
            print(min(stack))

print(', '.join(map(str, reversed(stack))))
