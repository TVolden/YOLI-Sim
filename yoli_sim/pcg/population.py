from yoli_sim.eval import RuleEvaluator
from yoli_sim.pcg import RuleGenerator
from yoli_sim.pcg.population_selector import PopulationSelector
from yoli_sim.pcg.specimen import Specimen
import random
from threading import Thread
import time, os

class Proc:
    def __init__(self) -> None:
        self.active = False
        self.specimen = None
    
    def assign(self, specimen:Specimen, thread:Thread):
        self.active = True
        self.specimen = specimen
        self.tread = thread

    def eval(self, evaluator:RuleEvaluator):
        self.specimen.value = evaluator.evaluate(self.specimen.rule)
        self.active = False

class Population:
    def __init__(self, size, rule_gen:RuleGenerator) -> None:
        self.rule_gen = rule_gen
        self.population_size = size
        self.reset()
    
    @property
    def top(self) -> Specimen:
        return self._population[0]
    
    def reset(self):
        self._population = []

    def generate(self, tile_examples:tuple[dict,...]) -> None:
        for i in range(self.population_size - len(self._population)):
            self._population.append(Specimen(self.rule_gen.generate_rule(tile_examples)))

    def evaluate(self, evaluator:RuleEvaluator, force:bool=False):
        self._parallel_evaluate(evaluator, force)

    def sort(self):
        self._population.sort(key=lambda x: x.value, reverse=True)

    def _serial_evaluate(self, evaluator:RuleEvaluator, force:bool=False):
        for specimen in self._population:
            if force or specimen.value == 0:
                specimen.value = evaluator.evaluate(specimen.rule)

    def _parallel_evaluate(self, evaluator:RuleEvaluator, force:bool=False):
        procs = [Proc() for _ in range(os.cpu_count())]
        for specimen in self._population:
            if force or specimen.value == 0:
                available = [proc for proc in procs if proc.active == False]
                while len(available) == 0:
                    time.sleep(0.01)
                    available = [proc for proc in procs if proc.active == False]

                thread = Thread(target=available[0].eval, args=[evaluator])
                available[0].assign(specimen, thread)
                thread.start()
        
        available = [proc for proc in procs if proc.active]
        while len(available) == 0:
            available[0].thread.join()
            available = [proc for proc in procs if proc.active]

    def scale(self, selector:PopulationSelector):
        self._population = selector.select(self._population)

    def clone(self):
        self._population = [s.clone() for s in self._population]

    def mutate(self, probability:float = 0.5, skip:int=0):
        mutations = 0
        for i in range(skip, len(self._population)):
            if probability >= random.random():
                specimen = self._population[i].clone()
                specimen.mutate()
                self._population[i] = specimen
                mutations += 1
        return mutations
    
    def reset_values(self):
        for specimen in self._population:
            specimen.value = 0