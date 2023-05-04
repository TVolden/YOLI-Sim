from yoli_sim.pcg import RuleGenerator, GameRuleFactory, RandomPicker, RandomVisitorFactory
from yoli_sim.gamerules import GameRule
   
class EffectiveGenerator(RuleGenerator):
    def __init__(self, decoratee:RuleGenerator, at_least_affect=1):
        super().__init__()
        self._decoratee = decoratee
        self.affect = at_least_affect

    def generate_rule(self, tiles:tuple[dict,...]) -> GameRule:
        rule:GameRule = self._decoratee.generate_rule(tiles)
        while rule.evaluate(tiles).count(rule.rejected) < self.affect:
            rule:GameRule = self._decoratee.generate_rule(tiles)
        return rule