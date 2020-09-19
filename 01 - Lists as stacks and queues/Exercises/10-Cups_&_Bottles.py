from collections import deque

cups = deque(map(int, input().split()))
bottles = deque(map(int, input().split()))
wasted_liters = 0

while True:
    if not cups or not bottles:
        break

    cup = cups[0]
    bottle = bottles.pop()

    if cup > bottle:
        cup -= bottle

        while cup > 0 and bottles:
            bottle = bottles.pop()
            if cup - bottle > 0:
                cup -= bottle
                continue

            wasted_liters += bottle - cup
            cup -= bottle
            cups.popleft()
    else:
        cups.popleft()
        wasted_liters += bottle - cup

if not cups and bottles:
    print(f'Bottles: {" ".join(list(map(str, bottles)))}')
else:
    print(f'Cups: {" ".join(list(map(str, cups)))}')

print(f'Wasted litters of water: {wasted_liters}')
