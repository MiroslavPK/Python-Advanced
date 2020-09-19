from collections import deque

food_quantity = int(input())
orders = deque(map(int, input().split()))

print(max(orders))

while orders:
    if food_quantity < orders[0]:
        break
    order = orders.popleft()
    food_quantity -= order

if orders:
    print(f'Orders left: {" ".join(map(str, orders))}')
else:
    print('Orders complete')
