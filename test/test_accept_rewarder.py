import unittest
import numpy as np
from yoli_sim.rewarders import AcceptedRewarder, Rewarder

class TestAcceptedRewarder(unittest.TestCase):
    def test_reward_addedTileAccepted_returnsOne(self):
        # Given
        terminated = False
        steps = -1

        action = Rewarder.action_add
        position = 0
        indications = np.array([1,0,0,0,0])
        sut = AcceptedRewarder()
        expected = 1

        # When
        result = sut.reward(action, position, indications, terminated, steps)

        # Then
        self.assertEqual(result, expected)

    def test_reward_removeTile_returnsZero(self):
        # Given
        terminated = False
        steps = -1

        action = Rewarder.action_remove
        position = 1
        indications = np.array([1,0,0,0,0])
        sut = AcceptedRewarder()
        expected = 0

        # When
        result = sut.reward(action, position, indications, terminated, steps)

        # Then
        self.assertEqual(result, expected)

    def test_reward_illegalAction_returnsZero(self):
        # Given
        terminated = False
        steps = -1

        action = Rewarder.action_illegal
        position = 1
        indications = np.array([1,0,0,0,0])
        sut = AcceptedRewarder()
        expected = 0

        # When
        result = sut.reward(action, position, indications, terminated, steps)

        # Then
        self.assertEqual(result, expected)

    def test_reward_addedTileRejected_returnsZero(self):
        # Given
        terminated = False
        steps = -1

        action = Rewarder.action_illegal
        position = 1
        indications = np.array([2,0,0,0,0])
        sut = AcceptedRewarder()
        expected = 0

        # When
        result = sut.reward(action, position, indications, terminated, steps)

        # Then
        self.assertEqual(result, expected)

    def test_reward_addedTileSkipped_returnsZero(self):
        # Given
        terminated = False
        steps = -1

        action = Rewarder.action_illegal
        position = 1
        indications = np.array([0,0,0,0,0])
        sut = AcceptedRewarder()
        expected = 0

        # When
        result = sut.reward(action, position, indications, terminated, steps)

        # Then
        self.assertEqual(result, expected)