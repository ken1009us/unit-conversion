import sys
import os
import pytest

current_directory = os.path.dirname(os.path.realpath(__file__))
myproject_directory = os.path.join(current_directory, '..', '..')
sys.path.append(myproject_directory)

from units_proto.units_pb2 import UnitConversionRequest
from units_proto_extensions.extensions import convert_units


def test_convert_units_success():
    request = UnitConversionRequest()
    request.from_unit = "meter"
    request.to_unit = "kilometer"
    request.value = 1000

    response = convert_units(request)

    assert response.converted_value == 1
    assert response.error == ""

def test_convert_units_failure():
    request = UnitConversionRequest()
    request.from_unit = "invalid_unit"
    request.to_unit = "kilometer"
    request.value = 1000

    response = convert_units(request)

    assert response.error != ""