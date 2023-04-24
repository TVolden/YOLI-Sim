from yoli_sim.gamerules import GameRule
from yoli_sim.pcg import GameRuleFactory, GameRuleConstructionVisitor

class ExclusiveConstraint(GameRule):
    def __init__(self, allowed_key:str, allowed_value:str):
        super().__init__()
        self._allowed_key = allowed_key
        self._allowed_value = allowed_value
    
    def evaluate(self, tiles: tuple[dict, ...]) -> tuple[int, ...]:
        return tuple([1 if self._allowed_key in tile.keys() and \
                       tile[self._allowed_key]==self._allowed_value \
                       else -1 \
                        for tile in tiles])
    
    def __str__(self) -> str:
        return f"Exclusively for any where {self._allowed_key} is equal to {self._allowed_value}"

class ExclusiveConstraintFactory(GameRuleFactory):
    def construct(self, visitor: GameRuleConstructionVisitor) -> GameRule:
        key = visitor.property_key()
        value = visitor.property_value(key)
        return ExclusiveConstraint(key, value)