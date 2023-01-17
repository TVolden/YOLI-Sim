from .rewarder import Rewarder
import numpy as np

class RejectPenaltyDecorator(Rewarder):
    reject=2

    def __init__(self, decoratee:Rewarder, penalty=0):
        self.decoratee = decoratee
        self.penalty = penalty

    def reward(self, action:str, position:int, indications: np.array, terminated: bool, steps: int) -> float:
        if indications.count(self.reject) > 0:
            return self.penalty
        return self.decoratee.reward(action, position, indications, terminated, steps)