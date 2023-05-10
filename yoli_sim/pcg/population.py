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

    def evaluate(self, evaluator:RuleEvaluator, force:bool=False):
        for specimen in self._population:
            if force or specimen.value == 0:
                specimen.value = evaluator.evaluate(specimen.rule)

    def scale(self, selector:PopulationSelector):
        self._population = selector.select(self._population)

    def clone(self):
        self._population = [s.clone() for s in self._population]

    def mutate(self, probability:float = 0.5, skip:int=0):
        for i in range(skip, len(self._population)):
            if probability >= random.random():
                specimen = self._population[i].clone()
                specimen.mutate()
                self._population[i] = specimen
    
    def reset_values(self):
        for specimen in self._population:
            specimen.value = 0