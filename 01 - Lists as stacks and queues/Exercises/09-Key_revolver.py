from collections import deque

bullet_price = int(input())
gun_barrel = int(input())
bullets_size = list(map(int, input().split()))
locks = deque(map(int, input().split()))
vault_reward = int(input())

current_barrel = gun_barrel
while True:

    if current_barrel == 0 and bullets_size:
        print('Reloading!')
        current_barrel = gun_barrel
        continue

    if not bullets_size or not locks:
        break

    bullet = bullets_size.pop()
    vault_reward -= bullet_price
    current_barrel -= 1

    lock = locks[0]

    if bullet <= lock:
        locks.popleft()
        print('Bang!')
    else:
        print('Ping!')

if not bullets_size and locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
elif not locks:
    print(f'{len(bullets_size)} bullets left. Earned ${vault_reward}')
