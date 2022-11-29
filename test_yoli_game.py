import unittest
import numpy.testing
from unittest.mock import Mock
from gym_yoli.envs.yoli_game import YoliGameEnv
from gym_yoli.envs.tile_master import TileMaster

class TestYoliGameEnv(unittest.TestCase):
    def test_instantiate_callsTileCountOnTileMaster(self):
        # Given
        tileMasterMock = Mock(TileMaster)
        tileMasterMock.tile_count = Mock(return_value=1)

        # When
        sut = YoliGameEnv(tile_master=tileMasterMock)

        # Than
        tileMasterMock.tile_count.assert_called_once()
    
    def test_reset_sizeOneOneTile_returnsOneByTwoObservation(self):
        # Given
        expected = [[1, 0]]
        tileMasterMock = Mock(TileMaster)
        tileMasterMock.tile_count = Mock(return_value=1)
        sut = YoliGameEnv(size=1, tile_master=tileMasterMock)

        # When
        observation, _ = sut.reset()

        # Then
        numpy.testing.assert_array_equal(observation, expected)
    
    def test_reset_sizeTwoOneTile_returnsTwoByTwoObservation(self):
        # Given
        expected = [[1, 0], [1, 0]]
        tileMasterMock = Mock(TileMaster)
        tileMasterMock.tile_count = Mock(return_value=1)
        sut = YoliGameEnv(size=2, tile_master=tileMasterMock)

        # When
        observation, _ = sut.reset()

        # Then
        numpy.testing.assert_array_equal(observation, expected)

    def test_reset_sizeTwoTwoTiles_returnsTwoByThreeObservation(self):
        # Given
        expected = [[1, 0, 0], [1, 0, 0]]
        tileMasterMock = Mock(TileMaster)
        tileMasterMock.tile_count = Mock(return_value=2)
        sut = YoliGameEnv(size=2, tile_master=tileMasterMock)

        # When
        observation, _ = sut.reset()

        # Then
        numpy.testing.assert_array_equal(observation, expected)

    def test_reset_returnsInformationDict_notificationIsZero(self):
        # Given
        expected = 0
        tileMasterMock = Mock(TileMaster)
        tileMasterMock.tile_count = Mock(return_value=0)
        sut = YoliGameEnv(tile_master=tileMasterMock)

        # When
        _, information = sut.reset()

        # Then
        self.assertEqual(information.get('notification'), expected)
    
    def test_reset_returnsInformationDict_indicationsIsZeroArray(self):
        # Given
        expected = tuple([0] * 5)
        tileMasterMock = Mock(TileMaster)
        tileMasterMock.tile_count = Mock(return_value=0)
        sut = YoliGameEnv(tile_master=tileMasterMock)

        # When
        _, information = sut.reset()

        # Then
        self.assertEqual(information.get('indications'), expected)
    
    def test_step_evaluateIsCalled(self):
        # Given
        tileMasterMock = Mock(TileMaster)
        tileMasterMock.tile_count = Mock(return_value=1)
        tileMasterMock.evaluate = Mock(return_value=(tuple([0]*5), 0))
        sut = YoliGameEnv(size=3, tile_master=tileMasterMock)
        sut.reset()
        action = [[0,0], [0,1], [0,0]]

        # When
        sut.step(action)

        # Then
        tileMasterMock.evaluate.assert_called_once()
