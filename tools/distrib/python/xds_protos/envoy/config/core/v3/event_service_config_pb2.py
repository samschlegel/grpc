# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/config/core/v3/event_service_config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.config.core.v3 import grpc_service_pb2 as envoy_dot_config_dot_core_dot_v3_dot_grpc__service__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from udpa.annotations import versioning_pb2 as udpa_dot_annotations_dot_versioning__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/envoy/config/core/v3/event_service_config.proto\x12\x14\x65nvoy.config.core.v3\x1a\'envoy/config/core/v3/grpc_service.proto\x1a\x1dudpa/annotations/status.proto\x1a!udpa/annotations/versioning.proto\x1a\x17validate/validate.proto\"\x9c\x01\n\x12\x45ventServiceConfig\x12\x39\n\x0cgrpc_service\x18\x01 \x01(\x0b\x32!.envoy.config.core.v3.GrpcServiceH\x00:+\x9a\xc5\x88\x1e&\n$envoy.api.v2.core.EventServiceConfigB\x1e\n\x17\x63onfig_source_specifier\x12\x03\xf8\x42\x01\x42\x8b\x01\n\"io.envoyproxy.envoy.config.core.v3B\x17\x45ventServiceConfigProtoP\x01ZBgithub.com/envoyproxy/go-control-plane/envoy/config/core/v3;corev3\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'envoy.config.core.v3.event_service_config_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"io.envoyproxy.envoy.config.core.v3B\027EventServiceConfigProtoP\001ZBgithub.com/envoyproxy/go-control-plane/envoy/config/core/v3;corev3\272\200\310\321\006\002\020\002'
  _EVENTSERVICECONFIG.oneofs_by_name['config_source_specifier']._options = None
  _EVENTSERVICECONFIG.oneofs_by_name['config_source_specifier']._serialized_options = b'\370B\001'
  _EVENTSERVICECONFIG._options = None
  _EVENTSERVICECONFIG._serialized_options = b'\232\305\210\036&\n$envoy.api.v2.core.EventServiceConfig'
  _globals['_EVENTSERVICECONFIG']._serialized_start=206
  _globals['_EVENTSERVICECONFIG']._serialized_end=362
# @@protoc_insertion_point(module_scope)