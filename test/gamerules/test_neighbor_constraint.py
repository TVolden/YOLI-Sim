from yoli_sim.gamerules import NeighborConstraint
import unittest

class TestNeighborConstraint(unittest.TestCase):
    def test_evaluate_noTilesIn_noTilesOut(self):
        # Given
        sut = NeighborConstraint("some key", "some value",\
                                 "some key", "some value")
        expected = tuple([])

        # When
        result = sut.evaluate([])

        # Then
        self.assertEqual(result, expected)
    
    def test_evaluate_noTriggeredTile_ignoreAll(self):
        # Given
        triggered_key = "triggerable"
        triggered_value = "true"
        trigger_key = "trigger"
        trigger_value = "true"

        sut = NeighborConstraint(triggered_key, triggered_value, \
                                 trigger_key, trigger_value)
        tiles = tuple([
            {triggered_key: "false", trigger_key:trigger_value},
            {triggered_key: "false", trigger_key:trigger_value},
        ])
        expected = tuple([0, 0])

        # When
        result = sut.evaluate(tiles)

        # Then
        self.assertEqual(result, expected)
        
    def test_evaluate_neighborConflict_triggeredTileRejected(self):
        # Given
        triggered_key = "triggerable"
        triggered_value = "true"
        trigger_key = "trigger"
        trigger_value = "true"

        sut = NeighborConstraint(triggered_key, triggered_value, \
                                 trigger_key, trigger_value)
        tiles = tuple([
            {triggered_key: triggered_value},
            {triggered_key: "false", trigger_key:trigger_value},
        ])
        expected = tuple([-1, 0])

        # When
        result = sut.evaluate(tiles)

        # Then
        self.assertEqual(result, expected)

    def test_evaluate_noConflict_triggeredTileAccepted(self):
        # Given
        triggered_key = "triggerable"
        triggered_value = "true"
        trigger_key = "trigger"
        trigger_value = "true"

        sut = NeighborConstraint(triggered_key, triggered_value, \
                                 trigger_key, trigger_value)
        tiles = tuple([
            {triggered_key: triggered_value},
            {triggered_key: "false", trigger_key: "false"},
        ])
        expected = tuple([1, 0])

        # When
        result = sut.evaluate(tiles)

        # Then
        self.assertEqual(result, expected)
        
    def test_evaluate_multipleConflict_triggeredTileRejected(self):
        # Given
        triggered_key = "triggerable"
        triggered_value = "true"
        trigger_key = "trigger"
        trigger_value = "true"

        sut = NeighborConstraint(triggered_key, triggered_value, \
                                 trigger_key, trigger_value)
        tiles = tuple([
            {triggered_key: "false", trigger_key: trigger_value},
            {triggered_key: triggered_value},
            {triggered_key: "false", trigger_key: trigger_value},
        ])
        expected = tuple([0, -1, 0])

        # When
        result = sut.evaluate(tiles)

        # Then
        self.assertEqual(result, expected)

    def test_toString_returnsStr(self):
        # Given
        triggered_key = "triggerable"
        triggered_value = "true"
        trigger_key = "trigger"
        trigger_value = "true"
        sut = NeighborConstraint(triggered_key, triggered_value, \
                                 trigger_key, trigger_value)
        expected = f"Those with {triggered_key} set to {triggered_value} cannot be adjacent to those with {trigger_key} set to {trigger_value}"

        # When
        result = str(sut)

        # Then
        self.assertEqual(result, expected)