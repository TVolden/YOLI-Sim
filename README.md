# YOLI-Sim
A virtual simulator for the YOLI board and games. Made as part of a PhD Project.

# Getting started

Install package

```pycon
cd YOLI-Sim
pip install -e .
```

Run play.py

```pycon
python play.py
```

## Using GYM (OpenAI)

The library uses the deprecated version of *gym* to support libraries such as stable-baselines3.

Create environment:

```python
import gym

env = gym.make('gym_yoli/YoliSim-v0')
```

It is possible to provide an instance of a YoliTileGame with the *game* parameter.
```python
env = gym.make('gym_yoli/YoliSim-v0', game=CustomGame())
```