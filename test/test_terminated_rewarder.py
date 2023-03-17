import unittest
import numpy as np
from unittest.mock import Mock
from yoli_sim.rewarders import Rewarder, TerminatedRewarder, TerminatedRewardDecorator

class TestTerminatedRewarder(unittest.TestCase):
    def test_reward_terminatedFalse_returnsZero(self):
        # Given
        terminated = False
        steps = -1
        action = Rewarder.action_add
        position = 0
        indications = np.array([0,0,0,0,0])
        sut = TerminatedRewarder()
        expected = 0

        # When
        result = sut.reward(action, position, indications, terminated, steps)

        # Then
        self.assertEqual(result, expected)

    def test_reward_terminatedTrue_returnsOne(self):
        # Given
        terminated = True
        steps = -1
        action = Rewarder.action_add
        position = 0
        indications = np.array([0,0,0,0,0])
        sut = TerminatedRewarder()
        expected = 1

        # When
        result = sut.reward(action, position, indications, terminated, steps)

        # Then
        self.assertEqual(result, expected)

class TestTerminatedRewardDecorator(unittest.TestCase):
    def test_reward_terminatedFalse_callsRewardOnDecoratee(self):
        # Given
        decorateeMock = Mock(Rewarder)
        decorateeMock.reward = Mock()
        steps = -1
        action = "Any action"
        position = 0
        indications = np.array([0,0,0,0,0])

        terminated = False
        sut = TerminatedRewardDecorator(decorateeMock)

        # When
        sut.reward(action, position, indications, terminated, steps)

        # Then
        decorateeMock.reward.assert_called_once()

    def test_reward_terminatedTrue_doesNotCallRewardOnDecoratee(self):
        # Given
        decorateeMock = Mock(Rewarder)
        decorateeMock.reward = Mock()
        steps = -1
        action = "Any action"
        position = 0
        indications = np.array([0,0,0,0,0])

        terminated = True
        sut = TerminatedRewardDecorator(decorateeMock)

        # When
        sut.reward(action, position, indications, terminated, steps)

        # Then
        decorateeMock.reward.assert_not_called()

    def test_reward_terminatedTrue_returnsTrue(self):
        # Given
        decorateeMock = Mock(Rewarder)
        decorateeMock.reward = Mock()
        steps = -1
        action = "Any action"
        position = 0
        indications = np.array([0,0,0,0,0])

        terminated = True
        sut = TerminatedRewardDecorator(decorateeMock)
        expected = 1

        # When
        result = sut.reward(action, position, indications, terminated, steps)

        # Then
        self.assertEqual(result, expected)