# env.py

import gym
from gym import spaces
import numpy as np

class AppleOfFortuneEnv(gym.Env):
    def __init__(self):
        self.num_levels = 10
        self.num_choices = 5
        self.observation_space = spaces.Discrete(self.num_levels * self.num_choices)
        self.action_space = spaces.Discrete(self.num_choices)
        self.grid = None
        self.current_level = 1

        self.reset()

    def reset(self):
        # creating the 5 by 10 grid
        # self.grid = np.random.randint(2, size=(self.num_levels, self.num_choices))
        ## RANDOM ARRANGEMENT
        # self.grid = np.zeros((self.num_levels, self.num_choices), dtype=int)
        # for row in self.grid:
        #     rand_index = np.random.randint(self.num_choices)
        #     row[rand_index] = 1
        ## NOTRANDOM ARRANGEMENT
        pattern = [
            [1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0]
        ]
        self.grid = np.tile(pattern, (10 // len(pattern), 1))




        self.current_level = 1
        return self.current_level * self.num_choices

    def step(self, action):
        chosen_apple = self.grid[self.current_level, action]

        if chosen_apple == 1:
            reward = 0
            done = True
        else:
            reward = 1
            done = False
            self.current_level += 1
            # if self.current_level == 1:
            #     reward = 1
            #     done = False
            #     self.current_level += 1
            #
            # elif self.current_level == 2:
            #     reward = 2
            #     done = False
            #     self.current_level += 1
            #
            # elif self.current_level == 3:
            #     reward = 3
            #     done = False
            #     self.current_level += 1
            #
            # elif self.current_level == 4:
            #     reward = 4
            #     done = False
            #     self.current_level += 1
            #
            # elif self.current_level == 5:
            #     reward = 5
            #     done = False
            #     self.current_level += 1
            #
            # elif self.current_level == 6:
            #     reward = 6
            #     done = False
            #     self.current_level += 1
            #
            # elif self.current_level == 7:
            #     reward = 7
            #     done = False
            #     self.current_level += 1
            #
            # elif self.current_level == 8:
            #     reward = 8
            #     done = False
            #     self.current_level += 1
            #
            # elif self.current_level == 9:
            #     reward = 9
            #     done = False
            #     self.current_level += 1

        if self.current_level == self.num_levels:
            done = True

        # Render the environment (optional)
        self.render()

        return self.current_level * self.num_choices, reward, done, {}

    def render(self, mode='human'):
        if mode == 'human':
            # Implement rendering for visualization here (e.g., print grid)
            pass
        elif mode == 'ansi':
            # Return a textual representation of the environment
            representation = ""
            for row in self.grid:
                representation += " ".join(map(str, row)) + "\n"
            return representation
        else:
            super().render(mode=mode)

    def close(self):
        pass


# Register the environment with Gym
from gym.envs.registration import register

register(
    id='AppleOfFortune-v0',
    entry_point='env:AppleOfFortuneEnv',
)
