import gymnasium as gym
from gymnasium import spaces
import pygame
import numpy as np

class YoliGameEnv(gym.Env):
    metadata = {"render_modes": ["human", "rgb_array"], "render_fps": 4}

    def __init__(self, render_mode=None, size=5, tiles=30):
        self.size = size
        self.window_size = 512  # The size of the PyGame window

        self.observation_space = spaces.Dict(
            {
                "positions": spaces.Tuple((spaces.Discrete(size), spaces.Discrete(tiles+1)))
            }
        )

        self.action_space = spaces.Dict(
            {
                "position": spaces.Discrete(size),
                "tile": spaces.Discrete(tiles+1)
            }
        )

        self._action_tiles = {
            0: None,
            1: {"name": "Monkey", "group": 1, "order": 1},
            2: {"name": "Banana", "group": 1, "order": 2},
            3: {"name": "Lion", "group": 2, "order": 1},
            4: {"name": "Zebra", "group": 2, "order": 2}
        }

        assert render_mode is None or render_mode in self.metadata["render_modes"]
        self.render_mode = render_mode

        self.window = None
        self.clock = None

    def _get_obs(self):
        return {"positions": tuple(self._positions)}

    def _get_info(self):
        return {
            "notification": self._notification, #global notification, 0=nothing, 1=success, 2=failure
            "indications": tuple(self._indications) #0=nothing, 1=indicated, 2=rejected
        }

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)

        self._positions = [0] * self.size
        self._indications = [0] * self.size

        observation = self._get_obs()
        info = self._get_info()

        if self.render_mode == "human":
            self._render_frame()

        return observation, info

    def step(self, action):
        truncated = False
        if action.position < 0 or action.position > self.size:
            truncated = True
        
        self._notification = 0
        self._indications = [0 in range(self.size)]

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
        pix_square_size = (
            self.window_size / self.size
        )  # The size of a single grid square in pixels

        # First we draw the target
        pygame.draw.rect(
            canvas,
            (255, 0, 0),
            pygame.Rect(
                pix_square_size * self._target_location,
                (pix_square_size, pix_square_size),
            ),
        )
        # Now we draw the agent
        pygame.draw.circle(
            canvas,
            (0, 0, 255),
            (self._agent_location + 0.5) * pix_square_size,
            pix_square_size / 3,
        )

        # Finally, add some gridlines
        for x in range(self.size + 1):
            pygame.draw.line(
                canvas,
                0,
                (0, pix_square_size * x),
                (self.window_size, pix_square_size * x),
                width=3,
            )
            pygame.draw.line(
                canvas,
                0,
                (pix_square_size * x, 0),
                (pix_square_size * x, self.window_size),
                width=3,
            )

        if self.render_mode == "human":
            # The following line copies our drawings from `canvas` to the visible window
            self.window.blit(canvas, canvas.get_rect())
            pygame.event.pump()
            pygame.display.update()

            # We need to ensure that human-rendering occurs at the predefined framerate.
            # The following line will automatically add a delay to keep the framerate stable.
            self.clock.tick(self.metadata["render_fps"])
        else:  # rgb_array
            return np.transpose(
                np.array(pygame.surfarray.pixels3d(canvas)), axes=(1, 0, 2)
            )

    def close(self):
        if self.window is not None:
            pygame.display.quit()
            pygame.quit()
