from abc import ABC, abstractmethod

class GameRuleConstructionVisitor(ABC):
    @abstractmethod
    def property_key(self, exclude_keys:list[str]=None) -> str:
        ...
    
    @abstractmethod
    def property_value(self, property_key:str, exclude_values:list[str]=None) -> str:
        ...
    
    @abstractmethod
    def decimal(self, min:int, max:int) -> int:
        ...

    @abstractmethod
    def pick(self, list:tuple[object, ...]) -> object:
        ...