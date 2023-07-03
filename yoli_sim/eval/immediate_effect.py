from yoli_sim.eval import RuleEvaluator
from yoli_sim.gamerules import GameRule

class ImmediateEffectCutoff(RuleEvaluator):
    def __init__(self, evaluator:RuleEvaluator, board:tuple[dict]) -> None:
        super().__init__()
        self.evaluator = evaluator
        self.board = board
    
    def evaluate(self, rule: GameRule) -> float:
        result = rule.evaluate(self.board)
        if result.count(rule.rejected) > 0:
            return self.evaluator.evaluate(rule)
        return 0