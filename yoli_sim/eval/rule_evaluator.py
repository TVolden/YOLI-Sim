from abc import ABC, abstractmethod
from yoli_sim.gamerules import GameRule

class RuleEvaluator(ABC):
    @abstractmethod
    def evaluate(self, rule:GameRule) -> float:
        ...