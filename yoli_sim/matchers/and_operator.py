from yoli_sim.matchers import Matcher, LogicalOperator

class AndOperator (LogicalOperator):
    def compare(self, first: int, second: int) -> int:
        if first != second:
            if first == self.ignored:
                return second
            if second == self.ignored:
                return first
            return self.rejected
        return first