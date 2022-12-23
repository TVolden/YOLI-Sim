import unittest
import numpy.testing
from unittest.mock import Mock
from gym_yoli.envs.yoli_game import YoliGameEnv
from gym_yoli.envs.tile_master import TileMaster

class TestYoliGameEnv(unittest.TestCase):
    def test_instantiate_callsTileCountOnTileMaster(self):
        # Given
        tileMasterMock = Mock(TileMaster)
        tileMasterMock.count_tiles = Mock(return_value=1)

        # When
        sut = YoliGameEnv(tile_master=tileMasterMock)

        # Than
        tileMasterMock.count_tiles.assert_called_once()
    
    def test_reset_sizeOneOneTile_returnsTwoElementObservation(self):
        # Given
        expected = [1, 0]
        tileMasterMock = Mock(TileMaster)
        tileMasterMock.count_tiles = Mock(return_value=1)
        sut = YoliGameEnv(size=1, tile_master=tileMasterMock)

        # When
        observation = sut.reset()

        # Then
        numpy.testing.assert_array_equal(observation, expected)
    
    def test_reset_sizeTwoOneTile_returnsFourElementsObservation(self):
        # Given
        expected = [1, 0, 1, 0]
        tileMasterMock = Mock(TileMaster)
        tileMasterMock.count_tiles = Mock(return_value=1)
        sut = YoliGameEnv(size=2, tile_master=tileMasterMock)

        # When
        observation = sut.reset()

        # Then
        numpy.testing.assert_array_equal(observation, expected)

    def test_reset_sizeTwoTwoTiles_returnsSixElementsObservation(self):
        # Given
        expected = [1, 0, 0, 1, 0, 0]
        tileMasterMock = Mock(TileMaster)
        tileMasterMock.count_tiles = Mock(return_value=2)
        sut = YoliGameEnv(size=2, tile_master=tileMasterMock)

        # When
        observation = sut.reset()

        # Then
        numpy.testing.assert_array_equal(observation, expected)

    def test_step_noAction_returnNegativeReward(self):
        # Given
        tileMasterMock = Mock(TileMaster)
        tileMasterMock.count_tiles = Mock(return_value=1)
        tileMasterMock.evaluate = Mock(return_value=(tuple([0]*3), 0))
        sut = YoliGameEnv(size=3, tile_master=tileMasterMock)
        sut.reset()
        no_action = 0
        expected = -1

        # When
        _, reward, _, _ = sut.step(no_action)

        # Then
        self.assertEqual(reward, expected)

    def test_step_action_evaluateIsCalled(self):
        # Given
        tileMasterMock = Mock(TileMaster)
        tileMasterMock.count_tiles = Mock(return_value=1)
        tileMasterMock.evaluate = Mock(return_value=(tuple([0]*3), 0))
        sut = YoliGameEnv(size=3, tile_master=tileMasterMock)
        sut.reset()
        action = 4 # Place tile 1 on place 1

        # When
        sut.step(action)

        # Then
        tileMasterMock.evaluate.assert_called_once()

    def test_step_action_returnNewObservation(self):
        # Given
        tileMasterMock = Mock(TileMaster)
        tileMasterMock.count_tiles = Mock(return_value=1)
        tileMasterMock.evaluate = Mock(return_value=(tuple([0]*3), 0))
        sut = YoliGameEnv(size=3, tile_master=tileMasterMock)
        sut.reset()
        action = 4 # Place tile 1 on place 1
        excepted = [1,0, 0,1, 1,0]

        # When
        observation, _, _, _ = sut.step(action)

        # Then
        numpy.testing.assert_array_equal(observation, excepted)

    def test_step_evaluationRejectsAction_returnOldObservation(self):
        # Given
        tileMasterMock = Mock(TileMaster)
        tileMasterMock.count_tiles = Mock(return_value=1)
        tileMasterMock.evaluate = Mock(return_value=(tuple([0,2,0]), 0))
        sut = YoliGameEnv(size=3, tile_master=tileMasterMock)
        sut.reset()
        action = 4 # Place tile 1 on place 1
        excepted = [1,0, 1,0, 1,0]

        # When
        observation, _, _, _ = sut.step(action)

        # Then
        numpy.testing.assert_array_equal(observation, excepted)

    def test_step_evaluationReturnsTerminated_returnsTerminated(self):
        # Given
        tileMasterMock = Mock(TileMaster)
        tileMasterMock.count_tiles = Mock(return_value=1)
        tileMasterMock.evaluate = Mock(return_value=(tuple([0,0,0]), 1))
        sut = YoliGameEnv(size=3, tile_master=tileMasterMock)
        sut.reset()
        action = 4 # Place tile 1 on place 1

        # When
        _, _, terminated, _ = sut.step(action)

        # Then
        self.assertTrue(terminated)

    def test_step_evaluationReturnsTerminated_returnsReward(self):
        # Given
        tileMasterMock = Mock(TileMaster)
        tileMasterMock.count_tiles = Mock(return_value=1)
        tileMasterMock.evaluate = Mock(return_value=(tuple([0,0,0]), 1))
        sut = YoliGameEnv(size=3, tile_master=tileMasterMock)
        sut.reset()
        action = 4 # Place tile 1 on place 1
        expected = 1

        # When
        _, reward, _, _ = sut.step(action)

        # Then
        self.assertEqual(reward, expected)

    def test_step_repeatedAction_returnsNegativeReward(self):
        # Given
        tileMasterMock = Mock(TileMaster)
        tileMasterMock.count_tiles = Mock(return_value=1)
        tileMasterMock.evaluate = Mock(return_value=(tuple([0,0,0]), 1))
        sut = YoliGameEnv(size=3, tile_master=tileMasterMock)
        sut.reset()
        action = 4 # Place tile 1 on place 1
        expected = -1
        sut.step(action)

        # When
        _, reward, _, _ = sut.step(action)

        # Then
        self.assertEqual(reward, expected)