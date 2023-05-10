from yoli_sim.gamerules import GameRule, PopulationConstraint
from yoli_sim.pcg.rule_mutators import GameRuleMutator
from yoli_sim.pcg import GameRuleConstructionVisitor
from yoli_sim.pcg.rule_factories import PopulationConstraintFactory

class PopulationConstraintMutator(GameRuleMutator):
    def __init__(self, rule:PopulationConstraint, visitor:GameRuleConstructionVisitor):
        super().__init__(rule)
        self.rule = rule
        self.visitor = visitor

    def mutate(self) -> GameRule:
        d3 = self.visitor.pick([1,2,3])
        key = self.rule._key
        value = self.rule._value
        limit = self.rule._limit
        if d3 % 2 != 0:
            if d3 == 1:
                key = \
                    self.visitor.property_key([self.rule._key])
            value = \
                 self.visitor.property_value(key,
                                             [self.rule._value])
        else:
            limit = \
                self.visitor.pick([i for i in range(1, 4) if i != self.rule._limit])
        
        return PopulationConstraintMutator(PopulationConstraint(limit, key, value), self.visitor)
            
class MutablePopulationConstraintFactory(PopulationConstraintFactory):
    def construct(self, visitor: GameRuleConstructionVisitor) -> GameRule:
        return PopulationConstraintMutator(super().construct(visitor), visitor)