import numpy as np
from .rewarder import Rewarder

class FixedRewarder(Rewarder):
    def __init__(self, reward:float=1):
        self.value = reward

    def reward(self, _, __, ___) -> float:
        return self.value