from yoli_sim.gamerules import GameRule
from yoli_sim.matchers import MatchAllByFirstValue
from yoli_sim.pcg import GameRuleFactory, GameRuleConstructionVisitor

class MatchConstraint(GameRule):
    def __init__(self, matcher_key:str):
        super().__init__()
        self._key = matcher_key
        self._matcher = MatchAllByFirstValue(matcher_key)
    
    def evaluate(self, tiles: tuple[dict, ...]) -> tuple[int, ...]:
        return self._matcher.match(tiles)
    
    def __str__(self) -> str:
        return f"Only the ones where the value of {self._key} match"

class MatchConstraintFactory(GameRuleFactory):
    def construct(self, visitor: GameRuleConstructionVisitor) -> GameRule:
        key = visitor.property_key()
        return MatchConstraint(key)