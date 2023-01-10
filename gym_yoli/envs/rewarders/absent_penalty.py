from .rewarder import Rewarder
import numpy as np

class AbsentPenalty(Rewarder):
    accepted = 1
    def reward(self, indications: np.array, _, __) -> float:
        return indications.count(self.accepted) - len(indications)