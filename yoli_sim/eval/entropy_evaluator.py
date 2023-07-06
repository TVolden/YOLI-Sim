from yoli_sim.eval import RuleEvaluator, RuleEvaluatorFactory
from yoli_sim.gamerules import GameRule

class EntropyEvaluator(RuleEvaluator):
    def __init__(self, board: tuple[dict, ...], remaining: tuple[dict, ...]) -> None:
        super().__init__()
        self._board = board
        self._remaining = remaining

    def evaluate(self, rule: GameRule) -> float:
        free_spaces = self._board.count(None)
        if free_spaces == 0:
            return 0.0 # Already solved
        else:
            entropy_per_pos = rule.entropy(self._board, self._remaining)
            if self._has_solution(free_spaces, entropy_per_pos):
                max_entropy = len(self._remaining) * free_spaces
                entropy = [tiles for pos in entropy_per_pos for tiles in pos].count(True)
                return entropy / max_entropy
            else:
                return 0.0 # Has no solution
    
    def _has_solution(self, free_spaces, entropy_per_pos) -> bool:
        # Merge entropy using or-logic
        entropy = []
        for i in range(len(self._remaining)):
            has_true = False
            for n in range(len(entropy_per_pos)):
                has_true = has_true or entropy_per_pos[n][i]
            entropy.append(has_true)
        
        return entropy.count(True) <= free_spaces

class EntropyEvaluatorFactory(RuleEvaluatorFactory):
    def create(self, _: int, board: tuple[dict, ...], remaining: tuple[dict, ...]) -> RuleEvaluator:
        return EntropyEvaluator(board, remaining)