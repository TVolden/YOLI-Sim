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
            tiles = len(self.remaining)
            max_entropy = (tiles - free_spaces/2 - 1/2) * free_spaces
            return 1.0 - (rule.entropy(self.board, self.remaining) / max_entropy)

class EntropyEvaluatorFactory(RuleEvaluatorFactory):
    def create(self, _: int, board: tuple[dict, ...], remaining: tuple[dict, ...]) -> RuleEvaluator:
        return EntropyEvaluator(board, remaining)