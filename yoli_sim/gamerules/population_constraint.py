from yoli_sim.gamerules import GameRule
from yoli_sim.pcg import GameRuleFactory, GameRuleConstructionVisitor

class PopulationConstraint(GameRule):
    def __init__(self, limit:int, property_key:str, property_value:str):
        super().__init__()
        self._limit = limit
        self._key = property_key
        self._value = property_value
    
    def evaluate(self, tiles: tuple[dict, ...]) -> tuple[int, ...]:
        amount = 0
        evaluation = []
        for tile in tiles:
            if self._key in tile.keys() and tile[self._key] == self._value:
                if amount < self._limit:
                    evaluation.append(self.accepted)
                    amount += 1
                else:
                    evaluation.append(self.rejected)
            else:
                evaluation.append(self.ignored)
        
        return tuple(evaluation)
    
    def __str__(self) -> str:
        return f"There can only be {self._limit} with {self._key} set to {self._value}"
    
class PopulationConstraintFactory(GameRuleFactory):
    def construct(self, visitor: GameRuleConstructionVisitor) -> GameRule:
        limit = visitor.decimal(1,4)
        key = visitor.property_key()
        value = visitor.property_value(key)
        return PopulationConstraint(limit, key, value)
        