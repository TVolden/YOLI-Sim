from yoli_sim.gamerules import GameRule
from yoli_sim.utils import LogicalOperator, AndOperator

class CompositeGameRule(GameRule):
    def __init__(self, rules: list[GameRule], logical_operator:LogicalOperator = AndOperator()):
        super().__init__()
        self._rules = rules
        self._comparer = logical_operator

    def add_rule(self, rule:GameRule) -> None:
        self._rules.append(rule)

    def clear(self) -> None:
        self._rules = []

    def evaluate(self, tiles: tuple[dict, ...]) -> tuple[int, ...]:
        output = [self.ignored] * len(tiles)
        for rule in self._rules:
            result = rule.evaluate(tiles)
            for i in range(len(output)):
                output[i] = self._comparer.compare(output[i], result[i])
        return tuple(output)
    
    def __str__(self) -> str:
        rules = [f"{rule} {self._comparer}" for rule in self._rules]
        out = ' '.join(rules)
        return out[:-len(str(self._comparer))-1]
    
    def entropy(self, board: tuple[dict, ...], remaining: tuple[dict, ...]) -> list[list[bool]]:
        entropy = super().entropy(board, remaining)
        for rule in self._rules:
            new_entropy = rule.entropy(board, remaining)
            entropy = [self._comparer.operate(entropy[i], new_entropy[i]) for i in range(len(entropy))]
        return entropy
