from gym_yoli.matchers import Matcher

class MatchPlacement(Matcher):
    def __init__(self, match_key):
        self.key = match_key

    def match(self, tiles:tuple) -> tuple:
        output = [self.FAILED]*len(tiles)
        for i in range(len(tiles)):
            if tiles[i] is None:
                output[i] = self.SKIPPED
            elif self.key in tiles[i].keys() and tiles[i].get(self.key) == i:
                output[i] = self.PASSED
        return tuple(output)