# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v2/proto/common/asset_types.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v2.proto.enums import mime_type_pb2 as google_dot_ads_dot_googleads__v2_dot_proto_dot_enums_dot_mime__type__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v2/proto/common/asset_types.proto',
  package='google.ads.googleads.v2.common',
  syntax='proto3',
  serialized_options=_b('\n\"com.google.ads.googleads.v2.commonB\017AssetTypesProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v2/common;common\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V2.Common\312\002\036Google\\Ads\\GoogleAds\\V2\\Common\352\002\"Google::Ads::GoogleAds::V2::Common'),
  serialized_pb=_b('\n6google/ads/googleads_v2/proto/common/asset_types.proto\x12\x1egoogle.ads.googleads.v2.common\x1a\x33google/ads/googleads_v2/proto/enums/mime_type.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"K\n\x11YoutubeVideoAsset\x12\x36\n\x10youtube_video_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"=\n\x10MediaBundleAsset\x12)\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.BytesValue\"\xf3\x01\n\nImageAsset\x12)\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.BytesValue\x12.\n\tfile_size\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12G\n\tmime_type\x18\x03 \x01(\x0e\x32\x34.google.ads.googleads.v2.enums.MimeTypeEnum.MimeType\x12\x41\n\tfull_size\x18\x04 \x01(\x0b\x32..google.ads.googleads.v2.common.ImageDimension\"\xa2\x01\n\x0eImageDimension\x12\x32\n\rheight_pixels\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x31\n\x0cwidth_pixels\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12)\n\x03url\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"7\n\tTextAsset\x12*\n\x04text\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\xea\x01\n\"com.google.ads.googleads.v2.commonB\x0f\x41ssetTypesProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v2/common;common\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V2.Common\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V2\\Common\xea\x02\"Google::Ads::GoogleAds::V2::Commonb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v2_dot_proto_dot_enums_dot_mime__type__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_YOUTUBEVIDEOASSET = _descriptor.Descriptor(
  name='YoutubeVideoAsset',
  full_name='google.ads.googleads.v2.common.YoutubeVideoAsset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='youtube_video_id', full_name='google.ads.googleads.v2.common.YoutubeVideoAsset.youtube_video_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=205,
  serialized_end=280,
)


_MEDIABUNDLEASSET = _descriptor.Descriptor(
  name='MediaBundleAsset',
  full_name='google.ads.googleads.v2.common.MediaBundleAsset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='google.ads.googleads.v2.common.MediaBundleAsset.data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=282,
  serialized_end=343,
)


_IMAGEASSET = _descriptor.Descriptor(
  name='ImageAsset',
  full_name='google.ads.googleads.v2.common.ImageAsset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='google.ads.googleads.v2.common.ImageAsset.data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_size', full_name='google.ads.googleads.v2.common.ImageAsset.file_size', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mime_type', full_name='google.ads.googleads.v2.common.ImageAsset.mime_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='full_size', full_name='google.ads.googleads.v2.common.ImageAsset.full_size', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=346,
  serialized_end=589,
)


_IMAGEDIMENSION = _descriptor.Descriptor(
  name='ImageDimension',
  full_name='google.ads.googleads.v2.common.ImageDimension',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='height_pixels', full_name='google.ads.googleads.v2.common.ImageDimension.height_pixels', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width_pixels', full_name='google.ads.googleads.v2.common.ImageDimension.width_pixels', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='google.ads.googleads.v2.common.ImageDimension.url', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=592,
  serialized_end=754,
)


_TEXTASSET = _descriptor.Descriptor(
  name='TextAsset',
  full_name='google.ads.googleads.v2.common.TextAsset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='google.ads.googleads.v2.common.TextAsset.text', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=756,
  serialized_end=811,
)

