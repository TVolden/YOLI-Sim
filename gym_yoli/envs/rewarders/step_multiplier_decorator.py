from .rewarder import Rewarder
import numpy as np

class StepMultiplierDecorator(Rewarder):
    def __init__(self, decoratee:Rewarder):
        self.decoratee = decoratee

    def reward(self, action:str, position:int, indications: np.array, terminated: bool, steps: int) -> float:
        return self.decoratee.reward(action, position, indications, terminated, steps) * steps