from .rewarder import Rewarder
import numpy as np

class StepMultiplierDecorator(Rewarder):
    def __init__(self, decoratee:Rewarder):
        self.decoratee = decoratee

    def reward(self, indications: np.array, terminated: bool, steps: int) -> float:
        return self.decoratee.reward(indications, terminated, steps) * steps