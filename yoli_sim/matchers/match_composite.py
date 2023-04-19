from yoli_sim.matchers import Matcher
from yoli_sim.utils import LogicalOperator, AndOperator

class MatchComposite(Matcher):
    def __init__(self, matchers:list, logical_operator:LogicalOperator = AndOperator()):
        self.operator = logical_operator
        self.matchers = matchers

    def match(self, tiles:tuple) -> tuple:
        output = [self.ignored] * len(tiles)
        for matcher in self.matchers:
            result = matcher.match(tiles)
            for i in range(len(output)):
                output[i] = self.operator.compare(output[i], result[i])
        return tuple(output)