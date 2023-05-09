import unittest
from unittest.mock import Mock
from yoli_sim.pcg import RuleGenerator
from yoli_sim.pcg.population import Population
from yoli_sim.eval import RuleEvaluator

class TestPopulationControl(unittest.TestCase):
    def test_generate_callsGenerateRuleOnRuleGenerator(self):
        # Given
        generatorMock = Mock(RuleGenerator)
        sut = Population(1, generatorMock)

        # When
        sut.generate([])

        # Then
        generatorMock.generate_rule.assert_called_once()

    def test_generate_populationTwo_callsGenerateRuleOnRuleGeneratorTwoTimes(self):
        # Given
        generatorMock = Mock(RuleGenerator)
        sut = Population(2, generatorMock)
        expected = 2

        # When
        sut.generate([])

        # Then
        count = generatorMock.generate_rule.call_count
        self.assertEqual(count, expected)

    def test_evaluate_callsEvaluateOnRuleEvaluator(self):
        # Given
        evalMock = Mock(RuleEvaluator)
        sut = Population(1, Mock(RuleGenerator))
        sut.generate([])

        # When
        sut.evaluate(evalMock)

        # Then
        evalMock.evaluate.assert_called_once()