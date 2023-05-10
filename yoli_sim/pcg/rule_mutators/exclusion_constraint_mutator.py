from yoli_sim.gamerules import GameRule, ExclusionConstraint
from yoli_sim.pcg.rule_mutators import GameRuleMutator
from yoli_sim.pcg import GameRuleConstructionVisitor
from yoli_sim.pcg.rule_factories import ExclusionConstraintFactory

class ExclusionConstraintMutator(GameRuleMutator):
    def __init__(self, rule: ExclusionConstraint, visitor:GameRuleConstructionVisitor):
        super().__init__(rule)
        self.rule = rule
        self.visitor = visitor

    def mutate(self) -> GameRule:
        coin = self.visitor.pick([True, False])
        key = self.rule._exclusion_key
        if coin:
            key = \
                self.visitor.property_key(self.rule._exclusion_key)

        value = \
            self.visitor.property_value(key,
                                        self.rule._exclusion_value)
        return ExclusionConstraintMutator(ExclusionConstraint(key, value), self.visitor)
            
class MutableExclusionConstraintFactory(ExclusionConstraintFactory):
    def construct(self, visitor: GameRuleConstructionVisitor) -> GameRule:
        return ExclusionConstraintMutator(super().construct(visitor), visitor)