from yoli_sim.eval import RuleEvaluator
from yoli_sim.gamerules import GameRule

class NormalizedTargetValueDecorator(RuleEvaluator):
    def __init__(self, evaluator:RuleEvaluator, target:float) -> None:
        super().__init__()
        self.evaluator = evaluator
        self.target = target
    
    def evaluate(self, rule: GameRule) -> float:
        result = self.evaluator.evaluate(rule)
        return 1 - abs(result - self.target)