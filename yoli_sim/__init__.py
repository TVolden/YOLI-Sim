from gymnasium.envs.registration import register
from .events import *
from .rewarders import *
from .matchers import *
#from .utils import *
from .yoli_tile_game import *
from .gamerules import *
from .match_two import *
from .yoli_board_sim import *

register(
    id="yoli/YoliSim-v0",
    entry_point="yoli_sim.envs:YoliSimEnv",
    max_episode_steps=100
)
