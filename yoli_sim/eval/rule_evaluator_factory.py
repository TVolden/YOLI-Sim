from abc import ABC, abstractmethod
from yoli_sim.eval import RuleEvaluator

class RuleEvaluatorFactory(ABC):
    @abstractmethod
    def create(self, tiles2win:int, tiles:tuple[dict]) -> RuleEvaluator:
        ...