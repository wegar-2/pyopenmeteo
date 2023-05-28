import pytest

from pyopenmeteo.parameters.gps_position import GpsPosition


def test_correct_input():
    position = GpsPosition(latitude=23.22, longitude=-88.12)
    assert isinstance(position, GpsPosition)


def test_incorrect_input_case1():
    with pytest.raises(Exception):
        GpsPosition(latitude=223.22, longitude=-88.12)


def test_incorrect_input_case2():
    with pytest.raises(Exception):
        GpsPosition(latitude=23.22, longitude=-188.12)
