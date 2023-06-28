import unittest
from unittest.mock import Mock
from yoli_sim.pcg import GeneticRuleGenerator, RuleGenerator

class TestGeneticRuleGenerator(unittest.TestCase):
    def test_generateRule_calls(self):
        # Given
        generatorMock = Mock(RuleGenerator)
        sut = GeneticRuleGenerator(generatorMock, population_size=1, max_generations=1)

        # When
        sut.generate_rule([])

        # Then
        generatorMock.generate_rule.assert_called_once()