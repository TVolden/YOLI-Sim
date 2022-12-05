import gymnasium as gym
import numpy as np

class OneHotEncoding(gym.Space):
    def __init__(self, rows=2, columns=2):
        self.rows = rows
        self.columns = columns
        gym.Space.__init__(self, (), np.int64)

    def sample(self):
        one_hot_vector = np.zeros((self.rows, self.columns))
        one_hot_vector[np.random.randint(self.rows), np.random.randint(self.columns)] = 1
        return one_hot_vector

    def contains(self, x):
        if isinstance(x, (list, tuple, np.ndarray)) and self.__eq__(x):
            m = np.array(x)
            return np.count_nonzero(m == 1) == 1 and np.count_nonzero(m == 0) == self.rows * self.columns - 1
        else:
            return False

    def __repr__(self):
        return f"OneHotEncoding({self.rows}, {self.columns})"

    def __eq__(self, other):
        return np.array(other).shape == (self.rows, self.columns)