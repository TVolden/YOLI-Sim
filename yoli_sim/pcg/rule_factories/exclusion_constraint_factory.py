from yoli_sim.gamerules import GameRule, ExclusionConstraint
from yoli_sim.pcg import GameRuleFactory, GameRuleConstructionVisitor

class ExclusionConstraintFactory(GameRuleFactory):
    def construct(self, visitor: GameRuleConstructionVisitor) -> GameRule:
        key = visitor.property_key()
        value = visitor.property_value(key)
        return ExclusionConstraint(key, value)
    
