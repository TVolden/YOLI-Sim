import unittest
from  gym_yoli.spaces.onehotencoding import OneHotEncoding

class TestOneHotEncoding(unittest.TestCase):
    def test_sample_size3x3_returns3x3matrix(self):
        # Given
        sut = OneHotEncoding(3, 3)

        # When
        result = sut.sample()

        # Then
        print(result)
        self.assertEqual(result.shape, (3,3))

    def test_contains_legal_returnsTrue(self):
        # Given
        sut = OneHotEncoding(3, 3)
        legalInput = [[1,0,0],[0,0,0],[0,0,0]]

        # When
        result = sut.contains(legalInput)

        # Then
        self.assertTrue(result)

    def test_contains_illegal_returnsTrue(self):
        # Given
        sut = OneHotEncoding(3, 3)
        illegalInput = [[1,0,0],[1,0,0],[0,0,0]]

        # When
        result = sut.contains(illegalInput)

        # Then
        self.assertFalse(result)