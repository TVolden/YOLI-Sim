import unittest
import numpy as np
from gym_yoli.envs.rewarders import FixedRewarder

class TestFixedRewarder(unittest.TestCase):
    def test_reward_initializedWithOne_returnsOne(self):
        # Given
        terminated = False
        steps = -1
        action = "Any action"
        position = 0
        indications = np.array([])
        sut = FixedRewarder(1)
        expected = 1

        # When
        result = sut.reward(action, position, indications, terminated, steps)

        # Then
        self.assertEqual(result, expected)

    def test_reward_initializedWithTwo_returnsTwo(self):
        # Given
        terminated = False
        steps = -1
        action = "Any action"
        position = -1
        indications = np.array([])
        sut = FixedRewarder(2)
        expected = 2

        # When
        result = sut.reward(action, position, indications, terminated, steps)

        # Then
        self.assertEqual(result, expected)

    def test_reward_initializedWithThree_returnsThree(self):
        # Given
        terminated = True
        steps = -1
        action = "Any action"
        position = -1
        indications = np.array([])
        sut = FixedRewarder(3)
        expected = 3

        # When
        result = sut.reward(action, position, indications, terminated, steps)

        # Then
        self.assertEqual(result, expected)
