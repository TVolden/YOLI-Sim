from yoli_sim.gamerules import GameRule

class ExclusionConstraint(GameRule):
    def __init__(self, exclusion_key:str, exclusion_value:str, accepted_value=1, ignored_value=0, rejected_value=-1):
        super().__init__(accepted_value, ignored_value, rejected_value)
        self._exclusion_key = exclusion_key
        self._exclusion_value = exclusion_value
    
    def evaluate(self, tiles: tuple[dict, ...]) -> tuple[int, ...]:
        return tuple([self._match(tile) for tile in tiles])
    
    def _match(self, tile:dict):
        if self._exclusion_key in tile.keys() and \
            tile[self._exclusion_key] == self._exclusion_value:
            return self.rejected
        return self.ignored