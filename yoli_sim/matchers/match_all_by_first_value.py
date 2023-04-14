from yoli_sim.matchers import Matcher

class MatchAllByFirstValue(Matcher):
    def __init__(self, match_key, accepted_value=1, ignored_value=0, rejected_value=-1):
        super().__init__(accepted_value, ignored_value, rejected_value)
        self.key = match_key

    def match(self, tiles:tuple) -> tuple:
        output = [self.rejected]*len(tiles)
        accepted_value = None
        for i in range(len(tiles)):
            if tiles[i] is None:
                output[i] = self.ignored
            elif self.key in tiles[i].keys():
                if accepted_value is None:
                    accepted_value = tiles[i].get(self.key)
                    output[i] = self.accepted
                elif tiles[i].get(self.key) == accepted_value:
                    output[i] = self.accepted
        return tuple(output)