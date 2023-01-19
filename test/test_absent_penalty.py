import unittest
import numpy as np
from gym_yoli.envs.rewarders import AbsentPenalty

class TestAbsentPenalty(unittest.TestCase):
    def test_reward_noneAccepted_returnsMinusTheLength(self):
        # Given
        action = "Any actions"
        position = -1
        terminated = False
        steps = -1

        indications = np.array([0,0,0,0,0])
        sut = AbsentPenalty()
        expected = -len(indications)

        # When
        result = sut.reward(action, position, indications, terminated, steps)

        # Then
        self.assertEqual(result, expected)

    def test_reward_oneOutOfFiveAccepted_returnsMinusFour(self):
        # Given
        action = "Any actions"
        position = -1
        terminated = False
        steps = -1

        indications = np.array([1,0,0,0,0])
        sut = AbsentPenalty()
        expected = -4

        # When
        result = sut.reward(action, position, indications, terminated, steps)

        # Then
        self.assertEqual(result, expected)

    def test_reward_allAccepted_returnsZero(self):
        # Given
        action = "Any actions"
        position = -1
        terminated = False
        steps = -1

        indications = np.array([1,1,1,1,1])
        sut = AbsentPenalty()
        expected = 0

        # When
        result = sut.reward(action, position, indications, terminated, steps)

        # Then
        self.assertEqual(result, expected)
