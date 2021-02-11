import gym

env = gym.make('RSnake-v0').env

for i in range(100):
    env.reset()
    for t in range(1000):
        env.render()
        state, reward, done, info = env.step(env.action_space.sample())
        if done:
            print('episode {} finished after {} timesteps'.format(i, t))
            break
