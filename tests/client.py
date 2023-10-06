import grpc
import sys
import os

current_directory = os.path.dirname(os.path.realpath(__file__))
myproject_directory = os.path.join(current_directory, '..')
sys.path.append(myproject_directory)

from units_proto import units_pb2
from units_proto import units_pb2_grpc


channel = grpc.insecure_channel('localhost:50051')
stub = units_pb2_grpc.UnitConversionServiceStub(channel)

request = units_pb2.UnitConversionRequest()
request.from_unit = 'meter'
request.to_unit = 'kilometer'
request.value = 1000

response = stub.ConvertUnit(request)

print('Converted value: ', response.converted_value)