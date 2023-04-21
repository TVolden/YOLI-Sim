from yoli_sim.gamerules import GameRule
from yoli_sim.pcg import GameRuleFactory, GameRuleConstructionVisitor

class ExclusionConstraint(GameRule):
    def __init__(self, exclusion_key:str, exclusion_value:str):
        super().__init__()
        self._exclusion_key = exclusion_key
        self._exclusion_value = exclusion_value
    
    def evaluate(self, tiles: tuple[dict, ...]) -> tuple[int, ...]:
        return tuple([self._match(tile) for tile in tiles])
    
    def _match(self, tile:dict):
        if self._exclusion_key in tile.keys() and \
            tile[self._exclusion_key] == self._exclusion_value:
            return self.rejected
        return self.ignored
    
class ExclusionConstraintFactory(GameRuleFactory):
    def construct(self, visitor: GameRuleConstructionVisitor) -> GameRule:
        key = visitor.property_key()
        value = visitor.property_value(key)
        return ExclusionConstraint(key, value)