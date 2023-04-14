from abc import ABC, abstractmethod

class Matcher(ABC):
    def __init__(self, accepted_value=1, ignored_value=0, rejected_value=-1):
        self.accepted = accepted_value
        self.ignored = ignored_value
        self.rejected = rejected_value
    
    @abstractmethod
    def match(self, tiles:tuple[dict, ...]) -> tuple[int, ...]:
        ...