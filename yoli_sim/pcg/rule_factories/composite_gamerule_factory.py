from yoli_sim.gamerules import GameRule, CompositeGameRule
from yoli_sim.pcg import GameRuleFactory, GameRuleConstructionVisitor

class CompositeGameRuleFactory(GameRuleFactory):
    def __init__(self, factories:tuple[GameRuleFactory,...], min=1, max=2) -> None:
        super().__init__()
        self.factories = factories
        self.min = min
        self.max = max

    def construct(self, visitor: GameRuleConstructionVisitor) -> GameRule:
        rules = []
        for i in range(self.max):
            if i < self.min or visitor.pick([True, False]):
                rule = visitor.pick(self.factories).construct(visitor)
                rules.append(rule)

        return CompositeGameRule(rules)
    