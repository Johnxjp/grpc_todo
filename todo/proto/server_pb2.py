# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/server.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/server.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12proto/server.proto\"\x07\n\x05\x45mpty\"!\n\x11\x43reateListRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"4\n\x10\x41\x64\x64ToListRequest\x12\x11\n\tlist_name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"C\n\x04Item\x12\x0f\n\x07item_id\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x1b\n\x06status\x18\x03 \x01(\x0e\x32\x0b.ItemStatus\"A\n\x17UpdateItemStatusRequest\x12\x11\n\tlist_name\x18\x01 \x01(\t\x12\x13\n\x04item\x18\x02 \x01(\x0b\x32\x05.Item\"*\n\x04List\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x05items\x18\x02 \x03(\x0b\x32\x05.Item\"(\n\x10GetListsResponse\x12\x14\n\x05lists\x18\x01 \x03(\x0b\x32\x05.List\"\x1e\n\x0eGetListRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\'\n\x0fGetListResponse\x12\x14\n\x05items\x18\x01 \x03(\x0b\x32\x05.Item**\n\nItemStatus\x12\x0e\n\nINCOMPLETE\x10\x00\x12\x0c\n\x08\x43OMPLETE\x10\x01\x32\xf1\x01\n\nTodoServer\x12*\n\nCreateList\x12\x12.CreateListRequest\x1a\x06.Empty\"\x00\x12\'\n\tAddToList\x12\x11.AddToListRequest\x1a\x05.Item\"\x00\x12\x35\n\x10UpdateItemStatus\x12\x18.UpdateItemStatusRequest\x1a\x05.Item\"\x00\x12\'\n\x08GetLists\x12\x06.Empty\x1a\x11.GetListsResponse\"\x00\x12.\n\x07GetList\x12\x0f.GetListRequest\x1a\x10.GetListResponse\"\x00\x62\x06proto3'
)

_ITEMSTATUS = _descriptor.EnumDescriptor(
  name='ItemStatus',
  full_name='ItemStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INCOMPLETE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COMPLETE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=415,
  serialized_end=457,
)
_sym_db.RegisterEnumDescriptor(_ITEMSTATUS)

ItemStatus = enum_type_wrapper.EnumTypeWrapper(_ITEMSTATUS)
INCOMPLETE = 0
COMPLETE = 1



_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=22,
  serialized_end=29,
)


_CREATELISTREQUEST = _descriptor.Descriptor(
  name='CreateListRequest',
  full_name='CreateListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='CreateListRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=31,
  serialized_end=64,
)


_ADDTOLISTREQUEST = _descriptor.Descriptor(
  name='AddToListRequest',
  full_name='AddToListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='list_name', full_name='AddToListRequest.list_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='AddToListRequest.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=66,
  serialized_end=118,
)


_ITEM = _descriptor.Descriptor(
  name='Item',
  full_name='Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id', full_name='Item.item_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='Item.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='Item.status', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=120,
  serialized_end=187,
)


_UPDATEITEMSTATUSREQUEST = _descriptor.Descriptor(
  name='UpdateItemStatusRequest',
  full_name='UpdateItemStatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='list_name', full_name='UpdateItemStatusRequest.list_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='item', full_name='UpdateItemStatusRequest.item', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=189,
  serialized_end=254,
)


_LIST = _descriptor.Descriptor(
  name='List',
  full_name='List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='List.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='items', full_name='List.items', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=256,
  serialized_end=298,
)


_GETLISTSRESPONSE = _descriptor.Descriptor(
  name='GetListsResponse',
  full_name='GetListsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='lists', full_name='GetListsResponse.lists', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=300,
  serialized_end=340,
)


_GETLISTREQUEST = _descriptor.Descriptor(
  name='GetListRequest',
  full_name='GetListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='GetListRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=342,
  serialized_end=372,
)


_GETLISTRESPONSE = _descriptor.Descriptor(
  name='GetListResponse',
  full_name='GetListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='GetListResponse.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=374,
  serialized_end=413,
)

