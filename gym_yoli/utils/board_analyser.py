import numpy as np

class YoliBoardAnalyzer:
    def __init__(self, board_size: int) -> None:
        self.board_size = board_size
    
    def is_empty(self, board: np.array):
        return self.count_occupied(board) == 0
    
    def count_occupied(self, board: np.array):
        stride = int(board.size / self.board_size)
        count = 0
        for i in range(self.board_size):
            if board[0][i*stride] == 0:
                count += 1
        return count