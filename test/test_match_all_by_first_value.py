import unittest
from yoli_sim import MatchAllByFirstValue

class TestMatchAllByFirstValue(unittest.TestCase):
    def test_match_noInput_noOutput(self):
        # Given
        tiles = []
        sut = MatchAllByFirstValue("key")

        # When
        result = sut.match(tiles)

        # Then
        self.assertTupleEqual(result, ())

    def test_match_oneInput_oneAccepted(self):
        # Given
        accepted = 1
        tiles = [{"key":0}]
        sut = MatchAllByFirstValue("key", accepted_value=accepted)
        expected = tuple([accepted])

        # When
        result = sut.match(tiles)

        # Then
        self.assertTupleEqual(result, expected)

    def test_match_twoDifferentValues_rejectsSecondTile(self):
        # Given
        tiles = [{"key":1}, {"key":2}]
        sut = MatchAllByFirstValue("key")

        # When
        _, second = sut.match(tiles)

        # Then
        self.assertEqual(second, -1)        