from abc import ABC, abstractmethod
from yoli_sim.gamerules import *
from yoli_sim.utils import SetGenerator

class GameDifficultyAnalyzer(ABC):
    @abstractmethod
    def determine_difficulty(self, tiles2win:int, rule:GameRule, tiles: tuple[dict,...]):
        ...

class DifficultyByUniqueSolutionsOrderMatters(GameDifficultyAnalyzer):
    def determine_difficulty(self, tile2win:int, rule:GameRule, tiles: tuple[dict,...]):
        self.rule = rule
        self.tiles = tiles
        board = [-1] * tile2win
        tiles = range(len(self.tiles))
        sum = 0
        for pos in range(len(board)):
            for tile in tiles:
                new_board = [-1] * tile2win
                new_board[pos] = tile
                new_tiles = [t for t in tiles if t != tile]
                sum += self._combine(new_board, new_tiles)
        return sum

    def _combine(self, board: tuple[int,...], tiles: tuple[int,...]):
        if board.count(-1) == 0:
            return 1 if self._evaluate(board) else 0
        else:
            sum = 0
            for i, pos in enumerate(board):
                if pos == -1:
                    for tile in tiles:
                        new_board = [n for n in board]
                        new_board[i] = tile
                        new_tiles = [t for t in tiles if t != tile]
                        sum += self._combine(new_board, new_tiles)

            return sum

    def _evaluate(self, tiles: tuple[int,...]):
        board = [self.tiles[i] if i >= 0 else None for i in tiles]
        result = self.rule.evaluate(board)
        return result.count(self.rule.rejected) == 0
    
class DifficultyByUniqueSolutions(GameDifficultyAnalyzer):
    def determine_difficulty(self, tile2win:int, rule:GameRule, tiles: tuple[dict,...]):
        self.rule = rule
        self.tiles = tiles
        tiles = range(len(self.tiles))
        self.count = 0
        gen = SetGenerator(tile2win, len(tiles))
        gen.generate(self._evaluate)
        return self.count
        
    def _evaluate(self, tiles: tuple[int,...]):
        board = [self.tiles[i] if i >= 0 else None for i in tiles]
        result = self.rule.evaluate(board)
        if result.count(self.rule.rejected) == 0:
            self.count += 1