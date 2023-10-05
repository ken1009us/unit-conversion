import pytest

from units_core.units import Units


def test_conversion():
    units = Units()
    converted_value = units.convert(1, 'meter', 'centimeter')
    assert converted_value == 100

