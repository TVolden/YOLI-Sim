from yoli_sim.gamerules import GameRule
from abc import ABC, abstractmethod

class RuleGenerator(ABC):
    def __init__(self):
        ...
    
    @abstractmethod
    def generate_rule(self, board:tuple[dict, ...], tiles:tuple[dict,...]) -> GameRule:
        ...