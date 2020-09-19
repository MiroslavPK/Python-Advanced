from collections import deque

queue = deque()
liters_in_dispenser = int(input())

while True:
    person = input()
    if person == 'Start':
        break
    queue.append(person)

while True:
    command = input()
    if command == 'End':
        print(f'{liters_in_dispenser} liters left')
        break

    if command.isdigit():
        if liters_in_dispenser < int(command):
            print(f'{queue.popleft()} must wait')
        else:
            print(f'{queue.popleft()} got water')
            liters_in_dispenser -= int(command)
    elif 'refill' in command:
        todo = command.split()
        liters_in_dispenser += int(todo[1])
