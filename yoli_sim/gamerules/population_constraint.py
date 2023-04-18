from yoli_sim.gamerules import GameRule

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