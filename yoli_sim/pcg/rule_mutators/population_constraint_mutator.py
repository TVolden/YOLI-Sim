from yoli_sim.gamerules import GameRule, PopulationConstraint
from yoli_sim.pcg.rule_mutators import GameRuleMutator
from yoli_sim.pcg import GameRuleConstructionVisitor
from yoli_sim.pcg.rule_factories import PopulationConstraintFactory

class PopulationConstraintMutator(GameRuleMutator):
    def __init__(self, rule:PopulationConstraint, visitor:GameRuleConstructionVisitor):
        super().__init__(rule)
        self.rule = rule
        self.visitor = visitor

    def mutate(self) -> None:
        d3 = self.visitor.pick([1,2,3])
        if d3 % 2 != 0:
            if d3 == 1:
                self.rule._key = \
                    self.visitor.property_key([self.rule._key])
            self.rule._value = \
                 self.visitor.property_value(self.rule._key,
                                             [self.rule._value])
        else:
            self.rule._limit = \
                self.visitor.pick([i for i in range(1, 4) if i != self.rule._limit])
            
class MutablePopulationConstraintFactory(PopulationConstraintFactory):
    def construct(self, visitor: GameRuleConstructionVisitor) -> GameRule:
        return PopulationConstraintMutator(super().construct(visitor), visitor)