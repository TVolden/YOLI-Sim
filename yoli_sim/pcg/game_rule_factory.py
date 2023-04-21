from abc import ABC, abstractmethod
from yoli_sim.pcg import GameRuleConstructionVisitor
from yoli_sim.gamerules import GameRule

class GameRuleFactory(ABC):
    @abstractmethod
    def construct(self, visitor:GameRuleConstructionVisitor) -> GameRule:
        ...