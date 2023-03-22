import unittest
from unittest.mock import Mock
from yoli_sim import YoliTileGame, YoliBoardSim, YoliTile

class TestYoliBoardSim(unittest.TestCase):
    def test_instantiate_callsNoTilesOnYoliTileGame(self):
        # Given
        gameMock = Mock(YoliTileGame)
        gameMock.count_tiles = Mock(return_value=1)
        
        # When
        YoliBoardSim(1, gameMock)

        # Then
        gameMock.count_tiles.assert_called_once()
    
    def test_setGame_callsNoTilesOnYoliTileGame(self):
        # Given
        gameMock = Mock(YoliTileGame)
        gameMock.count_tiles = Mock(return_value=1)
        sut = YoliBoardSim(1, Mock(YoliTileGame))        

        # When
        sut.set_game(gameMock)

        # Then
        gameMock.count_tiles.assert_called_once()

    # Skipping default setter - getter tests.

    def test_step_callsEvaluateOnYoliTileGame(self):
        # Given
        size = 1
        gameMock = Mock(YoliTileGame)
        gameMock.count_tiles = Mock(return_value=1)
        gameMock.evaluate = Mock(return_value=([0]*size, False))
        sut = YoliBoardSim(size, gameMock)

        # When
        sut.step(0, 1)

        # Then
        gameMock.evaluate.assert_called_once()

    def test_step_duplicateAction_throwsException(self):
        # Given
        size = 1
        gameMock = Mock(YoliTileGame)
        gameMock.count_tiles = Mock(return_value=1)
        gameMock.evaluate = Mock(return_value=([0]*size, False))
        sut = YoliBoardSim(size, gameMock)
        sut.step(0, 1)

        # When, Then
        self.assertRaises(Exception, sut.step, 0, 1)
    
    def test_step_incorrectTileIndex_throwsException(self):
        # Given
        size = 1
        gameMock = Mock(YoliTileGame)
        gameMock.count_tiles = Mock(return_value=1)
        sut = YoliBoardSim(size, gameMock)

        # When, Then
        self.assertRaises(Exception, sut.step, 0, 2)

    def test_step_removingTileFromEmptyPosition_throwsException(self):
        # Given
        size = 1
        gameMock = Mock(YoliTileGame)
        gameMock.count_tiles = Mock(return_value=1)
        sut = YoliBoardSim(size, gameMock)

        # When, Then
        self.assertRaises(Exception, sut.step, 0, 0)

    def test_positions_noActions_returnsEmptyBoard(self):
        # Given
        gameMock = Mock(YoliTileGame)
        size = 5
        expect = [0] * size
        sut = YoliBoardSim(size, gameMock)

        # When
        result = sut.positions

        # Then
        self.assertListEqual(result, expect)

    def test_positions_acceptedAction_returnsNewBoard(self):
        # Given
        size = 5
        tile = 1
        pos = 0

        gameMock = Mock(YoliTileGame)
        gameMock.count_tiles = Mock(return_value=1)
        gameMock.evaluate = Mock(return_value=([1, 0, 0, 0, 0], False))
        expect = [tile, 0, 0, 0, 0]
        sut = YoliBoardSim(size, gameMock)
        sut.step(pos, tile)

        # When
        result = sut.positions

        # Then
        self.assertListEqual(result, expect)

    def test_indications_noActions_returnsNoIndications(self):
        # Given
        gameMock = Mock(YoliTileGame)
        size = 5
        expect = tuple([0] * size)
        sut = YoliBoardSim(size, gameMock)

        # When
        result = sut.indications

        # Then
        self.assertTupleEqual(result, expect)

    def test_indications_action_returnsEvaluationOutput(self):
        # Given
        size = 5
        gameMock = Mock(YoliTileGame)
        gameMock.count_tiles = Mock(return_value=1)
        evaluation = [1, -1, 0, -1, 1]
        gameMock.evaluate = Mock(return_value=(evaluation, False))
        sut = YoliBoardSim(size, gameMock)
        sut.step(0, 1)
        expect = tuple(evaluation)

        # When
        result = sut.indications

        # Then
        self.assertTupleEqual(result, expect)

    def test_notification_noActions_returnsZero(self):
        # Given
        gameMock = Mock(YoliTileGame)
        gameMock.count_tiles = Mock(return_value=1)
        sut = YoliBoardSim(1, gameMock)
        expect = 0

        # When
        result = sut.notification

        # Then
        self.assertEqual(result, expect)

    def test_notification_evaluationReturnsTrue_returnsOne(self):
        # Given
        gameMock = Mock(YoliTileGame)
        gameMock.count_tiles = Mock(return_value=1)
        gameMock.evaluate = Mock(return_value=([0], True))
        sut = YoliBoardSim(1, gameMock)
        sut.step(0, 1)
        expect = 1

        # When
        result = sut.notification

        # Then
        self.assertEqual(result, expect)

    def test_availableTiles_noActions_returnsTiles(self):
        # Given
        tiles = 1
        gameMock = Mock(YoliTileGame)
        gameMock.count_tiles = Mock(return_value=tiles)
        sut = YoliBoardSim(1, gameMock)
        expect = tuple(range(1, tiles + 1))

        # When
        result = sut.available_tiles

        # Then
        self.assertTupleEqual(result, expect)

    def test_availableTiles_afterAction_returnsOneLessTile(self):
        # Given
        tiles = 1
        gameMock = Mock(YoliTileGame)
        gameMock.count_tiles = Mock(return_value=tiles)
        gameMock.evaluate = Mock(return_value=([0], True))
        sut = YoliBoardSim(1, gameMock)
        sut.step(0, 1)
        expect = tuple(range(1, tiles - 1))

        # When
        result = sut.available_tiles

        # Then
        self.assertTupleEqual(result, expect)
    
    def test_positionOccupied_noActions_returnsFalse(self):
        # Given
        pos = 0
        gameMock = Mock(YoliTileGame)
        gameMock.count_tiles = Mock(return_value=1)
        sut = YoliBoardSim(1, gameMock)

        # When
        result = sut.position_occupied(pos)

        # Then
        self.assertFalse(result)
    
    def test_positionOccupied_afterTilePlacedOnPosition_returnsTrue(self):
        # Given
        pos = 0
        gameMock = Mock(YoliTileGame)
        gameMock.count_tiles = Mock(return_value=1)
        gameMock.evaluate = Mock(return_value=([0], True))
        sut = YoliBoardSim(1, gameMock)
        sut.step(0, 1)

        # When
        result = sut.position_occupied(pos)

        # Then
        self.assertTrue(result)
    
    def test_isTileAvailable_noActions_returnsTrue(self):
        # Given
        tile = 1
        gameMock = Mock(YoliTileGame)
        gameMock.count_tiles = Mock(return_value=1)
        sut = YoliBoardSim(1, gameMock)

        # When
        result = sut.is_tile_available(tile)

        # Then
        self.assertTrue(result)
    
    def test_isTileAvailable_afterTilePlaced_returnsFalse(self):
        # Given
        tile = 1
        gameMock = Mock(YoliTileGame)
        gameMock.count_tiles = Mock(return_value=1)
        gameMock.evaluate = Mock(return_value=([0], True))
        sut = YoliBoardSim(1, gameMock)
        sut.step(0, 1)

        # When
        result = sut.is_tile_available(tile)

        # Then
        self.assertFalse(result)
    
    def test_getTileAt_noTileAtPosition_returnsNone(self):
        # Given
        pos = 0
        gameMock = Mock(YoliTileGame)
        gameMock.count_tiles = Mock(return_value=1)
        sut = YoliBoardSim(1, gameMock)

        # When
        result = sut.get_tile_at(pos)

        # Then
        self.assertIsNone(result)
    
    def test_getTileAt_tileAtPosition_callsTileAtOnYoliTileGameWithTileIndex(self):
        # Given
        pos = 0
        tile = 1
        gameMock = Mock(YoliTileGame)
        gameMock.count_tiles = Mock(return_value=1)
        gameMock.evaluate = Mock(return_value=([0], True))
        gameMock.tile_at = Mock(return_value=None)
        sut = YoliBoardSim(1, gameMock)
        sut.step(pos, tile)
        expectedTileIndex = tile - 1 # Subtract the No-Tile (0) indicated

        # When
        sut.get_tile_at(pos)

        # Then
        gameMock.tile_at.assert_called_once_with(expectedTileIndex)
    
    def test_getTileAt_tileAtPosition_returnsTileFromYoliTileGame(self):
        # Given
        pos = 0
        tile = 1
        gameStub = Mock(YoliTileGame)
        gameStub.count_tiles = Mock(return_value=1)
        gameStub.evaluate = Mock(return_value=([0], True))
        expected = Mock(YoliTile)
        gameStub.tile_at = Mock(return_value=expected)
        sut = YoliBoardSim(1, gameStub)
        sut.step(pos, tile)

        # When
        result = sut.get_tile_at(pos)

        # Then
        self.assertEqual(result, expected)

    