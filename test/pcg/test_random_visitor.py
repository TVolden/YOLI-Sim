import unittest
from unittest.mock import Mock
from yoli_sim.pcg import RandomVisitor, RandomPicker

class TestRandomVisitor(unittest.TestCase):
    def test_propertyKey_oneKey_returnsKey(self):
        # Given
        key = "key"
        sut = RandomVisitor([{key:"some value"}])
        expected = key

        # When
        result = sut.property_key()

        # Then
        self.assertEqual(result, expected)
    
    def test_propertyKey_callsPickOneOnRandomPicker(self):
        # Given
        randomMock = Mock(RandomPicker)
        sut = RandomVisitor([{"some key":"some value"}], random=randomMock)

        # When
        sut.property_key()

        # Then
        randomMock.pick_one.assert_called_once()

    def test_propertyKey_pickOneReturnsKey_returnsKey(self):
        # Given
        key = "key"
        randomStub = Mock(RandomPicker)
        randomStub.pick_one.return_value = key
        sut = RandomVisitor([{"some key":"some value"}], random=randomStub)
        expected = key

        # When
        result = sut.property_key()

        # Then
        self.assertEqual(result, expected)

    def test_propertyValue_oneValue_returnsValue(self):
        # Given
        key = "key"
        value = "some value"
        sut = RandomVisitor([{key:value}])
        expected = value

        # When
        result = sut.property_value(key)

        # Then
        self.assertEqual(result, expected)

    def test_decimal_callsPickOneOnRandomPicker(self):
        # Given
        randomMock = Mock(RandomPicker)
        sut = RandomVisitor([], random=randomMock)

        # When
        sut.decimal(1,4)

        # Then
        randomMock.pick_one.assert_called_once()

    def test_decimal_callsPickOneOnRandomPicker_withList(self):
        # Given
        randomMock = Mock(RandomPicker)
        sut = RandomVisitor([], random=randomMock)
        expected = [1,2,3,4]

        # When
        sut.decimal(1,4)

        # Then
        randomMock.pick_one.assert_called_once_with(expected)

    def test_pick_callsPickOneOnRandomPickerWithList(self):
        # Given
        randomMock = Mock(RandomPicker)
        sut = RandomVisitor([], random=randomMock)
        expected = [1,2,3,4]

        # When
        sut.pick([1,2,3,4])

        # Then
        randomMock.pick_one.assert_called_once_with(expected)

    def test_pick_pickOneReturnsItem_returnsItem(self):
        # Given
        choice = 42
        randomMock = Mock(RandomPicker)
        randomMock.pick_one.return_value = choice
        sut = RandomVisitor([], random=randomMock)
        expected = choice

        # When
        result = sut.pick([])

        # Then
        self.assertEqual(result, expected)