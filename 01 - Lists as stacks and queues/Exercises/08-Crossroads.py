from collections import deque

green_light_duration = int(input())
free_window = int(input())

cars_on_crossroad = deque()
cars_passed = 0
is_Safe = True

while True:
    light = input()

    if light == 'END' or not is_Safe:
        break

    if light == 'green':
        green_light_check = green_light_duration

        while green_light_check > 0:
            if not cars_on_crossroad:
                break

            car_passing = cars_on_crossroad.popleft()

            if green_light_check - len(car_passing) >= 0:
                green_light_check -= len(car_passing)
                cars_passed += 1
                continue
            elif (green_light_check + free_window) - len(car_passing) >= 0:
                green_light_check -= len(car_passing)
                cars_passed += 1
                break
            else:
                red_light_on = green_light_check + free_window
                hit = car_passing[red_light_on]
                is_Safe = False

                print('A crash happened!')
                print(f'{car_passing} was hit at {hit}.')
                break
    else:
        cars_on_crossroad.append(light)

if is_Safe:
    print('Everyone is safe.')
    print(f'{cars_passed} total cars passed the crossroads.')
