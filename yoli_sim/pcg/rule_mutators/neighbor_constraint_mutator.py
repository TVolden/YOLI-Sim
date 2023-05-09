from yoli_sim.gamerules import GameRule, NeighborConstraint
from yoli_sim.pcg.rule_mutators import GameRuleMutator
from yoli_sim.pcg import GameRuleConstructionVisitor
from yoli_sim.pcg.rule_factories import NeighborConstraintFactory

class NeighborConstraintMutator(GameRuleMutator):
    def __init__(self, rule:NeighborConstraint, visitor:GameRuleConstructionVisitor):
        super().__init__(rule)
        self.rule = rule
        self.visitor = visitor

    def mutate(self) -> None:
        d4 = self.visitor.pick([1,2,3,4])
        if d4 % 2 == 0:
            if d4 == 2:
                self.rule._trigger_key = \
                    self.visitor.property_key([self.rule._trigger_key])
            self.rule._trigger_value = \
                self.visitor.property_value(self.rule._trigger_key, 
                                            [self.rule._trigger_value,
                                             self.rule._triggered_value])
        else:
            if d4 == 1:
                self.rule._triggered_key = \
                    self.visitor.property_key([self.rule._triggered_key])
            self.rule._triggered_value = \
                self.visitor.property_value(self.rule._triggered_key, 
                                            [self.rule._trigger_value,
                                             self.rule._triggered_value])

class MutableNeighborConstraintFactory(NeighborConstraintFactory):
    def construct(self, visitor: GameRuleConstructionVisitor) -> GameRule:
        return NeighborConstraintMutator(super().construct(visitor), visitor)