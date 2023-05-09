from abc import ABC, abstractmethod
from yoli_sim.pcg.specimen import Specimen

class PopulationSelector(ABC):
    def select(self, specimens:tuple[Specimen,...]) -> list[Specimen]:
        ...

class HighestValueSelector(PopulationSelector):
    def __init__(self, limit:int) -> None:
        self.limit = limit

    def select(self, specimens: tuple[Specimen, ...]) -> list[Specimen]:
        sorted = list(specimens)
        sorted.sort(key=lambda x: x.value, reverse=True)
        return sorted[:self.limit]

class SelectorComposite(PopulationSelector):
    def __init__(self, selectors:tuple[PopulationSelector,...]) -> None:
        self.selectors = selectors

    def select(self, specimens: tuple[Specimen, ...]) -> list[Specimen]:
        return [s for selector in self.selectors for s in selector.select(specimens)]

class ClosestToTargetSelector(PopulationSelector):
    def __init__(self, limit:int, target:int) -> None:
        self.limit = limit
        self.target = target

    def select(self, specimens: tuple[Specimen, ...]) -> list[Specimen]:
        sorted = list(specimens)
        sorted.sort(key=lambda x: abs(x.value-self.target))
        return sorted[:self.limit]