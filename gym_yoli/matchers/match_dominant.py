from gym_yoli.matchers import Matcher

class MatchDominant(Matcher):
    def __init__(self, matchers:list):
        self.matchers = matchers

    def match(self, tiles:tuple) -> tuple:
        best_result = [self.SKIPPED] * len(tiles)
        best_score = 0
        for matcher in self.matchers:
            result = matcher.match(tiles)
            score = sum([2**(len(tiles)-i)*(result[i]%2) for i in range(len(result))])
            if score > best_score:
                best_score = score
                best_result = result

        return tuple(best_result)