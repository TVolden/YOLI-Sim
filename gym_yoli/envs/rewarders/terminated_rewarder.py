from .rewarder import Rewarder
import numpy as np

class TerminatedRewarder(Rewarder):
    def reward(self, _, terminated: bool, __) -> float:
        return 1 if terminated else 0 # binary reward

class TerminatedRewardDecorator(Rewarder):
    def __init__(self, decoratee:Rewarder, value:float = 1):
        self._decoratee = decoratee
        self._value = value

    def reward(self, indications: np.array, terminated: bool, steps: int) -> float:
        if terminated:
            return self._value
        return self._decoratee.reward(indications, terminated, steps)