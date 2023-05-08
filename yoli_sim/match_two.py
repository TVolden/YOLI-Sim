from yoli_sim import YoliTileGame, YoliTile
from yoli_sim.eval import RuleEvaluator
from yoli_sim.gamerules import MatchConstraint

class MatchTwo (YoliTileGame):
    def __init__(self, tiles = 4):
        super().__init__(tiles2win=2)
        self._tiles = [{"image": f"{x:02}.png", "group": int((x)/2+0.5)} for x in range(1, tiles+1)]
        self._rule = MatchConstraint("group")

    def tile_at(self, index:int) -> YoliTile:
        return YoliTile(f"{index}", self._tiles[index].get("image"))

    def count_tiles(self) -> int:
        return len(self._tiles)

    def _evaluate(self, board: tuple[dict,...]) -> tuple():
        indication = self._rule.evaluate(board)
        terminal = indication.count(1) >= 2
        return indication, terminal
        
    def reset(self):
        return super().reset()
    
    def analyze_rule(self, evaluator: RuleEvaluator) -> float:
        return evaluator.evaluate(self._rule)