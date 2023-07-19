import pytest

from pyopenmeteo.parameters.gps_position import GpsPosition


def test_correct_input():
    position = GpsPosition(latitude=23.22, longitude=-88.12, name="test_position")
    assert isinstance(position, GpsPosition)


def test_incorrect_input_case1():
    with pytest.raises(Exception):
        GpsPosition(latitude=223.22, longitude=-88.12, name="test_position")


def test_incorrect_input_case2():
    with pytest.raises(Exception):
        GpsPosition(latitude=23.22, longitude=-188.12, name="test_position")


def test_incorrect_input_case3():
    with pytest.raises(Exception):
        GpsPosition(latitude=23.22, longitude=-188.12, name=b"1234")
