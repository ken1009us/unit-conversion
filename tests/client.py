import grpc
import sys
import os

current_directory = os.path.dirname(os.path.realpath(__file__))
myproject_directory = os.path.join(current_directory, '..')
sys.path.append(myproject_directory)

from units_proto import units_pb2
from units_proto import units_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = units_pb2_grpc.UnitConversionServiceStub(channel)

    test_standard_units(stub)

    test_custom_units(stub)


def test_standard_units(stub):
    request = units_pb2.UnitConversionRequest()
    request.from_unit = 'meter'
    request.to_unit = 'kilometer'
    request.value = 1000

    response = stub.ConvertUnit(request)

    print('Converted value (standard units): ', response.converted_value)


def test_custom_units(stub):
    request = units_pb2.UnitConversionRequest()
    request.from_unit = 'miG'
    request.to_unit = 'G'
    request.value = 1024

    response = stub.ConvertUnit(request)

    print('Converted value (custom units): ', response.converted_value)


if __name__ == '__main__':
    run()
