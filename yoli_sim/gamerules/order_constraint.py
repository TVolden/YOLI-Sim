from yoli_sim.gamerules import GameRule
from yoli_sim.matchers import MatchPlacement

class OrderConstraint(GameRule):
    def __init__(self, order_key):
        super().__init__()
        self._order_key = order_key
        self._matcher = MatchPlacement(order_key)
    
    def evaluate(self, tiles: tuple[dict, ...]) -> tuple[int, ...]:
        return self._matcher.match(tiles)