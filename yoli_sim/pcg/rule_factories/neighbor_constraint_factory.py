from yoli_sim.gamerules import GameRule, NeighborConstraint
from yoli_sim.pcg import GameRuleFactory, GameRuleConstructionVisitor

class NeighborConstraintFactory(GameRuleFactory):
    def construct(self, visitor: GameRuleConstructionVisitor) -> GameRule:
        key1 = visitor.property_key()
        value1 = visitor.property_value(key1)

        try:
            key2 = visitor.property_key()
            value2 = visitor.property_value(key2, [value1])
        except:
            key2 = visitor.property_key([key2])
            value2 = visitor.property_value(key2, [value1])            

        return NeighborConstraint(key1, value1, key2, value2)