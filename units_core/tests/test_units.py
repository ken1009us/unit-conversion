"""
This module contains test cases for the Units class in the units_core.units module.

The test cases cover common scenarios for unit conversion,
including successful conversions and expected errors
when dealing with undefined or invalid units.

"""

import pytest
import pint.errors

from units_core.units import Units


def test_conversion():
    """
    Test the conversion of a value from one defined unit to another using the Units class.

    This test case creates an instance of the Units class
    and uses it to convert a value from meters to centimeters.
    It asserts that the converted value is as expected.
    """

    units = Units()
    converted_value = units.convert(1, 'meter', 'centimeter')
    assert converted_value == 100


def test_invalid_unit():
    """
    Test the error handling when attempting
    to convert an undefined or invalid unit using the Units class.

    This test case ensures that an UndefinedUnitError is raised
    when attempting to convert a value with an undefined
    or invalid unit. It uses pytest's raises context manager to check for the expected error.
    """

    units = Units()
    with pytest.raises(pint.errors.UndefinedUnitError):
        units.convert(1000, 'invalid_unit', 'kilometer')
