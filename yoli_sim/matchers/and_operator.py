from yoli_sim.matchers import Matcher, LogicalOperator

class AndOperator (LogicalOperator):
    def compare(self, first: int, second: int) -> int:
        if first != second:
            if first == 0:
                return second
            if second == 0:
                return first
            return Matcher.FAILED
        return first