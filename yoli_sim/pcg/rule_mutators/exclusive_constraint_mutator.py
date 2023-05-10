from yoli_sim.gamerules import GameRule, ExclusiveConstraint
from yoli_sim.pcg.rule_mutators import GameRuleMutator
from yoli_sim.pcg import GameRuleConstructionVisitor
from yoli_sim.pcg.rule_factories import ExclusiveConstraintFactory

class ExclusiveConstraintMutator(GameRuleMutator):
    def __init__(self, rule:ExclusiveConstraint, visitor:GameRuleConstructionVisitor):
        super().__init__(rule)
        self.rule = rule
        self.visitor = visitor

    def mutate(self) -> GameRule:
        coin = self.visitor.pick([True, False])
        key = self.rule._allowed_key
        if coin:
            key = self.visitor.property_key([self.rule._allowed_key])
        
        value = self.visitor.property_value(key,
                                            [self.rule._allowed_value])
        
        return ExclusiveConstraint(key, value)
            
class MutableExclusiveConstraintFactory(ExclusiveConstraintFactory):
    def construct(self, visitor: GameRuleConstructionVisitor) -> GameRule:
        return ExclusiveConstraintMutator(super().construct(visitor), visitor)