import numpy as np

class YoliBoardAnalyzer:
    def __init__(self, board_size) -> None:
        self.board_size = board_size
    
    def is_empty(self, board: np.array):
        return board[:self.board_size].count(0)==0
    