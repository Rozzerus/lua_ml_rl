import time
from pynput.keyboard import Controller
from random import randrange

keyboard = Controller()


def move_up():
    keyboard.press('w')
    keyboard.release('w')


def move_down():
    keyboard.press('s')
    keyboard.release('s')


def move_left():
    keyboard.press('a')
    keyboard.release('a')


def move_right():
    keyboard.press('d')
    keyboard.release('d')


if __name__ == '__main__':
    while True:
        time.sleep(1)
        i = randrange(4)
        if i == 1:
            move_up()
        elif i == 2:
            move_down()
        elif i == 3:
            move_right()
        elif i == 4:
            move_left()
