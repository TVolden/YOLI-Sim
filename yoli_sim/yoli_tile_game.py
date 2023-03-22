import random
from abc import ABC, abstractproperty, abstractclassmethod

class YoliTile:
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def image(self) -> str:
        return self._image

    def __init__(self, name, image):
        self._name = name
        self._image = image

class YoliTileGame(ABC):
    ACCEPTED = 1
    IGNORED = 0
    REJECTED = -1
    
    @abstractclassmethod
    def tile_at(self, position:int) -> YoliTile:
        ...
    
    @abstractclassmethod
    def evaluate(self, positions: tuple()) -> tuple():
        ...        

    def __init__(self):
        self._tiles = []

    def count_tiles(self) -> int:
        return len(self._tiles)

    def shuffle_tiles(self) -> None:
        random.shuffle(self._tiles)