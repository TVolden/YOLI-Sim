from yoli_sim.pcg import RuleGenerator
from yoli_sim.gamerules import GameRule
from yoli_sim.pcg.population import Population
from yoli_sim.eval import UniqueSolutions, TargetValueDecorator, ImmediateEffectCutoff, EntropyEvaluator, NormalizedTargetValueDecorator
from yoli_sim.pcg.population_selector import SelectorComposite, HighestValueSelector
from yoli_sim.pcg.roulette_selector import *
   
class GeneticRuleGenerator(RuleGenerator):
        def __init__(
                    self, 
                    generator:RuleGenerator,
                    target:float = 0.5,
                    max_generations:int = 50,
                    population_size:int = 100,
                    mutation_rate:float = 0.5) -> None:
            self._generator = generator
            self._target = target
            self._generations = max_generations
            self._size = population_size
            self._mutation_rate = mutation_rate
            self._tolerance = 0.001
        
        def set_target(self, target:float) -> None:
              self._target = target

        def generate_rule(self, board: tuple[dict, ...], tiles: tuple[dict, ...] = None) -> GameRule:
            if tiles is None:
                tiles = board
            pop = Population(self._size, self._generator)
            pop.generate(board)

            for generation in range(self._generations):
                pop.evaluate(
                    ImmediateEffectCutoff(
                        NormalizedTargetValueDecorator(
                            #UniqueSolutions(5, tiles)
                            EntropyEvaluator(board, tiles),
                            self._target),
                        board))
                
                pop.scale(SelectorComposite([HighestValueSelector(1), RouletteSelector(self._size - 1)]))
                pop.sort()
                if generation == self._generations - 1 or \
                    pop.top.value > 1-self._tolerance:
                      break
                
                pop.mutate(self._mutation_rate, 1)

            return pop.top.rule