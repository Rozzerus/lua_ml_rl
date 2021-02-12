import time
import json
from pynput.keyboard import Controller
from random import randrange
from math import sqrt


class SnakeController:

    def __init__(self, reward_step=-0.25, reward_apple=3.5, reward_death=-10.0, reward_death2=-100.0,
                 reward_apple_func=lambda cnt, reward: sqrt(cnt) * reward) -> None:
        self.keyboard: Controller = Controller()
        self.reward_reader: GameRewordReader = GameRewordReader('../snake_game/snake_log.txt')

        self.direction = self.DIRECTIONS['UP']

        self.reward_step = reward_step
        self.reward_apple = reward_apple
        self.reward_death = reward_death
        self.reward_death2 = reward_death2
        self.reward_apple_func = reward_apple_func

        self.minimal_count_steps: int = 50
        self.minimal_count_apples: int = 5
        self.count_steps: int = 0
        self.count_apples: int = 0
        self.game_over: bool = False

    DIRECTIONS = {
        'UP': 'w',
        'DOWN': 's',
        'LEFT': 'a',
        'RIGHT': 'd',
    }

    def move(self, action) -> None:
        key = self.DIRECTIONS[action]
        self.keyboard.press(key)
        self.keyboard.release(key)

    def reset(self) -> None:
        time.sleep(2)
        key = 'r'
        self.keyboard.press(key)
        self.keyboard.release(key)

    def get_raw_state(self):
        game_state: dict = self.reward_reader.read_current_game_state()
        game_stage = game_state['state']
        reward = self.reward_step
        self.count_steps = self.reward_reader.get_count_steps()
        if self.count_apples < int(game_state['tail_legth']):
            self.count_apples = int(game_state['tail_legth'])
            reward = self.reward_apple_func(self.count_apples, self.reward_apple)
        elif 'game_over' in game_stage:
            self.game_over = True
            if self.count_steps < self.minimal_count_steps or self.count_apples < self.minimal_count_apples:
                reward = self.reward_death2
            else:
                reward = self.reward_death

        state = [
            game_state["snakeX"], game_state["snakeY"],
            game_state["appleX"], game_state["appleY"]
        ]

        return state, reward, self.game_over


class GameRewordReader:

    def __init__(self, path) -> None:
        self.path = path
        self.steps = 0

    def get_count_steps(self) -> int:
        return self.steps

    def read_current_game_state(self) -> dict:
        file_handle = open(self.path, 'r')
        line_list = file_handle.readlines()
        file_handle.close()
        self.steps = len(line_list)
        if self.steps > 0:
            print(line_list[-1])
            return json.loads(line_list[-1])
        else:
            return json.loads('{"snakeX":15,"snakeY":15,"appleX":0,"appleY":0,"tail_legth":0,"state":"game_over"}')


if __name__ == '__main__':
    pass
    # print(GameRewordReader('../../../snake_game/snake_log.txt').read_current_game_state())
    # controller = SnakeController()
    # controller.DIRECTIONS[1]
    # while True:
    #     time.sleep(1)
    #     i = randrange(4)
    #     if i == 0:
    #         controller.move('UP')
    #     elif i == 1:
    #         controller.move('DOWN')
    #     elif i == 2:
    #         controller.move('LEFT')
    #     elif i == 3:
    #         controller.move('RIGHT')
