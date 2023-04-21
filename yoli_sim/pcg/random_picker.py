from random import Random

class RandomPicker():
    def __init__(self) -> None:
        self._random = Random()
        
    def pick_one(self, list: tuple[object, ...]) -> object:
        return self._random.choice(list)