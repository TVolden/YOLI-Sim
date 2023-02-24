from .rewarder import Rewarder
import numpy as np

class TerminatedRewarder(Rewarder):
    def reward(self, _, __, ___, terminated: bool, ____) -> float:
        return 1 if terminated else 0 # binary reward

class TerminatedRewardDecorator(Rewarder):
    def __init__(self, decoratee:Rewarder, value:float = 1):
        self._decoratee = decoratee
        self._value = value

    def reward(self, action:str, position:int, indications: np.array, terminated: bool, steps: int) -> float:
        if terminated:
            return self._value
        return self._decoratee.reward(action, position, indications, terminated, steps)