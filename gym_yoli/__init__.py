from gymnasium.envs.registration import register

register(
    id="gym_yoli/YoliGame-v0",
    entry_point="gym_yoli.envs:YoliGameEnv",
)
