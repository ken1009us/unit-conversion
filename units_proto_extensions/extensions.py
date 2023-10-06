import sys
import os

current_directory = os.path.dirname(os.path.realpath(__file__))
myproject_directory = os.path.join(current_directory, '..')
sys.path.append(myproject_directory)

from units_proto.units_pb2 import UnitConversionRequest, UnitConversionResponse
from units_core.units import Units


units_converter = Units()

def convert_units(request: UnitConversionRequest) -> UnitConversionResponse:
    response = UnitConversionResponse()

    try:
        converted_value = units_converter.convert(request.value, request.from_unit, request.to_unit)
        response.converted_value = converted_value
    except ValueError as e:
        response.error = f"Value Error: {str(e)}"
    except Exception as e:
        response.error = f"An error occurred: {str(e)}"


    return response
