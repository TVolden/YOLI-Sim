from yoli_sim.gamerules import GameRule, CompositeGameRule
from yoli_sim.pcg.rule_mutators import GameRuleMutator
from yoli_sim.pcg import GameRuleConstructionVisitor, GameRuleFactory
from yoli_sim.pcg.rule_factories import CompositeGameRuleFactory

class CompositeGameRuleMutator(GameRuleMutator):
    def __init__(self, 
                 rule: CompositeGameRule, 
                 visitor:GameRuleConstructionVisitor,
                 factories:tuple[GameRuleFactory,...]):
        super().__init__(rule)
        self.rule = rule
        self.visitor = visitor
        self.factories = factories

    def mutate(self) -> GameRule:
        comparer = self.rule._comparer
        
        options = [self._mutate_rule, self._add_rule]
        if len(self.rule._rules) > 1:
            options.append(self._remove_rule)

        rules = self.visitor.pick(options)(self.rule._rules)
        return CompositeGameRuleMutator(CompositeGameRule(rules, comparer), self.visitor, self.factories)
    
    def _add_rule(self, rules:list[GameRule]) -> list[GameRule]:
        rule = self.visitor.pick(self.factories).construct(self.visitor)
        return rules + [rule]

    def _remove_rule(self, rules:list[GameRule]) -> list[GameRule]:
        rule = self.visitor.pick(rules)
        return [r for r in rules if r != rule]
    
    def _mutate_rule(self, rules:list[GameRule]) -> list[GameRule]:
        rule = self.visitor.pick(rules)
        if isinstance(rule, GameRuleMutator):
            return [r.mutate() if r == rule else r for r in rules]
        else:
            return rules

class MutableCompositeGameRuleFactory(CompositeGameRuleFactory):
    def __init__(self, factories: tuple[GameRuleFactory, ...], min=1, max=2) -> None:
        super().__init__(factories, min, max)

    def construct(self, visitor: GameRuleConstructionVisitor) -> GameRule:
        return CompositeGameRuleMutator(super().construct(visitor), visitor, self.factories)