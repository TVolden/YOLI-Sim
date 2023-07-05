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
            if tile is not None and self._key in tile.keys() and tile[self._key] == self._value:
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

    def entropy(self, board: tuple[dict, ...], tiles: tuple[dict, ...]) -> list[list[bool]]:
        amount = len(tuple(filter(lambda x: self._key in x.keys() and x[self._key] == self._value)))
        if amount >= self._limit:
            return [[False] * len(tiles)] * len(board) # Limit reached, no more tiles
        
        valid_tiles = [True if self._key in t.keys() and t[self._key] == self._value else False for t in tiles]
        return [valid_tiles if b is None else [False] * len(tiles) for b in board]