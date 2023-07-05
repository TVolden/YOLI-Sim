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

    def entropy(self, board: tuple[dict, ...], tiles: tuple[dict, ...]) -> list[list[bool]]:
        valid_tiles = [True if self._allowed_key in t.keys() and t[self._allowed_key] == self._allowed_value else False for t in tiles]
        return [valid_tiles if b is None else [False] * len(tiles) for b in board]