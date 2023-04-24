import unittest
from yoli_sim.match_two import MatchTwo

class TestMatchTwo(unittest.TestCase):
    def test_evaluate_inputLength_matchesOutputLength(self):
        # Given
        sut = MatchTwo()
        emptyBoard = [None] * 5
        excepted = tuple([0] * 5)

        # When
        indications, _ = sut.evaluate(emptyBoard)

        # Then
        self.assertCountEqual(indications, excepted)

    def test_evaluate_noTiles_noIndications(self):
        # Given
        sut = MatchTwo()
        emptyBoard = [None]*5
        expected = tuple([0]*5)

        # When
        indications, _ = sut.evaluate(emptyBoard)

        # Then
        self.assertEqual(indications, expected)

    def test_evaluate_oneTile_oneAccept(self):
        # Given
        sut = MatchTwo()
        board = [1] + [None]*4
        expected = tuple([1]+[0]*4)

        # When
        indications, _ = sut.evaluate(board)

        # Then
        self.assertEqual(indications, expected)

    def test_evaluate_oneTile_nonTerminalState(self):
        # Given
        sut = MatchTwo()
        board = [1] + [None] * 5
        expected = False

        # When
        _, terminal = sut.evaluate(board)

        # Then
        self.assertEqual(terminal, expected)

    def test_evaluate_groupMismatch_rejectSecond(self):
        # Given
        sut = MatchTwo()
        board = [1, 3] + [None] * 3
        expected = (1,-1,0,0,0)

        # When
        indications, _ = sut.evaluate(board)

        # Then
        self.assertEqual(indications, expected)

    def test_evaluate_groupMismatch_nonTerminalState(self):
        # Given
        sut = MatchTwo()
        board = [1, 3] + [None] * 4
        expected = False

        # When
        _, terminal = sut.evaluate(board)

        # Then
        self.assertEqual(terminal, expected)

    def test_evaluate_matchingGroups_terminalState(self):
        # Given
        sut = MatchTwo()
        board = [0, 1] + [None] * 4
        expected = True

        # When
        _, terminal = sut.evaluate(board)

        # Then
        self.assertEqual(terminal, expected)

    def test_evaluate_multipleGroupMatch_rejectOneAcceptTheOther(self):
        # Given
        sut = MatchTwo()
        board = [0, 2, 1] + [None] * 2
        expected = (1,-1,1,0,0)

        # When
        indications, _ = sut.evaluate(board)

        # Then
        self.assertEqual(indications, expected)
