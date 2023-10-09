import json
import os
import re
import sys

from pathlib import Path
from units_grpc_stub import conversion_service_pb2
from units_core.units import Units

current_directory = os.path.dirname(os.path.realpath(__file__))
myproject_directory = os.path.join(current_directory, '..')
sys.path.append(myproject_directory)

units_converter = Units()

project_root = Path(__file__).resolve().parents[2]
file_path = project_root / 'unit-conversion' / 'config' / 'conversions.json'

with open(file_path, 'r', encoding="utf-8") as file:
    custom_units = json.load(file)
    for obj, definition in custom_units.items():
        match = re.match(r'(\d+)([a-zA-Z]+)', obj)
        if match:
            prefix, base_unit_name = match.groups()
            factor = int(prefix)
            base_definition = definition.split(' / ')[0]
            num = int(definition.split(' ')[-1]) * factor
            definition = f'{base_definition} / {num}'
            unit_name = base_unit_name
        else:
            unit_name = obj
        units_converter.unit_registry.define(f'{unit_name} = {definition}')
        print(f"Defined {unit_name} = {definition}")


def convert_units(request: conversion_service_pb2.units__proto_dot_units__pb2.UnitConversionRequest
                  ) -> conversion_service_pb2.units__proto_dot_units__pb2.UnitConversionResponse:
    """
    Convert units from the provided request.

    Parameters:
    - request (UnitConversionRequest): The request containing the value, from_unit, and to_unit.

    Returns:
    - UnitConversionResponse: The response containing the converted value or an error message.

    Raises:
    - ValueError: If there is an issue with the provided value or units.
    - Exception: For general exceptions not caught by specific error handling.
    """

    response = conversion_service_pb2.units__proto_dot_units__pb2.UnitConversionResponse()

    try:
        converted_value = units_converter.convert(request.value, request.from_unit, request.to_unit)
        response.converted_value = converted_value
    except ValueError as e:
        response.error = f"Value Error: {str(e)}"
    except Exception as e:
        response.error = f"An error occurred: {str(e)}"


    return response
