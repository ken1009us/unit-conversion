# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from units_proto import units_pb2 as units__proto_dot_units__pb2


class UnitConversionServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ConvertUnit = channel.unary_unary(
                '/units_grpc_stub.UnitConversionService/ConvertUnit',
                request_serializer=units__proto_dot_units__pb2.UnitConversionRequest.SerializeToString,
                response_deserializer=units__proto_dot_units__pb2.UnitConversionResponse.FromString,
                )


class UnitConversionServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ConvertUnit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UnitConversionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ConvertUnit': grpc.unary_unary_rpc_method_handler(
                    servicer.ConvertUnit,
                    request_deserializer=units__proto_dot_units__pb2.UnitConversionRequest.FromString,
                    response_serializer=units__proto_dot_units__pb2.UnitConversionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'units_grpc_stub.UnitConversionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UnitConversionService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ConvertUnit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/units_grpc_stub.UnitConversionService/ConvertUnit',
            units__proto_dot_units__pb2.UnitConversionRequest.SerializeToString,
            units__proto_dot_units__pb2.UnitConversionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
