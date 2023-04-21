from yoli_sim.pcg import RuleGenerator, GameRuleFactory, RandomPicker, RandomVisitorFactory
from yoli_sim.gamerules import GameRule
   
class RandomRuleGenerator(RuleGenerator):
    def __init__(
            self, 
            game_rules: list[GameRuleFactory],
            random_picker:RandomPicker = RandomPicker(),
            visitor_factory:RandomVisitorFactory = RandomVisitorFactory()):
        super().__init__()
        self._rules = game_rules
        self._random = random_picker
        self._factory = visitor_factory

    def generate_rule(self, tiles:tuple[dict,...]) -> GameRule:
        # Gate: There must be at least one rule to pick among
        if len(self._rules) == 0:
            raise NoRulesException("There must be at least one rule to pick among.")
        visitor = self._factory.construct(tiles)
        return self._random.pick_one(self._rules).construct(visitor)

class NoRulesException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)