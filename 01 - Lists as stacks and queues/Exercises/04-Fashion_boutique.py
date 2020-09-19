clothes = list(map(int, input().split()))
rack_capacity = int(input())
racks_needed = 0
clothes_sum = 0

while clothes:
    cloth = clothes.pop()

    if clothes_sum + cloth == rack_capacity:
        racks_needed += 1
        clothes_sum = 0
        continue

    elif clothes_sum + cloth > rack_capacity:
        racks_needed += 1
        clothes_sum = 0

    clothes_sum += cloth

    if clothes_sum > 0 and len(clothes) == 0:
        racks_needed += 1

print(racks_needed)
