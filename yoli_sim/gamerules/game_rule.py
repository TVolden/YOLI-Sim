from abc import ABC, abstractmethod

class GameRule (ABC):
    def __init__(self, accepted_value=1, ignored_value=0, rejected_value=-1):
        self.accepted = accepted_value
        self.ignored = ignored_value
        self.rejected = rejected_value

    @abstractmethod
    def evaluate(self, tiles:tuple[dict, ...]) -> tuple[int, ...]:
        ...

    @abstractmethod
    def __str__(self) -> str:
        ...

    def entropy(self, board:tuple[dict,...], tiles:tuple[dict, ...]) -> list[list[bool]]:
        return [[True] * len(tiles) if b is None else [False] * len(tiles) for b in board] # All tiles are valid for all available positions