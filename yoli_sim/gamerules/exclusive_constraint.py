from yoli_sim.gamerules import GameRule

class ExclusiveConstraint(GameRule):
    def __init__(self, allowed_key:str, allowed_value:str):
        super().__init__()
        self._allowed_key = allowed_key
        self._allowed_value = allowed_value
    
    def evaluate(self, tiles: tuple[dict, ...]) -> tuple[int, ...]:
        return tuple([self._match(tile) for tile in tiles])
    
    def _match(self, tile:dict):
        if tile is None:
            return self.ignored
        elif self._allowed_key in tile.keys() and \
            tile[self._allowed_key] == self._allowed_value:
            return self.accepted
        return self.rejected
    
    def __str__(self) -> str:
        return f"Exclusively for any where {self._allowed_key} is equal to {self._allowed_value}"

    def entropy(self, board: tuple[dict, ...], remaining: tuple[dict, ...]) -> int:
        free_space = len(tuple(filter(lambda x: x is None, board)))
        valid_tiles = len(tuple(filter(lambda x: self._allowed_key in x.keys() and x[self._allowed_key] == self._allowed_value, remaining)))
        return (valid_tiles - free_space/2 - 1/2) * free_space