import pytest
import pint.errors

from pathlib import Path
from units_core.units import Units


def test_conversion():
    units = Units()
    converted_value = units.convert(1, 'meter', 'centimeter')
    assert converted_value == 100


def test_invalid_unit():
    units = Units()
    with pytest.raises(pint.errors.UndefinedUnitError):
        units.convert(1000, 'invalid_unit', 'kilometer')