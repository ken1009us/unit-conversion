# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: units_proto/units.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17units_proto/units.proto\x12\x0bunits_proto\"J\n\x15UnitConversionRequest\x12\x11\n\tfrom_unit\x18\x01 \x01(\t\x12\x0f\n\x07to_unit\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\x01\"@\n\x16UnitConversionResponse\x12\x17\n\x0f\x63onverted_value\x18\x01 \x01(\x01\x12\r\n\x05\x65rror\x18\x02 \x01(\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'units_proto.units_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_UNITCONVERSIONREQUEST']._serialized_start=40
  _globals['_UNITCONVERSIONREQUEST']._serialized_end=114
  _globals['_UNITCONVERSIONRESPONSE']._serialized_start=116
  _globals['_UNITCONVERSIONRESPONSE']._serialized_end=180
# @@protoc_insertion_point(module_scope)
