from yoli_sim.eval import RuleEvaluator, RuleEvaluatorFactory
from yoli_sim.gamerules import GameRule

class EntropyEvaluator(RuleEvaluator):
    def __init__(self, board: tuple[dict, ...], remaining: tuple[dict, ...]) -> None:
        super().__init__()
        self.board = board
        self.remaining = remaining

    def evaluate(self, rule: GameRule) -> float:
        free_spaces = self.board.count(None)
        if free_spaces == 0:
            return 0.0 # Already solved
        else:
            max_entropy = len(self.remaining) * free_spaces
            entropy_array = rule.entropy(self.board, self.remaining)
            entropy = [tiles for pos in entropy_array for tiles in pos].count(True)
            return 1.0 - (entropy / max_entropy)

class EntropyEvaluatorFactory(RuleEvaluatorFactory):
    def create(self, _: int, board: tuple[dict, ...], remaining: tuple[dict, ...]) -> RuleEvaluator:
        return EntropyEvaluator(board, remaining)