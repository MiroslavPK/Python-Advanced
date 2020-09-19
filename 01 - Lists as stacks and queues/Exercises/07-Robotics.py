from collections import deque
from datetime import datetime, timedelta

robots_input = input().split(';')
starting_time = datetime.strptime(input(), '%H:%M:%S')

robots = {}
products_on_hold = deque()

for tokens in robots_input:
    robot_name, processing_time = tokens.split('-')
    robots[robot_name] = {
        'processing_time': float(processing_time),
        'available_at': starting_time
    }

assembly_line_technical_time = 0

product = input()
while product != 'End':
    products_on_hold.append(product)
    product = input()


while products_on_hold:
    assembly_line_technical_time += 1
    current_time = starting_time + timedelta(seconds=assembly_line_technical_time)

    for robot in robots:
        if robots[robot]['available_at'] <= current_time:
            print(f'{robot} - {products_on_hold.popleft()} [{current_time.time()}]')
            robots[robot]['available_at'] = current_time + timedelta(seconds=robots[robot]['processing_time'])
            break
    else:
        products_on_hold.rotate(-1)
