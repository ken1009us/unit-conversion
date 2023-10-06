import sys
import os
import json
import re

current_directory = os.path.dirname(os.path.realpath(__file__))
myproject_directory = os.path.join(current_directory, '..')
sys.path.append(myproject_directory)

from pathlib import Path
from units_proto.units_pb2 import UnitConversionRequest, UnitConversionResponse
from units_core.units import Units


units_converter = Units()

project_root = Path(__file__).resolve().parents[2]
file_path = project_root / 'unit-conversion' / 'config' / 'conversions.json'
with open(file_path, 'r') as file:
    custom_units = json.load(file)
    for object, definition in custom_units.items():
        match = re.match(r'(\d+)([a-zA-Z]+)', object)
        if match:
            prefix, base_unit_name = match.groups()
            factor = int(prefix)
            base_definition = definition.split(' / ')[0]
            num = int(definition.split(' ')[-1]) * factor
            definition = f'{base_definition} / {num}'
            unit_name = base_unit_name
        else:
            unit_name = object
        units_converter.unit_registry.define(f'{unit_name} = {definition}')
        print(f"Defined {unit_name} = {definition}")


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
