import unittest
from unittest.mock import Mock
import numpy as np
from gym_yoli.envs.rewarders import Rewarder, RejectPenaltyDecorator

class TestRejectPenaltyDecorator(unittest.TestCase):
    def test_reward_noRejects_callsRewardOnDecoratee(self):
        # Given
        decorateeMock = Mock(Rewarder)
        decorateeMock.reward = Mock()
        terminated = False
        steps = -1
        action = "Any action"
        position = 0
        indications = np.array([0,0,0,0,0])
        sut = RejectPenaltyDecorator(decorateeMock)

        # When
        sut.reward(action, position, indications, terminated, steps)

        # Then
        decorateeMock.reward.assert_called_once()

    def test_reward_oneReject_doesNotCallRewardOnDecoratee(self):
        # Given
        decorateeMock = Mock(Rewarder)
        decorateeMock.reward = Mock()
        terminated = False
        steps = -1
        action = "Any action"
        position = 0
        indications = np.array([2,0,0,0,0])
        sut = RejectPenaltyDecorator(decorateeMock)

        # When
        sut.reward(action, position, indications, terminated, steps)

        # Then
        decorateeMock.reward.assert_not_called()

    def test_reward_oneReject_returnsZero(self):
        # Given
        decorateeStub = Mock(Rewarder)
        terminated = False
        steps = -1
        action = "Any action"
        position = 0
        indications = np.array([2,0,0,0,0])
        sut = RejectPenaltyDecorator(decorateeStub)
        expected = 0

        # When
        result = sut.reward(action, position, indications, terminated, steps)

        # Then
        self.assertEqual(result, expected)

    def test_reward_oneReject_returnsInitiatedValue(self):
        # Given
        decorateeStub = Mock(Rewarder)
        terminated = False
        steps = -1
        action = "Any action"
        position = 0
        indications = np.array([2,0,0,0,0])
        sut = RejectPenaltyDecorator(decorateeStub, -1)
        expected = -1

        # When
        result = sut.reward(action, position, indications, terminated, steps)

        # Then
        self.assertEqual(result, expected)