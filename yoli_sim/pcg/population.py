from yoli_sim.eval import RuleEvaluator
from yoli_sim.pcg import RuleGenerator
from yoli_sim.pcg.population_selector import PopulationSelector
from yoli_sim.pcg.specimen import Specimen
import random

class Population:
    def __init__(self, size, rule_gen:RuleGenerator) -> None:
        self.rule_gen = rule_gen
        self.population_size = size
        self.reset()
        
    def reset(self):
        self._population = []

    def generate(self, tile_examples:tuple[dict,...]) -> None:
        for i in range(self.population_size - len(self._population)):
            self._population.append(Specimen(self.rule_gen.generate_rule(tile_examples)))

    def evaluate(self, evaluator:RuleEvaluator):
        for specimen in self._population:
            specimen.value = evaluator.evaluate(specimen.rule)

    def scale(self, selector:PopulationSelector):
        self._population = selector.select(self._population)

    def clone(self, no_clones:int, trim:bool = True):
        self._population = self._population * no_clones
        
        if trim:
            self._population = self._population[:self.population_size]

    def mutate(self, probability:float = 0.5, skip:int=0):
        for specimen in self._population[skip:]:
            if probability >= random.random():
                specimen.mutate()