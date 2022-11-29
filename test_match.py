import unittest
from gym_yoli.envs.match import MatchTwo

class TestMatchTwo(unittest.TestCase):
    def test_evaluate_inputLength_matchesOutputLength(self):
        # Given
        sut = MatchTwo()
        input = [0] * 5
        excepted = tuple(input)

        # When
        indications, _ = sut.evaluate(input)

        # Then
        self.assertCountEqual(indications, excepted)

    def test_evaluate_noTiles_noIndications(self):
        # Given
        sut = MatchTwo()
        expected = tuple([0]*5)

        # When
        indications, _ = sut.evaluate([0]*5)

        # Then
        self.assertEqual(indications, expected)

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
        board = [1, 3, 2] + [0] * 2
        expected = (1,2,1,0,0)

        # When
        indications, _ = sut.evaluate(board)

        # Then
        self.assertEqual(indications, expected)
