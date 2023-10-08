import grpc
import os
import sys

current_directory = os.path.dirname(os.path.realpath(__file__))
myproject_directory = os.path.join(current_directory, '..')
sys.path.append(myproject_directory)

from units_grpc_stub import conversion_service_pb2
from units_grpc_stub import conversion_service_pb2_grpc


def run():
    """
    Establishes a connection to the gRPC server and tests unit conversions.

    Handles any raised exceptions during the connection or conversion processes.
    """
    try:
        channel = grpc.insecure_channel('localhost:50051')
        stub = conversion_service_pb2_grpc.UnitConversionServiceStub(channel)

        test_standard_units(stub)

        test_custom_units(stub)

    except grpc.RpcError as e:
        print(f"An error occurred during the RPC call: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def test_standard_units(stub):
    """
    Tests the conversion of standard units.

    Parameters:
    - stub (conversion_service_pb2_grpc.UnitConversionServiceStub): The stub to make requests to the gRPC server.

    Handles any raised exceptions during the conversion process and prints the converted value.
    """
    try:
        request = conversion_service_pb2.units__proto_dot_units__pb2.UnitConversionRequest()
        request.from_unit = 'meter'
        request.to_unit = 'kilometer'
        request.value = 1000

        response = stub.ConvertUnit(request)

        print('Converted value (standard units): ', response.converted_value)

    except grpc.RpcError as e:
        print(f"An error occurred during the RPC call: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def test_custom_units(stub):
    """
    Tests the conversion of custom units.

    Parameters:
    - stub (conversion_service_pb2_grpc.UnitConversionServiceStub): The stub to make requests to the gRPC server.

    Handles any raised exceptions during the conversion process and prints the converted value.
    """
    try:
        request = conversion_service_pb2.units__proto_dot_units__pb2.UnitConversionRequest()
        request.from_unit = 'miG'
        request.to_unit = 'G'
        request.value = 2048

        response = stub.ConvertUnit(request)

        print('Converted value (custom units): ', response.converted_value)

    except grpc.RpcError as e:
        print(f"An error occurred during the RPC call: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == '__main__':
    run()
