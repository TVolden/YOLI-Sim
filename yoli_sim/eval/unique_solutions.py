from yoli_sim.eval import RuleEvaluator, RuleEvaluatorFactory
from yoli_sim.gamerules import GameRule
from yoli_sim.utils import SetGenerator

class UniqueSolutions(RuleEvaluator):
    def __init__(self, tiles2win:int, tiles:tuple[dict]) -> None:
        super().__init__()
        self.tiles2win = tiles2win
        self.tiles = tiles
        self.sets = SetGenerator(tiles2win, len(tiles)).generate_all()

    def evaluate(self, rule: GameRule) -> float:
        count = 0
        for set in self.sets:
            board = [self.tiles[i] if i >= 0 else None for i in set]
            result = rule.evaluate(board)
            if result.count(rule.rejected) == 0:
                count += 1
        return count
        
    def _evaluate(self, tiles: tuple[int,...]):
        board = [self.tiles[i] if i >= 0 else None for i in tiles]
        result = self.rule.evaluate(board)
        if result.count(self.rule.rejected) == 0:
            self.count += 1

class UniqueSolutionsFactory(RuleEvaluatorFactory):
    def create(self, tiles2win: int, tiles: tuple[dict]) -> RuleEvaluator:
        return UniqueSolutions(tiles2win, tiles)