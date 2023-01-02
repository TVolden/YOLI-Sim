from .rewarder import Rewarder
import numpy as np

class AcceptedRewarder(Rewarder):
    accepted = 1
    def reward(self, indications: np.array, _) -> float:
        return indications.count(self.accepted) / len(indications)