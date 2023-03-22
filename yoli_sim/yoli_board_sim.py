from yoli_sim import YoliTileGame, YoliTile
import numpy as np

class YoliBoardSim:
    @property
    def positions(self) -> tuple():
        return ([pos for pos in self._positions])

    @property
    def indications(self) -> tuple():
        return tuple(self._indications)
    
    @property
    def available_tiles(self) -> tuple():
        return tuple([tile for tile in range(1, self.no_tiles + 1) if tile not in self.positions])
    
    def __init__(self, size, game:YoliTileGame):
        self.size = size
        self.set_game(game)
        self.reset()

    def set_game(self, game:YoliTileGame):
        self._game = game
        self.no_tiles = game.count_tiles()

    def is_tile_available(self, tile):
        return tile in self.available_tiles

    def position_occupied(self, pos) -> bool:
        return self._positions[pos] != 0
    
    def get_tile(self, tileIndex):
        return self._game.tile_at(tileIndex - 1)
    
    def get_tile_at(self, pos) -> YoliTile:
        tile = self._positions[pos]
        if tile == 0:
            return None
        else:
            return self._game.tile_at(tile - 1)

    def reset(self):
        self._positions = np.array([0] * self.size)
        self._indications = [0] * self.size
        self.notification = 0
    
    def shuffle_tiles(self):
        self._game.shuffle_tiles()

    def step(self, pos, tile):
        self._gate_input(pos, tile)

        self._positions[pos] = tile
        # Create a board representation where No-Tile (0) indicator is replaced with None
        board = [i-1 if i > 0 else None for i in self._positions]
        self._indications, self.terminated = self._game.evaluate(board)
        self._positions[np.where(np.array(self._indications)==-1)] = 0
        self.notification = 1 if self.terminated else 0
    
    def _gate_input(self, pos, tile):
        if tile > 0 and self.position_occupied(pos):
            raise Exception("Illegal action. Tiles can't be replaced with other tiles, only removed.")
        if tile == 0 and self.position_occupied(pos) == False:
            raise Exception("Illegal action. No tile to remove.")
        if tile > 0 and self.is_tile_available(tile) == False:
            raise Exception("Illegal action. Tile already placed.")