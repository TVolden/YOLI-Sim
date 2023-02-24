from gym_yoli.matchers import Matcher

class MatchAllByFirstValue(Matcher):
    def __init__(self, match_key):
        self.key = match_key

    def match(self, tiles:tuple) -> tuple:
        output = [self.FAILED]*len(tiles)
        accepted_value = None
        for i in range(len(tiles)):
            if tiles[i] is None:
                output[i] = self.SKIPPED
            elif self.key in tiles[i].keys():
                if accepted_value is None:
                    accepted_value = tiles[i].get(self.key)
                    output[i] = self.PASSED
                elif tiles[i].get(self.key) == accepted_value:
                    output[i] = self.PASSED
        return tuple(output)