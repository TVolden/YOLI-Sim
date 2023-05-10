from __future__ import annotations
from yoli_sim import GameRule
from yoli_sim.pcg.rule_mutators import GameRuleMutator

class Specimen:
    def __init__(self, rule:GameRule) -> None:
        self.rule = rule
        self.value = 0

    def clone(self) -> Specimen:
        return Specimen(self.rule)

    def mutate(self):
        if isinstance(self.rule, GameRuleMutator):
            self.rule = self.rule.mutate()