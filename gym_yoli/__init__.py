from gym.envs.registration import register
from .rewarders import *
from .matchers import *

register(
    id="gym_yoli/YoliSim-v0",
    entry_point="gym_yoli.envs:YoliSimEnv",
    max_episode_steps=30_000_000
)
