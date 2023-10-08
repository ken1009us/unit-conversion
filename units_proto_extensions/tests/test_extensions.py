import sys
import os
import pytest

current_directory = os.path.dirname(os.path.realpath(__file__))
myproject_directory = os.path.join(current_directory, '..', '..')
sys.path.append(myproject_directory)

from units_grpc_stub import conversion_service_pb2
from units_proto_extensions.extensions import convert_units


def test_convert_units_success():
    request = conversion_service_pb2.units__proto_dot_units__pb2.UnitConversionRequest()
    request.from_unit = "meter"
    request.to_unit = "kilometer"
    request.value = 1000

    response = convert_units(request)

    assert response.converted_value == 1
    assert response.error == ""

def test_convert_units_failure():
    request = conversion_service_pb2.units__proto_dot_units__pb2.UnitConversionRequest()
    request.from_unit = "invalid_unit"
    request.to_unit = "kilometer"
    request.value = 1000

    response = convert_units(request)

    assert response.error != ""