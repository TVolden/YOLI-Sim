from abc import ABC, abstractmethod
from yoli_sim.gamerules import GameRule

class GameRuleMutator(GameRule, ABC):
    def __init__(self, rule:GameRule):
        super().__init__()
        self.rule = rule

    def evaluate(self, tiles: tuple[dict, ...]) -> tuple[int, ...]:
        return self.rule.evaluate(tiles)
    
    def __str__(self) -> str:
        return self.rule.__str__()
    
    @abstractmethod
    def mutate(self) -> None:
        ...