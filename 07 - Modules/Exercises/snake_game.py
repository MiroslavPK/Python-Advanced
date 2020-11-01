from random import randint
import os


class Game:
    def __init__(self):
        self.__head_pos = (0, 0)
        self.__body_pos = []
        self.__move = 10
        self.__direction = 'Right'
        self.__food_position = randint(-280, 280), randint(-280, 280)
        self.__high_score = 0
        self.border_check()

    def go_up(self):
        if self.__direction != 'Down':
            self.__direction = 'Up'

    def go_down(self):
        if self.__direction != 'Up':
            self.__direction = 'Down'

    def go_right(self):
        if self.__direction != 'Left':
            self.__direction = 'Right'

    def go_left(self):
        if self.__direction != 'Right':
            self.__direction = 'Left'

    def move(self):
        x, y = self.__head_pos
        if self.__direction == 'Up':
            self.__head_pos = (x, y + self.__move)

        if self.__direction == 'Down':
            self.__head_pos = (x, y - self.__move)

        if self.__direction == 'Right':
            self.__head_pos = (x + self.__move, y)

        if self.__direction == 'Left':
            self.__head_pos = (x - self.__move, y)

    def head_position(self):
        return self.__head_pos

    def add_body_segment(self, body_segment):
        self.__body_pos.append(body_segment)

    def body_position(self):
        return self.__body_pos

    def restart(self):
        self.__head_pos = (0, 0)
        return self.__head_pos

    def food_position(self):
        return self.__food_position

    def food_respawn(self):
        self.__food_position = randint(-280, 280), randint(-280, 260)
        return self.__food_position

    def border_check(self):
        x, y = self.__head_pos

        if (x > 290 or x < -290) or (y > 290 or y < -290):
            return True

    def game_over_update(self):
        for part in self.__body_pos:
            part.goto(1000, 1000)
        self.__body_pos.clear()

    def body_collision_check(self):
        head_x, head_y = self.__head_pos
        for part in self.__body_pos:
            part_x, part_y = part.xcor(), part.ycor()
            if abs(head_x - part_x) <= 5 and abs(head_y - part_y) <= 5:
                return True

    def high_score(self):
        if not os.path.exists('scores/'):
            os.makedirs('scores/')
        with open('scores/high_score.txt', 'r') as hs_file:
            cur_high_score = hs_file.readline()
            if cur_high_score != '':
                self.__high_score = int(cur_high_score)
        return self.__high_score

    def new_record(self, new_high_score):
        with open('scores/high_score.txt', 'w+') as hs_file:
            if new_high_score > self.__high_score:
                hs_file.write(str(new_high_score))
