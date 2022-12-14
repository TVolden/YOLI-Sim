from distutils.errors import DistutilsClassError
import gymnasium as gym
from gymnasium import spaces
import pygame
import numpy as np
import math
from .tile import Tile
from .tile_master import TileMaster
from .match import MatchTwo
from .onehotgenerator import OneHotGenerator


class YoliGameEnv(gym.Env):
    metadata = {"render_modes": ["human", "rgb_array"], "render_fps": 4}

    def __init__(self, render_mode=None, size=5, tile_master: TileMaster = MatchTwo()):
        self.size = size
        self.master = tile_master
        self.tiles = tile_master.tile_count()
        self.window_size = 512  # The size of the PyGame window

        # One-hot encoding
        self.observation_space = spaces.Box(low = 0,  high = 1, shape = (size * (self.tiles+1),), dtype=np.uint8)
        self.action_space = spaces.Discrete(size * (self.tiles+1))

        assert render_mode is None or render_mode in self.metadata["render_modes"]
        self.render_mode = render_mode

        self.window = None
        self.clock = None

    def _get_obs(self):
        oh = np.zeros((self.size, self.tiles + 1), dtype=np.uint8)
        oh[range(self.size), self._positions] = 1
        return oh.flatten()

    def _get_info(self):
        return {
            "notification": self._notification, #global notification, 0=nothing, 1=success, 2=failure
            "indications": tuple(self._indications) #0=nothing, 1=indicated, 2=rejected
        }

    def reset(self, seed=None, options=None):
        #super().reset(seed=seed)

        self._positions = np.array([0] * self.size)
        self._indications = [0] * self.size
        self._notification = 0

        observation = self._get_obs()
        info = self._get_info()

        if self.render_mode == "human":
            self._render_frame()

        return observation

    def _unpack_action(self, action):
        pos = None
        tile = None
        if np.count_nonzero(action) != 1:
            raise Exception("Illegal action. Multiple moves.")
        else:
            # Find coordinate
            pos = action % (self.tiles + 1)
            tile = math.floor(action / (self.tiles + 1))
            if tile > 0 and np.count_nonzero(self._positions == tile) > 0:
                raise Exception("Illegal action. Tile already placed.")
        return pos, tile
    
    def step(self, action):
        reward = 0
        terminated = False

        try:
            pos, tile = self._unpack_action(action)
            self._positions[pos] = tile
            board = [i-1 if i > 0 else None for i in self._positions]
            self._indications, terminated = self.master.evaluate(board)
            self._positions[np.where(np.array(self._indications)==2)]=0
            self._notification = 1 if terminated else 0
        
            if terminated:
                reward = 1
        except:
            reward = -1

        observation = self._get_obs()
        info = self._get_info()

        if self.render_mode == "human":
            self._render_frame()

        return observation, reward, terminated, info
  
    def render(self, mode = None):
        if mode == "human":
            old_mode = self.render_mode
            self.render_mode = mode
            self._render_frame()
            self.render_mode = old_mode
            
        if self.render_mode == "rgb_array":
            return self._render_frame()

    def _render_frame(self):
        if self.window is None and self.render_mode == "human":
            pygame.init()
            pygame.display.init()
            self.window = pygame.display.set_mode((self.window_size, self.window_size))
        if self.clock is None and self.render_mode == "human":
            self.clock = pygame.time.Clock()
        
        canvas = pygame.Surface((self.window_size, self.window_size))
        canvas.fill((255, 255, 255))
        
        # Calculate unit lengths
        board_pix_square_size = (
            self.window_size / self.size
        )  # The size of a single board grid square in pixels

        tile_squares = math.floor(math.sqrt(self.tiles) + 1)
        tile_pix_square_size = (
            (self.window_size - board_pix_square_size)  / tile_squares
        )  # The size of a single tile grid square in pixels
        margin = 10
        padding = 2

        # Setup tile sprite
        tile_sprites = pygame.sprite.Group()
        
        # Setup board grid and tile objects
        for x in range(self.size):
            rect = (
                x * board_pix_square_size + margin / 2,
                margin / 2,
                board_pix_square_size - margin, 
                board_pix_square_size - margin
            )
            pygame.draw.rect(
                canvas,
                (0, 0, 0),
                rect,
                1
            )
            pos = self._positions[x]
            if pos > 0:
                img = self.master.tile_at(pos).get("image") if self.tiles > pos else ""
                object_ = Tile(img, board_pix_square_size-margin-padding, board_pix_square_size-margin-padding)
                object_.rect.x = x * board_pix_square_size + margin / 2 + padding / 2
                object_.rect.y = margin / 2 + padding / 2
                tile_sprites.add(object_)
        
        #Setup available tiles grid and tile objects
        for x in range(self.tiles):
            col = x % tile_squares
            row = math.floor(x / tile_squares)
            rect = (
                col * tile_pix_square_size + board_pix_square_size / 2,
                row * tile_pix_square_size + board_pix_square_size + margin / 2,
                tile_pix_square_size - margin, 
                tile_pix_square_size - margin
            )
            pygame.draw.rect(
                canvas,
                (0, 0, 0),
                rect,
                1
            )
            pos = x+1
            if pos not in self._positions:
                img = self.master.tile_at(pos).get("image") if self.tiles > pos else ""
                object_ = Tile(img, tile_pix_square_size-margin-padding, tile_pix_square_size-margin-padding)
                object_.rect.x = col * tile_pix_square_size + board_pix_square_size / 2 + padding / 2
                object_.rect.y = row * tile_pix_square_size + board_pix_square_size + margin / 2 + padding / 2
                tile_sprites.add(object_)

        if self.render_mode == "human":
            tile_sprites.update()
            self.window.fill((255, 255, 255))
            pygame.event.pump()
            self.window.blit(canvas, canvas.get_rect())
            tile_sprites.draw(self.window)
            pygame.display.update()

            self.clock.tick(self.metadata["render_fps"])
        else:  # rgb_array
            return np.transpose(
                np.array(pygame.surfarray.pixels3d(canvas)), axes=(1, 0, 2)
            )

    def close(self):
        if self.window is not None:
            pygame.display.quit()
            pygame.quit()