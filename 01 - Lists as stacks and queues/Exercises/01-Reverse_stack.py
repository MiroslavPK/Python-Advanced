stack = input().split()
rev_stack = []

while stack:
    rev_stack.append(stack.pop())

print(' '.join(rev_stack))
