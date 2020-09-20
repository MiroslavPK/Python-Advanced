n_guests = int(input())
guests = set()
attendees = set()

for _ in range(n_guests):
    guests.add(input())

while True:
    command = input()
    if command == 'END':
        break

    attendees.add(command)
    # guests.remove(command)

guests -= attendees
print(len(guests))
print('\n'.join(sorted(guests)))
