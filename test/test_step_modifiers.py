import unittest
from unittest.mock import Mock
import numpy as np
from yoli_sim.rewarders import Rewarder, StepMultiplierDecorator, DivideByStepDecorator

class TestStepMultiplierDecorator(unittest.TestCase):
    def test_reward_callsRewardOnDecoratee(self):
        # Given
        decorateeMock = Mock(Rewarder)
        decorateeMock.reward = Mock(return_value=0)
        terminated = False
        steps = 0
        action = "Any action"
        position = 0
        indications = np.array([0,0,0,0,0])
        sut = StepMultiplierDecorator(decorateeMock)

        # When
        sut.reward(action, position, indications, terminated, steps)

        # Then
        decorateeMock.reward.assert_called_once()

    def test_reward_decorateeReturnsOne_returnsStep(self):
        # Given
        decorateeStub = Mock(Rewarder)
        decorateeStub.reward = Mock(return_value=1)
        terminated = False
        steps = 42
        action = "Any action"
        position = 0
        indications = np.array([0,0,0,0,0])
        sut = StepMultiplierDecorator(decorateeStub)
        expected = steps

        # When
        result = sut.reward(action, position, indications, terminated, steps)

        # Then
        self.assertEqual(result, expected)

    def test_reward_decorateeReturnsTwo_returnsStepTimesTwo(self):
        # Given
        decorateeStub = Mock(Rewarder)
        decorateeStub.reward = Mock(return_value=2)
        terminated = False
        steps = 42
        action = "Any action"
        position = 0
        indications = np.array([0,0,0,0,0])
        sut = StepMultiplierDecorator(decorateeStub)
        expected = steps*2

        # When
        result = sut.reward(action, position, indications, terminated, steps)

        # Then
        self.assertEqual(result, expected)

class TestStepDivideByStepDecorator(unittest.TestCase):
    def test_reward_callsRewardOnDecoratee(self):
        # Given
        decorateeMock = Mock(Rewarder)
        decorateeMock.reward = Mock(return_value=0)
        terminated = False
        steps = 1
        action = "Any action"
        position = 0
        indications = np.array([0,0,0,0,0])
        sut = DivideByStepDecorator(decorateeMock)

        # When
        sut.reward(action, position, indications, terminated, steps)

        # Then
        decorateeMock.reward.assert_called_once()

    def test_reward_decorateeReturnsSameNumberAsSteps_returnsOne(self):
        # Given
        steps = 42
        decorateeStub = Mock(Rewarder)
        decorateeStub.reward = Mock(return_value=steps)
        terminated = False
        action = "Any action"
        position = 0
        indications = np.array([0,0,0,0,0])
        sut = DivideByStepDecorator(decorateeStub)
        expected = 1

        # When
        result = sut.reward(action, position, indications, terminated, steps)

        # Then
        self.assertEqual(result, expected)

    def test_reward_decorateeReturnsOne_returnsOneDividedBySteps(self):
        # Given
        decorateeStub = Mock(Rewarder)
        decorateeStub.reward = Mock(return_value=1)
        terminated = False
        steps = 42
        action = "Any action"
        position = 0
        indications = np.array([0,0,0,0,0])
        sut = DivideByStepDecorator(decorateeStub)
        expected = 1/steps

        # When
        result = sut.reward(action, position, indications, terminated, steps)

        # Then
        self.assertEqual(result, expected)