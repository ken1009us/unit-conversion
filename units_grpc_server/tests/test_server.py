import pytest
import grpc
import asyncio
import sys
import os
import threading

current_directory = os.path.dirname(os.path.realpath(__file__))
myproject_directory = os.path.join(current_directory, '..')
sys.path.append(myproject_directory)

from concurrent import futures
from units_proto import units_pb2
from units_proto import units_pb2_grpc
from units_grpc_server import server


@pytest.fixture(scope="module")
def grpc_server():
    conversion_server = server.ConversionServer()
    conversion_server.start()

    yield conversion_server

    conversion_server.stop()


def test_grpc_service(grpc_server):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = units_pb2_grpc.UnitConversionServiceStub(channel)
        response = stub.ConvertUnit(units_pb2.UnitConversionRequest(
            from_unit='meter', to_unit='kilometer', value=1000))
        assert response.converted_value == 1