from yoli_sim.gamerules import GameRule, MatchConstraint
from yoli_sim.pcg.rule_mutators import GameRuleMutator
from yoli_sim.pcg import GameRuleConstructionVisitor
from yoli_sim.pcg.rule_factories import MatchConstraintFactory

class MatchConstraintMutator(GameRuleMutator):
    def __init__(self, rule:MatchConstraint, visitor:GameRuleConstructionVisitor):
        super().__init__(rule)
        self.rule = rule
        self.visitor = visitor

    def mutate(self) -> None:
        self.rule._matcher.key = self.visitor.property_key([self.rule._matcher.key])

class MutableMatchConstraintFactory(MatchConstraintFactory):
    def construct(self, visitor: GameRuleConstructionVisitor) -> GameRule:
        return MatchConstraintMutator(super().construct(visitor), visitor)