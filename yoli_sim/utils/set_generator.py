class SetGenerator:
    def __init__(self, size:int, items:int) -> None:
        self.size = size
        self.items = items
    
    def generate_all(self) -> tuple[tuple[int,...],...]:
        default = [-1] * self.size
        sets = []
        self.callback = lambda tiles: sets.append(tiles)
        self._iterate(self.size, self.items, 0, default)
        return tuple(sets)

    def generate(self, callback):
        self.callback = callback
        default = [-1] * self.size
        self._iterate(self.size, self.items, 0, default)
    
    def _iterate(self, window, amount, skip, current):
        if window <= 1:
            for k in range(skip, amount):
                 self.callback(self._list(current, self.size - window, k))
        else:
            for i in range(skip, amount):
                new_set = self._list(current, self.size - window, i)
                self._iterate(window-1, amount, i+1, new_set)
    
    def _list(self, current, index, value):
        return [value if i==index else n for i, n in enumerate(current)]