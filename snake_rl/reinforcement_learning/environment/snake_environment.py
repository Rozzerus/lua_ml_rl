import gym
from gym import spaces
import numpy as np

from snake_rl.reinforcement_learning.environment.snake_controller import SnakeController


class SnakeEnvironment(gym.Env):

    def __init__(self):
        self.snake_controller: SnakeController = None

        self.action_space = spaces.Discrete(3)
        self.observation_space = spaces.Box(
            dtype=np.float32,
            low=np.array([0, 0, 0, -1, -1]),
            high=np.array([1, 1, 1, 1, 1]),
        )

        self.rewards = None

    def set_rewards(self, rew_step, rew_apple, rew_death, rew_death2, rew_apple_func):
        self.rewards = [rew_step, rew_apple, rew_death, rew_death2, rew_apple_func]

    def step(self, action):
        if action != 0:
            self.snake_controller.direction = self.snake_controller.DIRECTIONS[self.snake_controller.direction[action]]

        info = {}

        raw_state, reward, done = self.snake_controller.get_raw_state()
        info['apples'] = self.snake_controller.count_apples

        state = np.array(raw_state, dtype=np.float32)

        return state, reward, done, info

    def reset(self):
        if self.rewards:
            self.snake_controller = SnakeController(reward_step=self.rewards[0], reward_apple=self.rewards[1],
                                                    reward_death=self.rewards[2], reward_death2=self.rewards[3],
                                                    reward_apple_func=self.rewards[4])
        else:
            self.snake_controller = SnakeController()
        self.snake_controller.reset()

        raw_state = self.snake_controller.get_raw_state()
        state = np.array(raw_state[0], dtype=np.float32)

        return state

    def render(self, mode='human'):
        pass
