from yoli_sim.gamerules import CompositeGameRule, GameRule
import unittest
from unittest.mock import Mock

class TestCompositeGameRule(unittest.TestCase):
    def test_toString_noRule_returnsEmpty(self):
        # Given
        sut = CompositeGameRule([])
        expected = ""

        # When
        result = f"{sut}"

        # Then
        self.assertEqual(result, expected)

    def test_toString_callsToStringOnRule(self):
        # Given
        rule = Mock(GameRule)
        rule.__str__ = Mock(return_value = "")
        sut = CompositeGameRule([rule])

        # When
        str(sut)

        # Then
        rule.__str__.assert_called_once()
        

    def test_toString_oneRule_returnsRuleToString(self):
        # Given
        expected = "test"
        rule = Mock(GameRule)
        rule.__str__ = Mock(return_value = expected)
        sut = CompositeGameRule([rule])

        # When
        result = f"{sut}"

        # Then
        self.assertEqual(result, expected)

    def test_toString_twoRule_returnsRule1AndRule2ToString(self):
        # Given
        first = "test1"
        second = "test2"
        expected = "test1 and test2"
        rule1 = Mock(GameRule)
        rule1.__str__ = Mock(return_value = first)
        rule2 = Mock(GameRule)
        rule2.__str__ = Mock(return_value = second)
        sut = CompositeGameRule([rule1, rule2])

        # When
        result = f"{sut}"

        # Then
        self.assertEqual(result, expected)