from yoli_sim.gamerules import GameRule
from yoli_sim.matchers import MatchAllByFirstValue

class MatchConstraint(GameRule):
    def __init__(self, matcher_key:str, accepted_value=1, ignored_value=0, rejected_value=-1):
        super().__init__(accepted_value, ignored_value, rejected_value)
        self._matcher = MatchAllByFirstValue(matcher_key)
    
    def evaluate(self, tiles: tuple[dict, ...]) -> tuple[int, ...]:
        return self._matcher.match(tiles)