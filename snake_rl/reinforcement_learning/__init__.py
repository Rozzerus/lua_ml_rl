import gym
from gym.envs.registration import register

env_dict = gym.envs.registration.registry.env_specs.copy()

for env in env_dict:
    if 'RSnake-v0' in env:
        print("Remove {} from registry".format(env))
        del gym.envs.registration.registry.env_specs[env]

register(
    id='RSnake-v0',
    entry_point='snake_rl.reinforcement_learning.environment:SnakeEnvironment',
)
print("Created new RSnake-v0 in registry")
