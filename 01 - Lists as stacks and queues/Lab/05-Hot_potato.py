from collections import deque

queue = deque(input().split())
n_tosses = int(input())

while len(queue) > 1:
    queue.rotate(-n_tosses+1)
    loser = queue.popleft()
    print(f'Removed {loser}')

winner = queue.pop()
print(f'Last is {winner}')
