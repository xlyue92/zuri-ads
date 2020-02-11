# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v1/proto/enums/feed_mapping_criterion_type.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v1/proto/enums/feed_mapping_criterion_type.proto',
  package='google.ads.googleads.v1.enums',
  syntax='proto3',
  serialized_options=_b('\n!com.google.ads.googleads.v1.enumsB\035FeedMappingCriterionTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v1/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V1.Enums\312\002\035Google\\Ads\\GoogleAds\\V1\\Enums\352\002!Google::Ads::GoogleAds::V1::Enums'),
  serialized_pb=_b('\nEgoogle/ads/googleads_v1/proto/enums/feed_mapping_criterion_type.proto\x12\x1dgoogle.ads.googleads.v1.enums\x1a\x1cgoogle/api/annotations.proto\"\x8d\x01\n\x1c\x46\x65\x65\x64MappingCriterionTypeEnum\"m\n\x18\x46\x65\x65\x64MappingCriterionType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12 \n\x1cLOCATION_EXTENSION_TARGETING\x10\x04\x12\x11\n\rDSA_PAGE_FEED\x10\x03\x42\xf2\x01\n!com.google.ads.googleads.v1.enumsB\x1d\x46\x65\x65\x64MappingCriterionTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v1/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V1.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V1\\Enums\xea\x02!Google::Ads::GoogleAds::V1::Enumsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_FEEDMAPPINGCRITERIONTYPEENUM_FEEDMAPPINGCRITERIONTYPE = _descriptor.EnumDescriptor(
  name='FeedMappingCriterionType',
  full_name='google.ads.googleads.v1.enums.FeedMappingCriterionTypeEnum.FeedMappingCriterionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCATION_EXTENSION_TARGETING', index=2, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DSA_PAGE_FEED', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=167,
  serialized_end=276,
)
_sym_db.RegisterEnumDescriptor(_FEEDMAPPINGCRITERIONTYPEENUM_FEEDMAPPINGCRITERIONTYPE)


_FEEDMAPPINGCRITERIONTYPEENUM = _descriptor.Descriptor(
  name='FeedMappingCriterionTypeEnum',
  full_name='google.ads.googleads.v1.enums.FeedMappingCriterionTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FEEDMAPPINGCRITERIONTYPEENUM_FEEDMAPPINGCRITERIONTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=135,
  serialized_end=276,
)

_FEEDMAPPINGCRITERIONTYPEENUM_FEEDMAPPINGCRITERIONTYPE.containing_type = _FEEDMAPPINGCRITERIONTYPEENUM
DESCRIPTOR.message_types_by_name['FeedMappingCriterionTypeEnum'] = _FEEDMAPPINGCRITERIONTYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FeedMappingCriterionTypeEnum = _reflection.GeneratedProtocolMessageType('FeedMappingCriterionTypeEnum', (_message.Message,), dict(
  DESCRIPTOR = _FEEDMAPPINGCRITERIONTYPEENUM,
  __module__ = 'google.ads.googleads_v1.proto.enums.feed_mapping_criterion_type_pb2'
  ,
  __doc__ = """Container for enum describing possible criterion types for a feed
  mapping.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.enums.FeedMappingCriterionTypeEnum)
  ))
_sym_db.RegisterMessage(FeedMappingCriterionTypeEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
