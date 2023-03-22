from .rewarder import Rewarder
import numpy as np

class AcceptedRewarder(Rewarder):
    accepted = 1
    def __init__(self, accept_reward = 1, nonAccept_reward = 0) -> None:
        self._true = accept_reward
        self._false = nonAccept_reward

    def reward(self, action:str, position:int, indications: np.array, __, ___) -> float:
        if action == Rewarder.action_add and indications[position] == self.accepted:
            return self._true
        return self._false