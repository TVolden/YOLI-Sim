import numpy as np
import random
from typing import Union

class OneHotGenerator(np.random.Generator):
    def __init__(self):
        seed_seq = np.random.SeedSequence()
        np_seed = seed_seq.entropy
        super().__init__(np.random.PCG64(np_seed))

    def integers(self, low, high, size: Union[int, tuple, list, np.array] , dtype):
        output = np.full(size, low, dtype)

        if isinstance(size, (tuple, list, np.array)):
            size = len(size)
            coords = [0] * len(size)
            for i in range(len(size)):
                coords[i] = random.randrange(0, size[i])
            output.itemset(tuple(coords), high-1)
        else:
            output[random.randrange(0, size)]=high-1
        return output
        
