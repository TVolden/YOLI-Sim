from .rewarder import Rewarder

class TerminatedRewarder(Rewarder):
    def reward(self, _, terminated: bool, __) -> float:
        return 1 if terminated else 0 # binary reward