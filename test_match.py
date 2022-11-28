import unittest
from gym_yoli.envs.match import MatchTwo

class TestMatchTwo(unittest.TestCase):
    def test_evaluate_noTiles_noIndications(self):
        # Given
        sut = MatchTwo()
        expected = tuple([0]*5)

        # When
        indications, _ = sut.evaluate([0]*5)

        # Then
        self.assertEqual(indications, expected)

    def test_evaluate_sizeOne_oneOutput_noMatterTheInput(self):
        # Given
        size = 1
        sit = MatchTwo(size)
        expected = size

        # When
        indication, _ = sit.evaluate([0]*100)

        # Then
        count = len(indication)
        self.assertEqual(count, expected)

    def test_evaluate_oneTile_oneAccept(self):
        # Given
        sut = MatchTwo()
        board = [1] + [0]*4
        expected = tuple(board)

        # When
        indications, _ = sut.evaluate(board)

        # Then
        self.assertEqual(indications, expected)

    def test_evaluate_oneTile_nonTerminalState(self):
        # Given
        sut = MatchTwo()
        board = [1] + [0] * 5
        expected = False

        # When
        _, terminal = sut.evaluate(board)

        # Then
        self.assertEqual(terminal, expected)

    def test_evaluate_groupMismatch_rejectSecond(self):
        # Given
        sut = MatchTwo()
        board = [1, 3] + [0] * 3
        expected = (1,2,0,0,0)

        # When
        indications, _ = sut.evaluate(board)

        # Then
        self.assertEqual(indications, expected)

    def test_evaluate_groupMismatch_nonTerminalState(self):
        # Given
        sut = MatchTwo()
        board = [1, 3] + [0] * 4
        expected = False

        # When
        _, terminal = sut.evaluate(board)

        # Then
        self.assertEqual(terminal, expected)

    def test_evaluate_sizeTwoTwoTilesSplitByEmptySpace_checksFirstTwoOnly(self):
        # Given
        size = 2
        sit = MatchTwo(size)
        board = [1, 0, 3]
        expected = (1, 0)

        # When
        indication, _ = sit.evaluate(board)

        # Then
        self.assertEqual(indication, expected)

    def test_evaluate_matchingGroups_terminalState(self):
        # Given
        sut = MatchTwo()
        board = [1, 2] + [0] * 4
        expected = True

        # When
        _, terminal = sut.evaluate(board)

        # Then
        self.assertEqual(terminal, expected)

    def test_evaluate_multipleGroupMatch_rejectOneAcceptTheOther(self):
        # Given
        sut = MatchTwo()
        board = [1, 3, 2] + [0] * 3
        expected = (1,2,1,0,0)

        # When
        indications, _ = sut.evaluate(board)

        # Then
        self.assertEqual(indications, expected)
