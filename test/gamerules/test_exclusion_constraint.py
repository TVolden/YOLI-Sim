from yoli_sim.gamerules import ExclusionConstraint
import unittest

class TestExclusionConstraint(unittest.TestCase):
    def test_evaluate_noTilesIn_nothingOut(self):
        # Given
        sut = ExclusionConstraint("test", "test")
        expected = tuple([])

        # When
        result = sut.evaluate([])

        # Then
        self.assertEqual(result, expected)

    def test_evaluate_matchKeyValue_tileRejected(self):
        # Given
        key = "exclude"
        value = "true"
        sut = ExclusionConstraint(key, value)
        expected = tuple([-1])
        tiles = [{key:value}]

        # When
        result = sut.evaluate(tiles)

        # Then
        self.assertEqual(result, expected)

    def test_evaluate_missingKey_tileIgnored(self):
        # Given
        key = "exclude"
        value = "true"
        sut = ExclusionConstraint(key, value)
        expected = tuple([0])
        tiles = [{}]

        # When
        result = sut.evaluate(tiles)

        # Then
        self.assertEqual(result, expected)

    def test_evaluate_mismatchValue_tileIgnored(self):
        # Given
        key = "exclude"
        value = "true"
        sut = ExclusionConstraint(key, value)
        expected = tuple([0])
        tiles = [{key:"false"}]

        # When
        result = sut.evaluate(tiles)

        # Then
        self.assertEqual(result, expected)

    def test_evaluate_twoTilesOneMatchOneMismatch_matchRejcted(self):
        # Given
        key = "exclude"
        value = "true"
        sut = ExclusionConstraint(key, value)
        expected = -1
        tiles = [{key:value}, {key:"false"}]

        # When
        result = sut.evaluate(tiles)

        # Then
        self.assertEqual(result[0], expected)

    def test_evaluate_twoTilesOneMatchOneMismatch_mismatchIgnored(self):
        # Given
        key = "exclude"
        value = "true"
        sut = ExclusionConstraint(key, value)
        expected = 0
        tiles = [{key:value}, {key:"false"}]

        # When
        result = sut.evaluate(tiles)

        # Then
        self.assertEqual(result[1], expected)

    def test_evaluate_threeTilesOneMissingKey_missingKeyIgnored(self):
        # Given
        key = "exclude"
        value = "true"
        sut = ExclusionConstraint(key, value)
        expected = 0
        tiles = [{key:value}, {key:"false"}, {}]

        # When
        result = sut.evaluate(tiles)

        # Then
        self.assertEqual(result[2], expected)