from yoli_sim.pcg import RuleGenerator, GameRuleFactory, RandomPicker, RandomVisitorFactory
from yoli_sim.gamerules import GameRule
   
class EffectiveGenerator(RuleGenerator):
    def __init__(self, decoratee:RuleGenerator, at_least_affect=1):
        super().__init__()
        self._decoratee = decoratee
        self.affect = at_least_affect

    def generate_rule(self, board: tuple[dict, ...], tiles: tuple[dict, ...] = None) -> GameRule:
        if tiles is None:
            tiles = board
        rule:GameRule = self._decoratee.generate_rule(board)
        while rule.evaluate(board).count(rule.rejected) < self.affect:
            rule:GameRule = self._decoratee.generate_rule(board)
        return rule