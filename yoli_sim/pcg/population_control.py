from yoli_sim.pcg import GameRule
from yoli_sim.utils import GameDifficultyAnalyzer

class Specimen:
    def __init__(self, rule:GameRule, analyzer:GameDifficultyAnalyzer) -> None:
        self.rule = rule
        self.analyzer = analyzer
        self.value = 0
    
    def evaluate(self, tiles2win:int, tiles:tuple[dict,...]) -> None:
        self.value = self.analyzer.determine_difficulty(tiles2win, self.rule, tiles)

class PopulationControl:
    def __init__(self, size:int, tiles:tuple[dict,...], ) -> None:
        self.size = size
        self.tiles = tiles

    def generate(self) -> None:
        ...