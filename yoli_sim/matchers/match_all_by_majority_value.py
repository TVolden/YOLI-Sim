from yoli_sim.matchers import Matcher

class MatchAllByMajorityValue(Matcher):
    def __init__(self, match_key):
        self.key = match_key

    def match(self, tiles:tuple) -> tuple:
        output = [self.rejected]*len(tiles)
        values = [tile.get(self.key) if tile is not None or self.key not in tile.keys() else None for tile in tiles]
        majority_value = None
        majority_count = 0
        for value in set(values):
            if values.count(value) > majority_count:
                majority_count = values.count(value)
                majority_value = value
                
        for i in range(len(tiles)):
            if tiles[i] is None:
                output[i] = self.ignored
            elif self.key in tiles[i].keys() and tiles[i].get(self.key) == majority_value:
                output[i] = self.accepted
        return tuple(output)
