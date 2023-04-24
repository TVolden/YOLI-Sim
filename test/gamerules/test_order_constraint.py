from yoli_sim.gamerules import OrderConstraint
import unittest

class TestOrderConstraint(unittest.TestCase):
    def test_evaluate_noTilesIn_nothingOut(self):
        # Given
        sut = OrderConstraint("test")
        expected = tuple([])

        # When
        result = sut.evaluate([])

        # Then
        self.assertEqual(result, expected)

    def test_evaluate_orderMatch_tileAccepted(self):
        # Given
        key = "order"
        sut = OrderConstraint(key)
        expected = tuple([1])
        tile = [{key:0}]

        # When
        result = sut.evaluate(tile)

        # Then
        self.assertEqual(result, expected)

    def test_evaluate_orderMismatch_tileRejected(self):
        # Given
        key = "order"
        sut = OrderConstraint(key)
        expected = tuple([-1])
        tile = [{key:1}]

        # When
        result = sut.evaluate(tile)

        # Then
        self.assertEqual(result, expected)

    def test_evaluate_missingKey_tileRejected(self):
        # Given
        key = "order"
        sut = OrderConstraint(key)
        expected = tuple([-1])
        tile = [{}]

        # When
        result = sut.evaluate(tile)

        # Then
        self.assertEqual(result, expected)

    def test_evaluate_threeTilesOneCorrect_correctTileAccepted(self):
        # Given
        key = "order"
        sut = OrderConstraint(key)
        expected = 1
        tile = [{key:0},{key:0},{}]

        # When
        result = sut.evaluate(tile)

        # Then
        self.assertEqual(result[0], expected)

    def test_evaluate_threeTilesOneCorrect_mismatchTileRejected(self):
        # Given
        key = "order"
        sut = OrderConstraint(key)
        expected = -1
        tile = [{key:0},{key:0},{}]

        # When
        result = sut.evaluate(tile)

        # Then
        self.assertEqual(result[1], expected)

    def test_evaluate_threeTilesOneCorrect_missingKeyTileRejected(self):
        # Given
        key = "order"
        sut = OrderConstraint(key)
        expected = -1
        tile = [{key:0},{key:0},{}]

        # When
        result = sut.evaluate(tile)

        # Then
        self.assertEqual(result[2], expected)

    def test_toString_returnsStr(self):
        # Given
        key = "required"
        sut = OrderConstraint(key)
        expected = f"The value of {key} has to match the position on the board"

        # When
        result = str(sut)

        # Then
        self.assertEqual(result, expected)