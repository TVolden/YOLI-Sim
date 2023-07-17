from yoli_sim.gamerules import GameRule

class NeighborConstraint(GameRule):
    def __init__(self, triggered_key:str, triggered_value:str, trigger_key:str, trigger_value:str):
        super().__init__()
        self._triggered_key = triggered_key
        self._triggered_value = triggered_value
        self._trigger_key = trigger_key
        self._trigger_value = trigger_value
        self._neighbors = [-1, 1]
    
    def evaluate(self, tiles: tuple[dict, ...]) -> tuple[int, ...]:
        eval = []
        for i, tile in enumerate(tiles):
            if tile is not None and tile[self._triggered_key] == self._triggered_value:
                if True in self.conflicting_neighbors(tiles, i):
                    eval.append(self.rejected)
                else:
                    eval.append(self.accepted)
            else:
                eval.append(self.ignored)
        return tuple(eval)
    
    def __str__(self) -> str:
        return f"Those with {self._triggered_key} set to {self._triggered_value} cannot be adjacent to those with {self._trigger_key} set to {self._trigger_value}"
    
    def conflicting_neighbors(self, tiles, index):
        return [tile[self._trigger_key]==self._trigger_value \
         for tile in self.get_neighbors(tiles, index) \
         if self._trigger_key in tile.keys()]

    def get_neighbors(self, tiles, index):
        return [tiles[index+n] for n in self._neighbors \
                if index + n >= 0 and index + n < len(tiles) \
                    and tiles[index+n] is not None]
    
    def get_valid_options(self, board, tiles, index):
        if True in self.conflicting_neighbors(board, index):
            return [tile[self._triggered_key]!=self._triggered_value for tile in tiles]
        return [True] * len(tiles)

    def entropy(self, board: tuple[dict, ...], tiles: tuple[dict, ...]) -> list[list[bool]]:
        entropy = []
        for i in range(len(board)):
            if board[i] is not None:
                entropy.append([False] * len(tiles))
            else:
                entropy.append(self.get_valid_options(board, tiles, i))

        return entropy