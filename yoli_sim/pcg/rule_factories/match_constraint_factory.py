from yoli_sim.gamerules import GameRule, MatchConstraint
from yoli_sim.pcg import GameRuleFactory, GameRuleConstructionVisitor

class MatchConstraintFactory(GameRuleFactory):
    def construct(self, visitor: GameRuleConstructionVisitor) -> GameRule:
        key = visitor.property_key()
        return MatchConstraint(key)