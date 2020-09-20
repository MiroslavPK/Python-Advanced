n = int(input())

cars_in = set()

parking_system = {
    'IN': cars_in.add,
    'OUT': cars_in.remove
}

for _ in range(n):
    command, reg = input().split(', ')
    parking_system[command](reg)

if cars_in:
    [print(reg) for reg in cars_in]
else:
    print('Parking Lot is Empty')
