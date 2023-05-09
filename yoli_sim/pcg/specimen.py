from yoli_sim import GameRule
from yoli_sim.pcg.rule_mutators import GameRuleMutator

class Specimen:
    def __init__(self, rule:GameRule) -> None:
        self.rule = rule
        self.value = 0

    def mutate(self):
        if isinstance(self.rule, GameRuleMutator):
            self.rule.mutate()