_YOUTUBEVIDEOASSET.fields_by_name['youtube_video_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_MEDIABUNDLEASSET.fields_by_name['data'].message_type = google_dot_protobuf_dot_wrappers__pb2._BYTESVALUE
_IMAGEASSET.fields_by_name['data'].message_type = google_dot_protobuf_dot_wrappers__pb2._BYTESVALUE
_IMAGEASSET.fields_by_name['file_size'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_IMAGEASSET.fields_by_name['mime_type'].enum_type = google_dot_ads_dot_googleads__v2_dot_proto_dot_enums_dot_mime__type__pb2._MIMETYPEENUM_MIMETYPE
_IMAGEASSET.fields_by_name['full_size'].message_type = _IMAGEDIMENSION
_IMAGEDIMENSION.fields_by_name['height_pixels'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_IMAGEDIMENSION.fields_by_name['width_pixels'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_IMAGEDIMENSION.fields_by_name['url'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_TEXTASSET.fields_by_name['text'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
DESCRIPTOR.message_types_by_name['YoutubeVideoAsset'] = _YOUTUBEVIDEOASSET
DESCRIPTOR.message_types_by_name['MediaBundleAsset'] = _MEDIABUNDLEASSET
DESCRIPTOR.message_types_by_name['ImageAsset'] = _IMAGEASSET
DESCRIPTOR.message_types_by_name['ImageDimension'] = _IMAGEDIMENSION
DESCRIPTOR.message_types_by_name['TextAsset'] = _TEXTASSET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

YoutubeVideoAsset = _reflection.GeneratedProtocolMessageType('YoutubeVideoAsset', (_message.Message,), dict(
  DESCRIPTOR = _YOUTUBEVIDEOASSET,
  __module__ = 'google.ads.googleads_v2.proto.common.asset_types_pb2'
  ,
  __doc__ = """A YouTube asset.
  
  
  Attributes:
      youtube_video_id:
          YouTube video id. This is the 11 character string value used
          in the YouTube video URL.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.common.YoutubeVideoAsset)
  ))
_sym_db.RegisterMessage(YoutubeVideoAsset)

MediaBundleAsset = _reflection.GeneratedProtocolMessageType('MediaBundleAsset', (_message.Message,), dict(
  DESCRIPTOR = _MEDIABUNDLEASSET,
  __module__ = 'google.ads.googleads_v2.proto.common.asset_types_pb2'
  ,
  __doc__ = """A MediaBundle asset.
  
  
  Attributes:
      data:
          Media bundle (ZIP file) asset data. The format of the uploaded
          ZIP file depends on the ad field where it will be used. For
          more information on the format, see the documentation of the
          ad field where you plan on using the MediaBundleAsset. This
          field is mutate only.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.common.MediaBundleAsset)
  ))
_sym_db.RegisterMessage(MediaBundleAsset)

ImageAsset = _reflection.GeneratedProtocolMessageType('ImageAsset', (_message.Message,), dict(
  DESCRIPTOR = _IMAGEASSET,
  __module__ = 'google.ads.googleads_v2.proto.common.asset_types_pb2'
  ,
  __doc__ = """An Image asset.
  
  
  Attributes:
      data:
          The raw bytes data of an image. This field is mutate only.
      file_size:
          File size of the image asset in bytes.
      mime_type:
          MIME type of the image asset.
      full_size:
          Metadata for this image at its original size.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.common.ImageAsset)
  ))
_sym_db.RegisterMessage(ImageAsset)

ImageDimension = _reflection.GeneratedProtocolMessageType('ImageDimension', (_message.Message,), dict(
  DESCRIPTOR = _IMAGEDIMENSION,
  __module__ = 'google.ads.googleads_v2.proto.common.asset_types_pb2'
  ,
  __doc__ = """Metadata for an image at a certain size, either original or resized.
  
  
  Attributes:
      height_pixels:
          Height of the image.
      width_pixels:
          Width of the image.
      url:
          A URL that returns the image with this height and width.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.common.ImageDimension)
  ))
_sym_db.RegisterMessage(ImageDimension)

TextAsset = _reflection.GeneratedProtocolMessageType('TextAsset', (_message.Message,), dict(
  DESCRIPTOR = _TEXTASSET,
  __module__ = 'google.ads.googleads_v2.proto.common.asset_types_pb2'
  ,
  __doc__ = """A Text asset.
  
  
  Attributes:
      text:
          Text content of the text asset.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.common.TextAsset)
  ))
_sym_db.RegisterMessage(TextAsset)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
