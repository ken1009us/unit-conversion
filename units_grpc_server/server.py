import grpc
import sys
import os

current_directory = os.path.dirname(os.path.realpath(__file__))
myproject_directory = os.path.join(current_directory, '..')
sys.path.append(myproject_directory)

from concurrent import futures
from units_proto import units_pb2
from units_proto import units_pb2_grpc
from units_proto_extensions.extensions import convert_units

class ConversionServer():
    def __init__(self):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        units_pb2_grpc.add_UnitConversionServiceServicer_to_server(
            ConversionServiceImpl(), self.server)
        self.server.add_insecure_port('[::]:50051')

    def start(self):
        print('Starting server. Listening on port 50051...')
        self.server.start()

    def stop(self):
        print('Stopping server.')
        self.server.stop(0)


class ConversionServiceImpl(units_pb2_grpc.UnitConversionServiceServicer):
    def ConvertUnit(self, request, context):
        response = convert_units(request)

        return response


if __name__ == "__main__":
    conversion_server = ConversionServer()
    conversion_server.start()
    conversion_server.server.wait_for_termination()