_ITEM.fields_by_name['status'].enum_type = _ITEMSTATUS
_UPDATEITEMSTATUSREQUEST.fields_by_name['item'].message_type = _ITEM
_LIST.fields_by_name['items'].message_type = _ITEM
_GETLISTSRESPONSE.fields_by_name['lists'].message_type = _LIST
_GETLISTRESPONSE.fields_by_name['items'].message_type = _ITEM
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['CreateListRequest'] = _CREATELISTREQUEST
DESCRIPTOR.message_types_by_name['AddToListRequest'] = _ADDTOLISTREQUEST
DESCRIPTOR.message_types_by_name['Item'] = _ITEM
DESCRIPTOR.message_types_by_name['UpdateItemStatusRequest'] = _UPDATEITEMSTATUSREQUEST
DESCRIPTOR.message_types_by_name['List'] = _LIST
DESCRIPTOR.message_types_by_name['GetListsResponse'] = _GETLISTSRESPONSE
DESCRIPTOR.message_types_by_name['GetListRequest'] = _GETLISTREQUEST
DESCRIPTOR.message_types_by_name['GetListResponse'] = _GETLISTRESPONSE
DESCRIPTOR.enum_types_by_name['ItemStatus'] = _ITEMSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'proto.server_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  })
_sym_db.RegisterMessage(Empty)

CreateListRequest = _reflection.GeneratedProtocolMessageType('CreateListRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATELISTREQUEST,
  '__module__' : 'proto.server_pb2'
  # @@protoc_insertion_point(class_scope:CreateListRequest)
  })
_sym_db.RegisterMessage(CreateListRequest)

AddToListRequest = _reflection.GeneratedProtocolMessageType('AddToListRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDTOLISTREQUEST,
  '__module__' : 'proto.server_pb2'
  # @@protoc_insertion_point(class_scope:AddToListRequest)
  })
_sym_db.RegisterMessage(AddToListRequest)

Item = _reflection.GeneratedProtocolMessageType('Item', (_message.Message,), {
  'DESCRIPTOR' : _ITEM,
  '__module__' : 'proto.server_pb2'
  # @@protoc_insertion_point(class_scope:Item)
  })
_sym_db.RegisterMessage(Item)

UpdateItemStatusRequest = _reflection.GeneratedProtocolMessageType('UpdateItemStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEITEMSTATUSREQUEST,
  '__module__' : 'proto.server_pb2'
  # @@protoc_insertion_point(class_scope:UpdateItemStatusRequest)
  })
_sym_db.RegisterMessage(UpdateItemStatusRequest)

List = _reflection.GeneratedProtocolMessageType('List', (_message.Message,), {
  'DESCRIPTOR' : _LIST,
  '__module__' : 'proto.server_pb2'
  # @@protoc_insertion_point(class_scope:List)
  })
_sym_db.RegisterMessage(List)

GetListsResponse = _reflection.GeneratedProtocolMessageType('GetListsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETLISTSRESPONSE,
  '__module__' : 'proto.server_pb2'
  # @@protoc_insertion_point(class_scope:GetListsResponse)
  })
_sym_db.RegisterMessage(GetListsResponse)

GetListRequest = _reflection.GeneratedProtocolMessageType('GetListRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETLISTREQUEST,
  '__module__' : 'proto.server_pb2'
  # @@protoc_insertion_point(class_scope:GetListRequest)
  })
_sym_db.RegisterMessage(GetListRequest)

GetListResponse = _reflection.GeneratedProtocolMessageType('GetListResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETLISTRESPONSE,
  '__module__' : 'proto.server_pb2'
  # @@protoc_insertion_point(class_scope:GetListResponse)
  })
_sym_db.RegisterMessage(GetListResponse)



_TODOSERVER = _descriptor.ServiceDescriptor(
  name='TodoServer',
  full_name='TodoServer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=460,
  serialized_end=701,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateList',
    full_name='TodoServer.CreateList',
    index=0,
    containing_service=None,
    input_type=_CREATELISTREQUEST,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AddToList',
    full_name='TodoServer.AddToList',
    index=1,
    containing_service=None,
    input_type=_ADDTOLISTREQUEST,
    output_type=_ITEM,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateItemStatus',
    full_name='TodoServer.UpdateItemStatus',
    index=2,
    containing_service=None,
    input_type=_UPDATEITEMSTATUSREQUEST,
    output_type=_ITEM,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetLists',
    full_name='TodoServer.GetLists',
    index=3,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_GETLISTSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetList',
    full_name='TodoServer.GetList',
    index=4,
    containing_service=None,
    input_type=_GETLISTREQUEST,
    output_type=_GETLISTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TODOSERVER)

DESCRIPTOR.services_by_name['TodoServer'] = _TODOSERVER

# @@protoc_insertion_point(module_scope)
