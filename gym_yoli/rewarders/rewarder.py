import numpy as np

class Rewarder:
    # Acceptable return value range [0:1]
    def reward(self, indications: np.array, terminated: bool) -> float:
        pass