from yoli_sim.gamerules import GameRule, PopulationConstraint
from yoli_sim.pcg import GameRuleFactory, GameRuleConstructionVisitor

class PopulationConstraintFactory(GameRuleFactory):
    def construct(self, visitor: GameRuleConstructionVisitor) -> GameRule:
        limit = visitor.decimal(1,4)
        key = visitor.property_key()
        value = visitor.property_value(key)
        return PopulationConstraint(limit, key, value)
        