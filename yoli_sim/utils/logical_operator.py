from abc import ABC, abstractmethod

class LogicalOperator (ABC):
    def __init__(self, accepted_value=1, ignored_value=0, rejected_value=-1) -> None:
        self.accepted=accepted_value
        self.ignored=ignored_value
        self.rejected=rejected_value

    @abstractmethod
    def compare(self, first:int, second:int) -> int:
        ...

    @abstractmethod
    def __str__(self) -> str:
        ...