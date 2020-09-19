from collections import deque

queue = deque()

while True:
    entry = input()
    if entry == 'End':
        print(f'{len(queue)} people remaining.')
        break
    if entry == 'Paid':
        while queue:
            print(f'{queue.popleft()}')
        continue
    queue.append(entry)
