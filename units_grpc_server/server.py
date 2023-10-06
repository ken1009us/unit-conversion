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


class ConversionServiceImpl(units_pb2_grpc.UnitConversionServiceServicer):
    def ConvertUnit(self, request, context):
        # Delegate the conversion to the units-proto-extensions function
        response = convert_units(request)

        return response


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

units_pb2_grpc.add_UnitConversionServiceServicer_to_server(ConversionServiceImpl(), server)

print('Starting server. Listening on port 50051...')
server.add_insecure_port('[::]:50051')
server.start()

server.wait_for_termination()

