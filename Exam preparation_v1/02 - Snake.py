def move(snake_pos, dir):
    territory[snake_pos[0]][snake_pos[1]] = '.'
    if dir == 'left':
        snake_pos[1] -= 1
    elif dir == 'right':
        snake_pos[1] += 1
    elif dir == 'up':
        snake_pos[0] -= 1
    elif dir == 'down':
        snake_pos[0] += 1


def game_over(snake_pos):
    if (snake_pos[0] < 0 or snake_pos[0] > size - 1) or (snake_pos[1] < 0 or snake_pos[1] > size - 1):
        return True


size = int(input())
territory = [list(input()) for _ in range(size)]

snake = [[row, part.index('S')] for row, part in enumerate(territory) if 'S' in part]
snake = snake[0]
food = 0

while True:
    direction = input()
    territory[snake[0]][snake[1]] = '.'
    move(snake, direction)

    if game_over(snake):
        print('Game over!')
        print(f'Food eaten: {food}')
        break

    if territory[snake[0]][snake[1]] == '*':
        food += 1
    elif territory[snake[0]][snake[1]] == 'B':
        territory[snake[0]][snake[1]] = '.'
        snake = [[row, part.index('B')] for row, part in enumerate(territory) if 'B' in part]
        snake = snake[0]

    if food >= 10:
        territory[snake[0]][snake[1]] = 'S'
        print('You won! You fed the snake.')
        print(f'Food eaten: {food}')
        break

[print(''.join(part)) for part in territory]
