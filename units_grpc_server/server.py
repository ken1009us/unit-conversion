import grpc
import os
import signal
import sys

current_directory = os.path.dirname(os.path.realpath(__file__))
myproject_directory = os.path.join(current_directory, '..')
sys.path.append(myproject_directory)

from concurrent import futures
from units_grpc_stub import conversion_service_pb2
from units_grpc_stub import conversion_service_pb2_grpc
from units_proto_extensions.extensions import convert_units


class ConversionServer():
    """
    A class to represent the gRPC server for unit conversions.

    ...

    Attributes
    ----------
    server : grpc.Server
        The gRPC server instance.

    Methods
    -------
    start():
        Starts the gRPC server.
    stop(signum, frame):
        Stops the gRPC server.
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the ConversionServer object.
        """
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        conversion_service_pb2_grpc.add_UnitConversionServiceServicer_to_server(
            ConversionServiceImpl(), self.server)
        self.server.add_insecure_port('[::]:50051')

    def start(self):
        """Starts the gRPC server."""
        print('Starting server. Listening on port 50051...')
        self.server.start()

    def stop(self):
        """Stops the gRPC server."""
        print('Stopping server.')
        self.server.stop(0)


class ConversionServiceImpl(conversion_service_pb2_grpc.UnitConversionServiceServicer):
    """
    A class to represent the gRPC service implementation for unit conversions.

    ...

    Methods
    -------
    ConvertUnit(request, context):
        Converts units based on the provided request.
    """

    def ConvertUnit(self, request, context):
        """
        Converts units based on the provided request.

        Parameters:
        - request (conversion_service_pb2.UnitConversionRequest): The request containing the value, from_unit, and to_unit.
        - context (grpc.ServicerContext): The context of the gRPC request.

        Returns:
        - conversion_service_pb2.UnitConversionResponse: The response containing the converted value.
        """

        try:
            response = convert_units(request)
            return response

        except Exception as e:
            print(f"Error occurred: {e}")
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            return conversion_service_pb2.UnitConversionResponse()


if __name__ == "__main__":
    conversion_server = ConversionServer()
    conversion_server.start()

    signal.signal(signal.SIGINT, conversion_server.stop)
    signal.signal(signal.SIGTERM, conversion_server.stop)

    conversion_server.server.wait_for_termination()
