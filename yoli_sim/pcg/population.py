from yoli_sim.eval import RuleEvaluator
from yoli_sim.pcg import GameRule, RuleGenerator

class Specimen:
    def __init__(self, rule:GameRule) -> None:
        self.rule = rule
        self.value = 0   

class Population:
    def __init__(self, rule_gen:RuleGenerator) -> None:
        self.rule_gen = rule_gen

    @property
    def population_size(self):
        return len()

    def generate(self, population:int) -> None:
        self._population = [Specimen(self.rule_gen.generate_rule()) for i in range(population)]

    def evaluate_population(self, evaluator:RuleEvaluator):
        for specimen in self._population:
            specimen.value = evaluator.evaluate(specimen.rule)