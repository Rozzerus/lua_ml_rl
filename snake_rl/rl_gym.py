import gym
import reinforcement_learning

env = gym.make('RSnake-v0')

for i in range(2000):
    env.reset()
    for t in range(5000):
        env.render()
        state, reward, done, info = env.step(env.action_space.sample())
        if done:
            print('episode {} finished after {} timesteps'.format(i, t))
            break

### rrrrr
