from random import random
import gymnasium as gym

class YoliTileActionWrapper(gym.ActionWrapper):
    def __init__(self, env):
        super().__init__(env)
        self.env = env
    
    def action(self, action):
        pos = action.position
        tile = self.env._positions[pos]

        if tile != 0:
            action.tile = 0
        else:
            while action.tile in self.env._positions:
                action.tile = random(self.env.tiles)

        return action
