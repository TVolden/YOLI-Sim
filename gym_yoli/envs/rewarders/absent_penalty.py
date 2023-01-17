from .rewarder import Rewarder
import numpy as np

class AbsentPenalty(Rewarder):
    accepted = 1

    def reward(self, _, __, indications: np.array, ___, ____) -> float:
        return indications.count(self.accepted) - len(indications)