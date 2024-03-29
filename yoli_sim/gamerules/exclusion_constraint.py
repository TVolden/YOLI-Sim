from yoli_sim.gamerules import GameRule

class ExclusionConstraint(GameRule):
    def __init__(self, exclusion_key:str, exclusion_value:str):
        super().__init__()
        self._exclusion_key = exclusion_key
        self._exclusion_value = exclusion_value
    
    def evaluate(self, tiles: tuple[dict, ...]) -> tuple[int, ...]:
        return tuple([self._match(tile) for tile in tiles])
    
    def _match(self, tile:dict):
        if tile is not None and self._exclusion_key in tile.keys() and \
            tile[self._exclusion_key] == self._exclusion_value:
            return self.rejected
        return self.ignored
    
    def __str__(self) -> str:
        return f"Exclude any where {self._exclusion_key} is equal to {self._exclusion_value}"
    
    def entropy(self, board: tuple[dict, ...], tiles: tuple[dict, ...]) -> list[list[bool]]:
        valid_tiles = [False if self._exclusion_key in t.keys() and t[self._exclusion_key] == self._exclusion_value else True for t in tiles]
        return [valid_tiles if b is None else [False] * len(tiles) for b in board]
