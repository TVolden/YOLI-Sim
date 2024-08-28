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

## Using Gymnasium (Farama Foundation)

Create environment:

```python
import gymnasium as gym

env = gym.make('yoli/YoliSim-v0')
```

It is possible to provide an instance of a YoliTileGame with the *game* parameter.

```python
env = gym.make('yoli/YoliSim-v0', game=CustomGame())
```