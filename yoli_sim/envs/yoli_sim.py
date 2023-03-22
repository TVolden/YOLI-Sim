from distutils.errors import DistutilsClassError
import gym as gym
from gym import spaces
import pygame
import numpy as np
import math
from .tile import Tile
from yoli_sim import YoliTileGame, MatchTwo, YoliBoardSim
from yoli_sim.rewarders import Rewarder, TerminatedRewarder, FixedRewarder

class YoliEnvConfiguration:
    def __init__(self):
        self.size = 5
        self.rewarder = TerminatedRewarder()
        self.shuffle = False
        self.illegal_penalty = FixedRewarder(-1)
        self.illegal_termination = False

class YoliSimEnv(gym.Env):
    render_modes = ["human", "rgb_array"]
    metadata = {"render_modes": render_modes, "render.modes":render_modes, "render_fps": 4, "render.fps": 4}

    def __init__(self, 
                render_mode="rgb_array",
                size=5, 
                game: YoliTileGame = MatchTwo(), 
                rewarder: Rewarder = TerminatedRewarder(), 
                shuffle=False,
                illegal_penalty:Rewarder = FixedRewarder(-1),
                illegal_termination:bool = False
        ):
        self._sim = YoliBoardSim(size, game)
        self.window_size = 512  # The size of the PyGame window

        self.observation_space = spaces.Box(low = 0,  high = 1, shape = (size * (self._sim.no_tiles+1),), dtype=np.uint8)
        self.action_space = spaces.Discrete(size * (self._sim.no_tiles+1))
        self.rewarder = rewarder
        self.shuffle = shuffle
        
        # How to handle illegal moves
        self.illegal_penalty = illegal_penalty
        self.illegal_termination = illegal_termination
        
        assert render_mode is None or render_mode in self.metadata["render_modes"]
        self.render_mode = render_mode

        self.window = None
        self.clock = None
        
        # aliases
        self.tiles = self._sim.no_tiles
        self.size = self._sim.size
        
    def _get_obs(self):
        oh = np.zeros((self.size, self.tiles + 1), dtype=np.uint8)
        oh[range(self.size), self._sim.positions] = 1
        return oh.flatten()

    def _get_info(self):
        return {
            "notification": self._sim.notification, #global notification, 0=nothing, 1=success, 2=failure
            "indications": tuple(self._sim.indications) #0=nothing, 1=indicated, 2=rejected
        }

    def reset(self, seed=None, options=None):
        #super().reset(seed=seed)
        
        self._sim.reset()
        self._steps = 0
        
        if self.shuffle:
            self._sim.shuffle_tiles()

        observation = self._get_obs()
        #info = self._get_info()

        if self.render_mode == "human":
            self._render_frame()
        return observation

    def _unpack_pos(self, action):
        return action % (self.size)

    def _unpack_action(self, action):
        # Find coordinate
        pos = self._unpack_pos(action)
        tile = math.floor(action / self.size)        
        return pos, tile
    
    def step(self, action):
        reward = 0
        terminated = False
        self._steps += 1

        try:
            pos, tile = self._unpack_action(action)
            self._sim.step(pos, tile)
            terminated = self._sim.terminated
            action_type = Rewarder.action_remove if tile == 0 else Rewarder.action_add
            reward = self.rewarder.reward(action_type, pos, np.array(self._sim.indications), terminated, self._steps)
        except:
            terminated = self.illegal_termination
            reward = self.illegal_penalty.reward(Rewarder.action_illegal, self._unpack_pos(action), self._sim.indications, terminated, self._steps)

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
        if self.window is None and self.render_mode == "rgb_array":
            pygame.init()
            pygame.display.init()
            self.window = pygame.display.set_mode((self.window_size, self.window_size))

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
        indication_colors = [(0,0,0), (0,255,0), (255,0,0)]
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
                indication_colors[self._sim.indications[x]],
                rect,
                2
            )
            tile = self._sim.get_tile_at(x)
            if tile is not None:
                img = tile.image
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
            tileIndex = x + 1
            tile = self._sim.get_tile(tileIndex)
            if tile is not None:
                img = tile.image
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