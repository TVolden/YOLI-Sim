import unittest
from unittest.mock import Mock
from yoli_sim.pcg import RuleGenerator
from yoli_sim.pcg.population import Population
from yoli_sim.eval import RuleEvaluator

class TestPopulationControl(unittest.TestCase):
    def test_generate_callsGenerateRuleOnRuleGenerator(self):
        # Given
        generatorMock = Mock(RuleGenerator)
        sut = Population(generatorMock)

        # When
        sut.generate(1)

        # Then
        generatorMock.generate_rule.assert_called_once()

    def test_generate_populationTwo_callsGenerateRuleOnRuleGeneratorTwoTimes(self):
        # Given
        generatorMock = Mock(RuleGenerator)
        sut = Population(generatorMock)
        expected = 2

        # When
        sut.generate(2)

        # Then
        count = generatorMock.generate_rule.call_count
        self.assertEqual(count, expected)

    def test_evaluate_callsEvaluateOnRuleEvaluator(self):
        # Given
        evalMock = Mock(RuleEvaluator)
        sut = Population(Mock(RuleGenerator))
        sut.generate(1)

        # When
        sut.evaluate_population(evalMock)

        # Then
        evalMock.evaluate.assert_called_once()