from collections import deque

n_pumps = int(input())
petrol_in_pump = deque()
distance_to_cover = deque()

for _ in range(n_pumps):
    entry = input().split()
    petrol_in_pump.append(int(entry[0]))
    distance_to_cover.append(int(entry[1]))


fuel = 0
start_pump = 0
i = 0

while i < n_pumps:
    fuel += petrol_in_pump[i]

    if fuel < distance_to_cover[i]:
        petrol_in_pump.rotate(-1)
        distance_to_cover.rotate(-1)
        start_pump += 1
        fuel = 0
        i = 0
        continue

    fuel -= distance_to_cover[i]
    i += 1

print(start_pump)
