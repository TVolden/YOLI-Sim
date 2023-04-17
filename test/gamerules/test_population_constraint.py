from yoli_sim.gamerules import PopulationConstraint
import unittest

class TestPopulationConstraint(unittest.TestCase):
    def test_evaluate_tileWithoutPropertyKey_returnsIgnore(self):
        # Given
        sut = PopulationConstraint(1, "test", "test")
        expected = tuple([0])

        # When
        result = sut.evaluate([{}])

        # Then
        self.assertEqual(result, expected)

    def test_evaluate_limitZero_rejectsAllMatches(self):
        # Given
        limit = 0
        key = "test"
        value = "test"
        tiles = [{key:value},{key:value},{key:value}]
        sut = PopulationConstraint(limit, key, value)
        expected = tuple([-1, -1, -1])

        # When
        result = sut.evaluate(tiles)

        # Then
        self.assertEqual(result, expected)

    def test_evaluate_limitZero_ignoresAllNonMatches(self):
        # Given
        limit = 0
        key = "test"
        value = "test"
        other_value = "not test"
        tiles = [{key:other_value},{key:other_value},{key:other_value}]
        sut = PopulationConstraint(limit, key, value)
        expected = tuple([0, 0, 0])

        # When
        result = sut.evaluate(tiles)

        # Then
        self.assertEqual(result, expected)

    def test_evaluate_limitOne_acceptsFirstMatch(self):
        # Given
        limit = 1
        key = "test"
        value = "test"
        tiles = [{key:value},{key:value}]
        sut = PopulationConstraint(limit, key, value)
        expected = 1

        # When
        result = sut.evaluate(tiles)

        # Then
        self.assertEqual(result[0], expected)

    def test_evaluate_limitOne_rejectsSecondMatch(self):
        # Given
        limit = 1
        key = "test"
        value = "test"
        tiles = [{key:value},{key:value}]
        sut = PopulationConstraint(limit, key, value)
        expected = tuple([1, -1])

        # When
        result = sut.evaluate(tiles)

        # Then
        self.assertEqual(result, expected)