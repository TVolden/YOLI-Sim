from .rewarder import Rewarder
import numpy as np

class AcceptedRewarder(Rewarder):
    accepted = 1
    def reward(self, action:str, position:int, indications: np.array, __, ___) -> float:
        if action == Rewarder.action_add and indications[position] == self.accepted:
            return 1
        return 0