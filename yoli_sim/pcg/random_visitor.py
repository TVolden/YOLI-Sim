from yoli_sim.pcg import GameRuleConstructionVisitor, RandomPicker

class RandomVisitor(GameRuleConstructionVisitor):
    def __init__(self, tiles:tuple[dict, ...], random = RandomPicker()) -> None:
        super().__init__()
        self._tiles = tiles
        self._random = random

    def property_key(self, exclude_keys: tuple[str] = None) -> str:
        dict_keys = [list(tiles.keys()) for tiles in self._tiles]
        flat_keys = [key for sub in dict_keys for key in sub]
        keys = list(set(flat_keys))
        if exclude_keys is not None:
             keys = [key for key in keys if key not in exclude_keys]
        return self.pick(keys)
    
    def property_value(self, property_key:str, exclude_values:list[str]=None) -> str:
        values = list(set([tile[property_key] for tile in self._tiles if property_key in tile.keys()]))
        if exclude_values is not None:
            values = [value for value in values if value not in exclude_values]
        return self.pick(values)
    
    def decimal(self, min: int, max: int) -> int:
        return self._random.pick_one(list(range(min, max+1)))
    
    def pick(self, list: tuple[object, ...]) -> object:
        return self._random.pick_one(list)

class RandomVisitorFactory:
    def construct(self, tiles:tuple[dict, ...]) -> GameRuleConstructionVisitor:
        return RandomVisitor(tiles)