from yoli_sim.gamerules import MatchConstraint
import unittest

class TestMatchConstraint(unittest.TestCase):
    def test_evaluate_noTilesIn_nothingOut(self):
        # Given
        sut = MatchConstraint("test")
        expected = tuple([])

        # When
        result = sut.evaluate([])

        # Then
        self.assertEqual(result, expected)

    def test_evaluate_twoMatchingTiles_bothAccepted(self):
        # Given
        key = "match key"
        value = "matching value"
        sut = MatchConstraint(key)
        expected = tuple([1, 1])
        tiles = tuple([{key:value}, {key:value}])

        # When
        result = sut.evaluate(tiles)

        # Then
        self.assertEqual(result, expected)

    def test_evaluate_twoMismatchingTiles_firstAccepted(self):
        # Given
        key = "match key"
        value = "matching value"
        sut = MatchConstraint(key)
        expected = 1
        tiles = tuple([{key:value}, {key:"wrong"}])

        # When
        result = sut.evaluate(tiles)

        # Then
        self.assertEqual(result[0], expected)

    def test_evaluate_twoMismatchingTiles_secondRejected(self):
        # Given
        key = "match key"
        value = "matching value"
        sut = MatchConstraint(key)
        expected = -1
        tiles = tuple([{key:value}, {key:"wrong"}])

        # When
        result = sut.evaluate(tiles)

        # Then
        self.assertEqual(result[1], expected)