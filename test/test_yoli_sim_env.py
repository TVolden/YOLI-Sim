import unittest
import numpy.testing
from unittest.mock import Mock
from yoli_sim.envs import YoliSimEnv
from yoli_sim import YoliTileGame

class TestYoliSimEnv(unittest.TestCase):
    def test_instantiate_callsTileCountOnTileMaster(self):
        # Given
        gameMock = Mock(YoliTileGame)
        gameMock.count_tiles = Mock(return_value=1)

        # When
        sut = YoliSimEnv(game=gameMock)

        # Then
        gameMock.count_tiles.assert_called_once()
    
    def test_reset_sizeOneOneTile_returnsTwoElementObservation(self):
        # Given
        expected = [1, 0]
        gameMock = Mock(YoliTileGame)
        gameMock.count_tiles = Mock(return_value=1)
        sut = YoliSimEnv(size=1, game=gameMock)

        # When
        observation = sut.reset()

        # Then
        numpy.testing.assert_array_equal(observation, expected)
    
    def test_reset_sizeTwoOneTile_returnsFourElementsObservation(self):
        # Given
        expected = [1, 0, 1, 0]
        gameMock = Mock(YoliTileGame)
        gameMock.count_tiles = Mock(return_value=1)
        sut = YoliSimEnv(size=2, game=gameMock)

        # When
        observation = sut.reset()

        # Then
        numpy.testing.assert_array_equal(observation, expected)

    def test_reset_sizeTwoTwoTiles_returnsSixElementsObservation(self):
        # Given
        expected = [1, 0, 0, 1, 0, 0]
        gameMock = Mock(YoliTileGame)
        gameMock.count_tiles = Mock(return_value=2)
        sut = YoliSimEnv(size=2, game=gameMock)

        # When
        observation = sut.reset()

        # Then
        numpy.testing.assert_array_equal(observation, expected)

    def test_step_noAction_returnNegativeReward(self):
        # Given
        gameMock = Mock(YoliTileGame)
        gameMock.count_tiles = Mock(return_value=1)
        gameMock.evaluate = Mock(return_value=(tuple([0]*3), 0))
        sut = YoliSimEnv(size=3, game=gameMock)
        sut.reset()
        no_action = 0
        expected = -1

        # When
        _, reward, _, _ = sut.step(no_action)

        # Then
        self.assertEqual(reward, expected)

    def test_step_action_evaluateIsCalled(self):
        # Given
        gameMock = Mock(YoliTileGame)
        gameMock.count_tiles = Mock(return_value=1)
        gameMock.evaluate = Mock(return_value=(tuple([0]*3), 0))
        sut = YoliSimEnv(size=3, game=gameMock)
        sut.reset()
        action = 4 # Place tile 1 on place 1

        # When
        sut.step(action)

        # Then
        gameMock.evaluate.assert_called_once()

    def test_step_action_returnNewObservation(self):
        # Given
        gameMock = Mock(YoliTileGame)
        gameMock.count_tiles = Mock(return_value=1)
        gameMock.evaluate = Mock(return_value=(tuple([0]*3), 0))
        sut = YoliSimEnv(size=3, game=gameMock)
        sut.reset()
        action = 4 # Place tile 1 on place 1
        excepted = [1,0, 0,1, 1,0]

        # When
        observation, _, _, _ = sut.step(action)

        # Then
        numpy.testing.assert_array_equal(observation, excepted)

    def test_step_evaluationRejectsAction_returnOldObservation(self):
        # Given
        gameMock = Mock(YoliTileGame)
        gameMock.count_tiles = Mock(return_value=1)
        gameMock.evaluate = Mock(return_value=(tuple([0,-1,0]), 0))
        sut = YoliSimEnv(size=3, game=gameMock)
        sut.reset()
        action = 4 # Place tile 1 on place 1
        excepted = [1,0, 1,0, 1,0]

        # When
        observation, _, _, _ = sut.step(action)

        # Then
        numpy.testing.assert_array_equal(observation, excepted)

    def test_step_evaluationReturnsTerminated_returnsTerminated(self):
        # Given
        gameMock = Mock(YoliTileGame)
        gameMock.count_tiles = Mock(return_value=1)
        gameMock.evaluate = Mock(return_value=(tuple([0,0,0]), 1))
        sut = YoliSimEnv(size=3, game=gameMock)
        sut.reset()
        action = 4 # Place tile 1 on place 1

        # When
        _, _, terminated, _ = sut.step(action)

        # Then
        self.assertTrue(terminated)

    def test_step_evaluationReturnsTerminated_returnsReward(self):
        # Given
        gameMock = Mock(YoliTileGame)
        gameMock.count_tiles = Mock(return_value=1)
        gameMock.evaluate = Mock(return_value=(tuple([0,0,0]), 1))
        sut = YoliSimEnv(size=3, game=gameMock)
        sut.reset()
        action = 4 # Place tile 1 on place 1
        expected = 1

        # When
        _, reward, _, _ = sut.step(action)

        # Then
        self.assertEqual(reward, expected)

    def test_step_repeatedAction_returnsNegativeReward(self):
        # Given
        gameMock = Mock(YoliTileGame)
        gameMock.count_tiles = Mock(return_value=1)
        gameMock.evaluate = Mock(return_value=(tuple([0,0,0]), 1))
        sut = YoliSimEnv(size=3, game=gameMock)
        sut.reset()
        action = 4 # Place tile 1 on place 1
        expected = -1
        sut.step(action)

        # When
        _, reward, _, _ = sut.step(action)

        # Then
        self.assertEqual(reward, expected)