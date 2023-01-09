from .rewarder import Rewarder

class StepsRewarder(Rewarder):
    def __init__(self, negative:bool=True) -> None:
        self._modifier = -1 if negative else 1

    def reward(self, _, __, steps:int) -> float:
        return self._modifier * steps