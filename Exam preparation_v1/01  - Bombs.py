from collections import deque

bomb_effects = deque(list(map(int, input().split(', '))))
bomb_casings = list(map(int, input().split(', ')))

bomb_poach = 0
bombs = {40: "Datura Bombs", 60: "Cherry Bombs", 120: "Smoke Decoy Bombs"}
bombs_made = {"Datura Bombs": 0, "Cherry Bombs": 0, "Smoke Decoy Bombs": 0}

while bomb_casings and bomb_effects and bomb_poach != 3:
    bomb_materials = bomb_effects[0] + bomb_casings[-1]

    if bomb_materials in bombs:
        bomb = bombs[bomb_materials]
        bombs_made[bomb] += 1
        if bombs_made[bomb] == 3:
            bomb_poach += 1

        bomb_effects.popleft()
        bomb_casings.pop()

    else:
        bomb_casings[-1] -= 5


if bomb_poach == 3:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

print(f"Bomb Effects: {', '.join(map(str, bomb_effects)) if bomb_effects else 'empty'}")
print(f"Bomb Casings: {', '.join(map(str, bomb_casings)) if bomb_casings else 'empty'}")

for bomb, count in sorted(bombs_made.items()):
    print(f'{bomb}: {count}')
