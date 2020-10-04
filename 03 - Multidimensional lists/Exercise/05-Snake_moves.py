from collections import deque

rows, cols = map(int, input().split())
snake = deque(input())

for row in range(rows):
    s = ''
    for col in range(cols):
        popped = snake.popleft()
        s += popped
        snake.append(popped)
    if row % 2 == 0:
        print(s)
    else:
        print(s[::-1])
