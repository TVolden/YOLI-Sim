from yoli_sim.gamerules import ExclusiveConstraint
import unittest

class TestExclusiveConstraint(unittest.TestCase):
    def test_evaluate_noTiles_noEvaluation(self):
        # Given
        sut = ExclusiveConstraint("test", "test")
        expected = tuple([])

        # When
        result = sut.evaluate([])

        # Then
        self.assertEqual(result, expected)
    
    def test_evaluate_missingKey_tileRejected(self):
        # Given
        sut = ExclusiveConstraint("required", "")
        expected = tuple([-1])
        tiles = [{}]

        # When
        result = sut.evaluate(tiles)

        # Then
        self.assertEqual(result, expected)

    def test_evaluate_wrongValue_tileRejected(self):
        # Given
        key = "required"
        sut = ExclusiveConstraint(key, "some value")
        expected = tuple([-1])
        tiles = [{key:"wrong value"}]

        # When
        result = sut.evaluate(tiles)

        # Then
        self.assertEqual(result, expected)

    def test_evaluate_correctValue_tileAccepted(self):
        # Given
        key = "required"
        value = "true"
        sut = ExclusiveConstraint(key, value)
        expected = tuple([1])
        tiles = [{key:value}]

        # When
        result = sut.evaluate(tiles)

        # Then
        self.assertEqual(result, expected)

    def test_evaluate_twoTilesOneCorrect_correctTileAccepted(self):
        # Given
        key = "required"
        value = "true"
        sut = ExclusiveConstraint(key, value)
        expected = tuple([1, -1])
        tiles = [{key:value}, {key:"false"}]

        # When
        result = sut.evaluate(tiles)

        # Then
        self.assertEqual(result, expected)