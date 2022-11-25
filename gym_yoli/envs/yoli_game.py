from distutils.errors import DistutilsClassError
import gymnasium as gym
from gymnasium import spaces
import pygame
import numpy as np
import math

class YoliGameEnv(gym.Env):
    metadata = {"render_modes": ["human", "rgb_array"], "render_fps": 4}

    def __init__(self, render_mode=None, size=5, tiles=30):
        self.size = size
        self.tiles = tiles
        self.window_size = 512  # The size of the PyGame window

        # One-hot encoding
        self.observation_space = spaces.Box(low=0, high=1, shape=[size, tiles+1], dtype=np.bool8)
        self.action_space = spaces.Box(low=0, high=1, shape=[size, tiles+1], dtype=np.bool8)

        self._action_tiles = [
            None,
            {"name": "Shape", "group": 1, "order": 1},
            {"name": "Circle", "group": 1, "order": 2},
            {"name": "Animal", "group": 2, "order": 1},
            {"name": "Lion", "group": 2, "order": 2}
        ]

        assert render_mode is None or render_mode in self.metadata["render_modes"]
        self.render_mode = render_mode

        self.window = None
        self.clock = None

    def _get_obs(self):
        oh = np.zeros((self.size, self.tiles + 1))
        oh[range(self.size), self._positions] = 1
        return oh

    def _get_action_mask(self):
        mask = np.zeros((self.size, self.tiles + 1))
        
        # Make a list of available tiles
        available_tiles = [0]+[0 if tile in self._positions else 1 for tile in range(self.tiles)]

        for i in range(self.size):
            if self._positions[i]==0:
                mask[i] = available_tiles # Must place a tile which is not already used
            else:
                mask[i, 0] = 1 # Only allow removal of a tile

    def _get_info(self):
        return {
            "notification": self._notification, #global notification, 0=nothing, 1=success, 2=failure
            "indications": tuple(self._indications) #0=nothing, 1=indicated, 2=rejected
        }

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)

        self._positions = np.array([0] * self.size)
        self._indications = [0] * self.size
        self._notification = 0

        observation = self._get_obs()
        info = self._get_info()

        if self.render_mode == "human":
            self._render_frame()

        return observation, info

    def step(self, action):
        truncated = False
        a = np.array(action)
        
        if np.count_nonzero(a == 1) != 1:
            truncated = True
        
        self._notification = 0
        self._indications = [0] * self.size

        # Perform action
        self._positions[action.position] = action.tile
        
        self._match()

        terminated = self._notification == 1
        reward = 1 if terminated else 0  # Binary sparse rewards
        observation = self._get_obs()
        info = self._get_info()

        if self.render_mode == "human":
            self._render_frame()

        return observation, reward, terminated, truncated, info

    def _match(self):
        group = None
        for i in range(self.size):
            pos = self._positions[i]
            tile = self._action_tiles[pos]
            if tile is not None:
                if group is None:
                    group = tile.group
                    self._indications[i] = 1 # Accept
                elif group != tile.group: 
                    self._positions[i] = 0
                    self._indications[i] = 2 # Rejected
                else:
                    self._indications[i] = 1 # Accept
                    self._notification = 1 # Win

    def render(self):
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
        
        # Calculate unit lenghts
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
                img = self._action_tiles[pos].get("image") if len(self._action_tiles) > pos else ""
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
            if pos not in self.positions:
                img = self._action_tiles[pos].get("image") if len(self._action_tiles) > pos else ""
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