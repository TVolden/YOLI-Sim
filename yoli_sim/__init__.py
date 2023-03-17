from gym.envs.registration import register
from .rewarders import *
from .matchers import *
from .utils import *

register(
    id="gym_yoli/YoliSim-v0",
    entry_point="yoli_sim.envs:YoliSimEnv",
    max_episode_steps=100
)
