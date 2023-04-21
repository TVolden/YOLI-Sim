import unittest
from unittest.mock import Mock
from yoli_sim.gamerules import GameRule
from yoli_sim.pcg import *

class TestRandomRuleGenerator(unittest.TestCase):
    def test_generateRule_noRules_raisesException(self):
        # Given
        sut = RandomRuleGenerator([])

        # When
        with self.assertRaises(NoRulesException) as cm:
            sut.generate_rule([])

    def test_generateRule_oneRuleFactory_callsConstructOnFactory(self):
        # Given
        ruleMock = Mock(GameRuleFactory)
        sut = RandomRuleGenerator([ruleMock])

        # When
        sut.generate_rule([])

        # Then
        ruleMock.construct.assert_called_once()

    def test_generateRule_oneRule_returnGeneratedRule(self):
        # Given
        ruleStub = Mock(GameRule)
        factoryStub = Mock(GameRuleFactory)
        factoryStub.construct.return_value = ruleStub
        sut = RandomRuleGenerator([factoryStub])

        # When
        result = sut.generate_rule([])

        # Then
        self.assertEqual(result, ruleStub)

    def test_generateRule_twoRules_callsPickOneOnRandomPicker(self):
        # Given
        factoryStub = Mock(GameRuleFactory)
        randomMock = Mock(RandomPicker)
        sut = RandomRuleGenerator([factoryStub, factoryStub], random_picker=randomMock)

        # When
        sut.generate_rule([])

        # Then
        randomMock.pick_one.assert_called_once()

    def test_generateRule_oneRule_callsConstructOnVisitorFactory(self):
        # Given
        factoryStub = Mock(GameRuleFactory)
        visitorFactoryMock = Mock(RandomVisitorFactory)

        sut = RandomRuleGenerator([factoryStub],visitor_factory=visitorFactoryMock)

        # When
        sut.generate_rule([])

        # Then
        visitorFactoryMock.construct.assert_called_once()

    def test_generateRule_twoRules_pickOneReturnsFirst_callsConstructOnFirst(self):
        # Given
        factoryMock = Mock(GameRuleFactory)
        randomStub = Mock(RandomPicker)
        randomStub.pick_one.return_value = factoryMock
        sut = RandomRuleGenerator([factoryMock, None], random_picker=randomStub)

        # When
        sut.generate_rule([])

        # Then
        factoryMock.construct.assert_called_once()

    def test_generateRule_oneRule_callsConstructWithVisitor(self):
        # Given
        factoryMock = Mock(GameRuleFactory)
        visitorStub = Mock(RandomVisitor)
        visitorFactoryStub = Mock(RandomVisitorFactory)
        visitorFactoryStub.construct.return_value = visitorStub

        sut = RandomRuleGenerator([factoryMock],visitor_factory=visitorFactoryStub)

        # When
        sut.generate_rule([])

        # Then
        factoryMock.construct.assert_called_once_with(visitorStub)