import random
from yoli_sim.pcg.specimen import Specimen
from yoli_sim.pcg.population_selector import PopulationSelector

class RouletteSelector(PopulationSelector):
    def __init__(self, size:int) -> None:
        self._size = size

    def select(self, specimens: tuple[Specimen, ...]) -> list[Specimen]:
        total = sum([s.value for s in specimens])
        return [self.find_winner(random.uniform(0, total), specimens) for _ in range(self._size)]

    def find_winner(self, ticket:float, specimens: tuple[Specimen,...]) -> Specimen:
        for specimen in specimens:
            ticket -= specimen.value
            if ticket <= 0:
                return specimen