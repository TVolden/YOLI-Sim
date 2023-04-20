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
            if tile[self._triggered_key] == self._triggered_value:
                if True in self.conflicting_neighbors(tiles, i):
                    eval.append(-1)
                else:
                    eval.append(1)
            else:
                eval.append(0)
        return tuple(eval)
    
    def conflicting_neighbors(self, tiles, index):
        return [tile[self._trigger_key]==self._trigger_value \
         for tile in self.get_neighbors(tiles, index) \
         if self._trigger_key in tile.keys()]

    def get_neighbors(self, tiles, index):
        return [tiles[index+n] for n in self._neighbors \
                if index + n >= 0 and index + n < len(tiles)]