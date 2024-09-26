import argparse
import pygame
from pygame.locals import *
import math
from yoli_sim.envs.tile import Tile
from yoli_sim import YoliTileGame, MatchTwo, YoliBoardSim

class PlayYoli:
    def __init__(self, size:int = 5, game: YoliTileGame = MatchTwo()) -> None:
        self.window_size = 512*1.5
        self._sim = YoliBoardSim(size, game)

        self.window = None
        self.clock = None
        self.selected = None
        self._selected_pos = (0, 0)
        # aliases
        self.tiles = self._sim.no_tiles
        self.size = self._sim.size

        pygame.init()
        pygame.display.init()
        self.window = pygame.display.set_mode((self.window_size, self.window_size))
        self.clock = pygame.time.Clock()

    def _calculate_sizes(self):
        # Calculate unit lengths
        self._board_tile_size = (
            self.window_size / self.size
        )  # The size of a single board grid square in pixels

        self._tile_squares = math.floor(math.sqrt(self.tiles) + 1)
        self._tile_size = (
            (self.window_size - self._board_tile_size)  / self._tile_squares
        )  # The size of a single tile grid square in pixels
        margin = 10
        padding = 2

        self._half_margin = margin / 2
        self._half_padding = padding / 2
        self._stride_space = self._board_tile_size + self._half_margin / 2
        self._board_size_outer = self._board_tile_size - margin
        self._board_size_inner = self._board_tile_size - margin - padding
        self._cell_spacing = self._half_margin + self._half_padding
        self._tile_size_outer = self._tile_size - margin
        self._tile_size_inner = self._tile_size - margin -padding

    def _tile_col_stride(self, x):
        return x * self._tile_size + self._board_tile_size / 2

    def _pix_to_board_index(self, x):
        return math.floor((x - self._half_margin) / self._board_tile_size)

    def _pix_to_col(self, x):
        return math.floor((x - self._board_tile_size / 2) / self._tile_size)

    def _pix_to_row(self, y):
        return math.floor((y - self._board_tile_size + self._half_margin) / self._tile_size)

    def _tile_row_stride(self, x):
        return x * self._tile_size + self._board_tile_size + self._half_margin

    def _board_stride(self, x):
        return x * self._board_tile_size + self._half_margin

    def _render_clean(self, canvas):
        canvas.fill((255, 255, 255))

    def _load_tiles(self) -> list[Tile]:
        tile_sprites = []
        for x in range(self.tiles):
            tile = self._sim.get_tile(x+1)
            if tile is not None:
                tile_sprites.append(Tile(tile.image, alt_text=tile.name))
        return tile_sprites

    def _render_board_frame(self, canvas, tiles: list[Tile]):
        # Setup tile sprite
        
        indication_colors = [(0,0,0), (0,255,0), (255,0,0)]
        # Setup board grid and tile objects
        for x in range(self.size):
            rect = (
                self._board_stride(x),
                self._half_margin,
                self._board_size_outer, 
                self._board_size_outer
            )
            pygame.draw.rect(
                canvas,
                indication_colors[self._sim.indications[x]],
                rect,
                2
            )
            tileIndex = self._sim.positions[x]
            if tileIndex is not None:
                tile = tiles[tileIndex]
                tile.scale(self._board_size_inner, self._board_size_inner)
                tile.transform(self._board_stride(x) + self._half_padding,
                               self._half_margin + self._half_padding)

    def _grid_coordinate(self, x):
        col = x % self._tile_squares
        row = math.floor(x / self._tile_squares)
        return (col, row)


    def _render_available_frame(self, canvas, tiles: list[Tile]):
        #Setup available tiles grid and tile objects
        for x in range(self.tiles):
            col, row = self._grid_coordinate(x)
            rect = (
                self._tile_col_stride(col),
                self._tile_row_stride(row),
                self._tile_size_outer, 
                self._tile_size_outer
            )
            pygame.draw.rect(
                canvas,
                (0, 0, 0),
                rect,
                1
            )
            if self._sim.is_tile_available(x + 1):
                tile = tiles[x]
                tile.scale(self._tile_size_inner, self._tile_size_inner)
                tile.transform(self._tile_col_stride(col) + self._half_padding,
                               self._tile_row_stride(row) + self._half_padding)

    def _render_floater(self, tiles: list[Tile]):
        if self.selected is not None:
            x, y = self._selected_pos
            tiles[self.selected].transform(x, y)

    def render(self):
        canvas = pygame.Surface((self.window_size, self.window_size))
        self._render_clean(canvas)
        self._calculate_sizes()
        tiles = self._load_tiles()
        self._render_board_frame(canvas, tiles)
        self._render_available_frame(canvas, tiles)
        self._render_floater(tiles)

        tile_sprites = pygame.sprite.Group()
        tile_sprites.add(tiles)
        tile_sprites.update()
        self.window.fill((255, 255, 255))
        pygame.event.pump()
        self.window.blit(canvas, canvas.get_rect())
        tile_sprites.draw(self.window)
        pygame.display.update()

    def _tile_at(self, x, y):
        if y < self.window_size and y > self._board_tile_size and \
           x > self._tile_col_stride(0) and x < self._tile_col_stride(self._tile_squares):
            col = self._pix_to_col(x)
            row = self._pix_to_row(y)
            tile_index = col + row * self._tile_squares
            return tile_index if tile_index < self.tiles and self._sim.is_tile_available(tile_index + 1) else None
        return None
    
    def _board_index_at(self, x, y):
        if y > 0 and y < self._board_tile_size and \
           x > self._board_stride(0) and x < self._board_stride(self.size):
            return self._pix_to_board_index(x)
        return None
    
    def place_tile(self, x, y) -> None:
        index = self._board_index_at(x, y)
        if index is None:
            self.selected = None
        elif self.selected is not None:
            if not self._sim.position_occupied(index):
                self._sim.step(index, self.selected + 1)
            self.selected = None
        elif self._sim.position_occupied(index):
            self._sim.step(index, 0)

    def board_now(self) -> list[int]:
        return [index for index in self._sim.positions]

    def board_potential(self, x, y) -> tuple[int,...]:
        board = self.board_now()
        index = self._board_index_at(x,y)
        if index is None:
            pass
        elif self.selected is not None:
            if not self._sim.position_occupied(index):
                board[index]=self.selected
        elif self._sim.position_occupied(index):
            board[index]=None
        
    def get_selected_tile_index(self) -> int:
        return self.selected
    
    def select_tile(self, x, y) -> None:
        tile = self._tile_at(x, y)
        self.selected = tile
        if tile is None:
            self.place_tile(x, y)

    def move_selected_tile(self, pos: tuple[int, int]):
        self._selected_pos = pos

    def close(self):
        if self.window is not None:
            pygame.display.quit()
            pygame.quit()
    
    @property
    def notification(self):
        return self._sim.notification
    
    @property
    def done(self):
        return self._sim.terminated

    def reset_notification(self):
        self._sim.notification = 0