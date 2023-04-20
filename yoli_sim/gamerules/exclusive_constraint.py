from yoli_sim.gamerules import GameRule

class ExclusiveConstraint(GameRule):
    def __init__(self, allowed_key:str, allowed_value:str, accepted_value=1, ignored_value=0, rejected_value=-1):
        super().__init__(accepted_value, ignored_value, rejected_value)
        self._allowed_key = allowed_key
        self._allowed_value = allowed_value
    
    def evaluate(self, tiles: tuple[dict, ...]) -> tuple[int, ...]:
        return tuple([1 if self._allowed_key in tile.keys() and \
                       tile[self._allowed_key]==self._allowed_value \
                       else -1 \
                        for tile in tiles])