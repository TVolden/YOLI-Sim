from gym_yoli.matchers import Matcher

class NoRepeatedValue(Matcher):
    def __init__(self, match_key):
        self.key = match_key

    def match(self, tiles:tuple) -> tuple:
        output = [self.FAILED]*len(tiles)
        values = []
        for i in range(tiles):
            if tiles[i] is None:
                output[i] = self.SKIPPED
            elif self.key in tiles[i].keys() and tiles[i].get(self.key) not in values:
                values.append(tiles[i].get(self.key))
                output[i] = self.PASSED
        return tuple(output)