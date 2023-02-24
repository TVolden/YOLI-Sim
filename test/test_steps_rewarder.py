import unittest
import numpy as np
from gym_yoli.envs.rewarders import StepsRewarder, Rewarder

class TestStepsRewarder(unittest.TestCase):
    def test_reward_default_returnsNegativeSteps(self):
        # Given
        terminated = False
        steps = 42
        action = Rewarder.action_add
        position = 0
        indications = np.array([0,0,0,0,0])
        sut = StepsRewarder()
        expected = -steps

        # When
        result = sut.reward(action, position, indications, terminated, steps)

        # Then
        self.assertEqual(result, expected)

    def test_reward_negativeFalse_returnsSteps(self):
        # Given
        terminated = False
        steps = 42
        action = Rewarder.action_add
        position = 0
        indications = np.array([0,0,0,0,0])
        sut = StepsRewarder(negative=False)
        expected = steps

        # When
        result = sut.reward(action, position, indications, terminated, steps)

        # Then
        self.assertEqual(result, expected)