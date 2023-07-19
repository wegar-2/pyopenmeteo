from datetime import date
import pytest
from pyopenmeteo.parameters.dates_interval import DatesInterval


def test_correct_arguments():
    di = DatesInterval(start=date(2000, 1, 1), end=date(2002, 3, 11))
    assert isinstance(di, DatesInterval) is True


def test_incorrect_arguments():
    with pytest.raises(Exception) as ve:
        DatesInterval(start=date(2011, 1, 1), end=date(2002, 3, 11))

