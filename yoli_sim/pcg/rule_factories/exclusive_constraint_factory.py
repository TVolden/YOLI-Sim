from yoli_sim.gamerules import GameRule, ExclusiveConstraint
from yoli_sim.pcg import GameRuleFactory, GameRuleConstructionVisitor

class ExclusiveConstraintFactory(GameRuleFactory):
    def construct(self, visitor: GameRuleConstructionVisitor) -> GameRule:
        key = visitor.property_key()
        value = visitor.property_value(key)
        return ExclusiveConstraint(key, value)