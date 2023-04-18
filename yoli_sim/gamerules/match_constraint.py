from yoli_sim.gamerules import GameRule
from yoli_sim.matchers import MatchAllByFirstValue

class MatchConstraint(GameRule):
    def __init__(self, matcher_key:str):
        super().__init__()
        self._matcher = MatchAllByFirstValue(matcher_key)
    
    def evaluate(self, tiles: tuple[dict, ...]) -> tuple[int, ...]:
        return self._matcher.match(tiles)