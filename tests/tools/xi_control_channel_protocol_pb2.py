# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xi_control_channel_protocol.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xi_control_channel_protocol.proto',
  package='xi_client_ftest_fw',
  serialized_pb=_b('\n!xi_control_channel_protocol.proto\x12\x12xi_client_ftest_fw\"\xbd\r\n\x0bXiClientAPI\x12\x38\n\x07\x63onnect\x18\x01 \x01(\x0b\x32\'.xi_client_ftest_fw.XiClientAPI.Connect\x12>\n\ndisconnect\x18\x02 \x01(\x0b\x32*.xi_client_ftest_fw.XiClientAPI.Disconnect\x12<\n\tsubscribe\x18\x03 \x01(\x0b\x32).xi_client_ftest_fw.XiClientAPI.Subscribe\x12\x45\n\x0epublish_string\x18\x04 \x01(\x0b\x32-.xi_client_ftest_fw.XiClientAPI.PublishString\x12\x45\n\x0epublish_binary\x18\x05 \x01(\x0b\x32-.xi_client_ftest_fw.XiClientAPI.PublishBinary\x12M\n\x12publish_timeseries\x18\x06 \x01(\x0b\x32\x31.xi_client_ftest_fw.XiClientAPI.PublishTimeseries\x12`\n\x1cpublish_formatted_timeseries\x18\x07 \x01(\x0b\x32:.xi_client_ftest_fw.XiClientAPI.PublishFormattedTimeseries\x12;\n\tsetup_tls\x18\x08 \x01(\x0b\x32(.xi_client_ftest_fw.XiClientAPI.SetupTLS\x1a,\n\x0e_ServerAddress\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\r\x1a\xed\x01\n\x07\x43onnect\x12\x46\n\x0eserver_address\x18\x01 \x01(\x0b\x32..xi_client_ftest_fw.XiClientAPI._ServerAddress\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\x12Z\n\x11mqtt_session_type\x18\x04 \x01(\x0e\x32\x30.xi_client_ftest_fw.XiClientAPI._MqttSessionType:\rCLEAN_SESSION\x12\x1a\n\x12\x63onnection_timeout\x18\x05 \x01(\r\x1a\x0c\n\nDisconnect\x1a/\n\x0c_TopicAndQoS\x12\x12\n\ntopic_name\x18\x01 \x01(\t\x12\x0b\n\x03qos\x18\x02 \x01(\r\x1aQ\n\tSubscribe\x12\x44\n\x0etopic_qos_list\x18\x01 \x03(\x0b\x32,.xi_client_ftest_fw.XiClientAPI._TopicAndQoS\x1a\x34\n\x11PublishCommonData\x12\x12\n\ntopic_name\x18\x01 \x01(\t\x12\x0b\n\x03qos\x18\x02 \x01(\r\x1a\x80\x01\n\rPublishString\x12N\n\x13publish_common_data\x18\x01 \x01(\x0b\x32\x31.xi_client_ftest_fw.XiClientAPI.PublishCommonData\x12\x0f\n\x07payload\x18\x02 \x01(\t\x12\x0e\n\x06retain\x18\x03 \x01(\r\x1a\x80\x01\n\rPublishBinary\x12N\n\x13publish_common_data\x18\x01 \x01(\x0b\x32\x31.xi_client_ftest_fw.XiClientAPI.PublishCommonData\x12\x0f\n\x07payload\x18\x02 \x01(\x0c\x12\x0e\n\x06retain\x18\x03 \x01(\r\x1at\n\x11PublishTimeseries\x12N\n\x13publish_common_data\x18\x01 \x01(\x0b\x32\x31.xi_client_ftest_fw.XiClientAPI.PublishCommonData\x12\x0f\n\x07payload\x18\x02 \x01(\x02\x1a\xb9\x01\n\x1aPublishFormattedTimeseries\x12N\n\x13publish_common_data\x18\x01 \x01(\x0b\x32\x31.xi_client_ftest_fw.XiClientAPI.PublishCommonData\x12\x0c\n\x04time\x18\x02 \x01(\r\x12\x10\n\x08\x63\x61tegory\x18\x03 \x01(\t\x12\x14\n\x0cstring_value\x18\x04 \x01(\t\x12\x15\n\rnumeric_value\x18\x05 \x01(\x02\x1a \n\x08SetupTLS\x12\x14\n\x0c\x63\x61_cert_file\x18\x01 \x01(\t\":\n\x10_MqttSessionType\x12\x13\n\x0fUNCLEAN_SESSION\x10\x00\x12\x11\n\rCLEAN_SESSION\x10\x01\"\x9a\x05\n\x10XiClientCallback\x12O\n\x11on_connect_finish\x18\x01 \x01(\x0b\x32\x34.xi_client_ftest_fw.XiClientCallback.OnConnectFinish\x12H\n\ron_disconnect\x18\x02 \x01(\x0b\x32\x31.xi_client_ftest_fw.XiClientCallback.OnDisconnect\x12S\n\x13on_subscribe_finish\x18\x03 \x01(\x0b\x32\x36.xi_client_ftest_fw.XiClientCallback.OnSubscribeFinish\x12S\n\x13on_message_received\x18\x04 \x01(\x0b\x32\x36.xi_client_ftest_fw.XiClientCallback.OnMessageReceived\x12O\n\x11on_publish_finish\x18\x05 \x01(\x0b\x32\x34.xi_client_ftest_fw.XiClientCallback.OnPublishFinish\x1a)\n\x0fOnConnectFinish\x12\x16\n\x0e\x63onnect_result\x18\x01 \x01(\r\x1a\"\n\x0cOnDisconnect\x12\x12\n\nerror_code\x18\x01 \x01(\r\x1a\x32\n\x11OnSubscribeFinish\x12\x1d\n\x15subscribe_result_list\x18\x01 \x03(\r\x1a\x45\n\x11OnMessageReceived\x12\x12\n\ntopic_name\x18\x01 \x01(\t\x12\x0b\n\x03qos\x18\x02 \x01(\r\x12\x0f\n\x07payload\x18\x03 \x01(\x0c\x1a&\n\x0fOnPublishFinish\x12\x13\n\x0breturn_code\x18\x01 \x01(\r')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_XICLIENTAPI__MQTTSESSIONTYPE = _descriptor.EnumDescriptor(
  name='_MqttSessionType',
  full_name='xi_client_ftest_fw.XiClientAPI._MqttSessionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNCLEAN_SESSION', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLEAN_SESSION', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1725,
  serialized_end=1783,
)
_sym_db.RegisterEnumDescriptor(_XICLIENTAPI__MQTTSESSIONTYPE)


_XICLIENTAPI__SERVERADDRESS = _descriptor.Descriptor(
  name='_ServerAddress',
  full_name='xi_client_ftest_fw.XiClientAPI._ServerAddress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='host', full_name='xi_client_ftest_fw.XiClientAPI._ServerAddress.host', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port', full_name='xi_client_ftest_fw.XiClientAPI._ServerAddress.port', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=637,
  serialized_end=681,
)

_XICLIENTAPI_CONNECT = _descriptor.Descriptor(
  name='Connect',
  full_name='xi_client_ftest_fw.XiClientAPI.Connect',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='server_address', full_name='xi_client_ftest_fw.XiClientAPI.Connect.server_address', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='username', full_name='xi_client_ftest_fw.XiClientAPI.Connect.username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='password', full_name='xi_client_ftest_fw.XiClientAPI.Connect.password', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mqtt_session_type', full_name='xi_client_ftest_fw.XiClientAPI.Connect.mqtt_session_type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='connection_timeout', full_name='xi_client_ftest_fw.XiClientAPI.Connect.connection_timeout', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=684,
  serialized_end=921,
)

_XICLIENTAPI_DISCONNECT = _descriptor.Descriptor(
  name='Disconnect',
  full_name='xi_client_ftest_fw.XiClientAPI.Disconnect',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=923,
  serialized_end=935,
)

_XICLIENTAPI__TOPICANDQOS = _descriptor.Descriptor(
  name='_TopicAndQoS',
  full_name='xi_client_ftest_fw.XiClientAPI._TopicAndQoS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='topic_name', full_name='xi_client_ftest_fw.XiClientAPI._TopicAndQoS.topic_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='qos', full_name='xi_client_ftest_fw.XiClientAPI._TopicAndQoS.qos', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=937,
  serialized_end=984,
)

_XICLIENTAPI_SUBSCRIBE = _descriptor.Descriptor(
  name='Subscribe',
  full_name='xi_client_ftest_fw.XiClientAPI.Subscribe',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='topic_qos_list', full_name='xi_client_ftest_fw.XiClientAPI.Subscribe.topic_qos_list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=986,
  serialized_end=1067,
)

_XICLIENTAPI_PUBLISHCOMMONDATA = _descriptor.Descriptor(
  name='PublishCommonData',
  full_name='xi_client_ftest_fw.XiClientAPI.PublishCommonData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='topic_name', full_name='xi_client_ftest_fw.XiClientAPI.PublishCommonData.topic_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='qos', full_name='xi_client_ftest_fw.XiClientAPI.PublishCommonData.qos', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1069,
  serialized_end=1121,
)

_XICLIENTAPI_PUBLISHSTRING = _descriptor.Descriptor(
  name='PublishString',
  full_name='xi_client_ftest_fw.XiClientAPI.PublishString',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='publish_common_data', full_name='xi_client_ftest_fw.XiClientAPI.PublishString.publish_common_data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='xi_client_ftest_fw.XiClientAPI.PublishString.payload', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='retain', full_name='xi_client_ftest_fw.XiClientAPI.PublishString.retain', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1124,
  serialized_end=1252,
)

_XICLIENTAPI_PUBLISHBINARY = _descriptor.Descriptor(
  name='PublishBinary',
  full_name='xi_client_ftest_fw.XiClientAPI.PublishBinary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='publish_common_data', full_name='xi_client_ftest_fw.XiClientAPI.PublishBinary.publish_common_data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='xi_client_ftest_fw.XiClientAPI.PublishBinary.payload', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='retain', full_name='xi_client_ftest_fw.XiClientAPI.PublishBinary.retain', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1255,
  serialized_end=1383,
)

_XICLIENTAPI_PUBLISHTIMESERIES = _descriptor.Descriptor(
  name='PublishTimeseries',
  full_name='xi_client_ftest_fw.XiClientAPI.PublishTimeseries',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='publish_common_data', full_name='xi_client_ftest_fw.XiClientAPI.PublishTimeseries.publish_common_data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='xi_client_ftest_fw.XiClientAPI.PublishTimeseries.payload', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1385,
  serialized_end=1501,
)

_XICLIENTAPI_PUBLISHFORMATTEDTIMESERIES = _descriptor.Descriptor(
  name='PublishFormattedTimeseries',
  full_name='xi_client_ftest_fw.XiClientAPI.PublishFormattedTimeseries',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='publish_common_data', full_name='xi_client_ftest_fw.XiClientAPI.PublishFormattedTimeseries.publish_common_data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time', full_name='xi_client_ftest_fw.XiClientAPI.PublishFormattedTimeseries.time', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='category', full_name='xi_client_ftest_fw.XiClientAPI.PublishFormattedTimeseries.category', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='string_value', full_name='xi_client_ftest_fw.XiClientAPI.PublishFormattedTimeseries.string_value', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='numeric_value', full_name='xi_client_ftest_fw.XiClientAPI.PublishFormattedTimeseries.numeric_value', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1504,
  serialized_end=1689,
)

_XICLIENTAPI_SETUPTLS = _descriptor.Descriptor(
  name='SetupTLS',
  full_name='xi_client_ftest_fw.XiClientAPI.SetupTLS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ca_cert_file', full_name='xi_client_ftest_fw.XiClientAPI.SetupTLS.ca_cert_file', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1691,
  serialized_end=1723,
)

_XICLIENTAPI = _descriptor.Descriptor(
  name='XiClientAPI',
  full_name='xi_client_ftest_fw.XiClientAPI',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='connect', full_name='xi_client_ftest_fw.XiClientAPI.connect', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='disconnect', full_name='xi_client_ftest_fw.XiClientAPI.disconnect', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='subscribe', full_name='xi_client_ftest_fw.XiClientAPI.subscribe', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='publish_string', full_name='xi_client_ftest_fw.XiClientAPI.publish_string', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='publish_binary', full_name='xi_client_ftest_fw.XiClientAPI.publish_binary', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='publish_timeseries', full_name='xi_client_ftest_fw.XiClientAPI.publish_timeseries', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='publish_formatted_timeseries', full_name='xi_client_ftest_fw.XiClientAPI.publish_formatted_timeseries', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='setup_tls', full_name='xi_client_ftest_fw.XiClientAPI.setup_tls', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_XICLIENTAPI__SERVERADDRESS, _XICLIENTAPI_CONNECT, _XICLIENTAPI_DISCONNECT, _XICLIENTAPI__TOPICANDQOS, _XICLIENTAPI_SUBSCRIBE, _XICLIENTAPI_PUBLISHCOMMONDATA, _XICLIENTAPI_PUBLISHSTRING, _XICLIENTAPI_PUBLISHBINARY, _XICLIENTAPI_PUBLISHTIMESERIES, _XICLIENTAPI_PUBLISHFORMATTEDTIMESERIES, _XICLIENTAPI_SETUPTLS, ],
  enum_types=[
    _XICLIENTAPI__MQTTSESSIONTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=1783,
)


_XICLIENTCALLBACK_ONCONNECTFINISH = _descriptor.Descriptor(
  name='OnConnectFinish',
  full_name='xi_client_ftest_fw.XiClientCallback.OnConnectFinish',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='connect_result', full_name='xi_client_ftest_fw.XiClientCallback.OnConnectFinish.connect_result', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2212,
  serialized_end=2253,
)

_XICLIENTCALLBACK_ONDISCONNECT = _descriptor.Descriptor(
  name='OnDisconnect',
  full_name='xi_client_ftest_fw.XiClientCallback.OnDisconnect',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error_code', full_name='xi_client_ftest_fw.XiClientCallback.OnDisconnect.error_code', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2255,
  serialized_end=2289,
)

_XICLIENTCALLBACK_ONSUBSCRIBEFINISH = _descriptor.Descriptor(
  name='OnSubscribeFinish',
  full_name='xi_client_ftest_fw.XiClientCallback.OnSubscribeFinish',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='subscribe_result_list', full_name='xi_client_ftest_fw.XiClientCallback.OnSubscribeFinish.subscribe_result_list', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2291,
  serialized_end=2341,
)

_XICLIENTCALLBACK_ONMESSAGERECEIVED = _descriptor.Descriptor(
  name='OnMessageReceived',
  full_name='xi_client_ftest_fw.XiClientCallback.OnMessageReceived',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='topic_name', full_name='xi_client_ftest_fw.XiClientCallback.OnMessageReceived.topic_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='qos', full_name='xi_client_ftest_fw.XiClientCallback.OnMessageReceived.qos', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='xi_client_ftest_fw.XiClientCallback.OnMessageReceived.payload', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2343,
  serialized_end=2412,
)

_XICLIENTCALLBACK_ONPUBLISHFINISH = _descriptor.Descriptor(
  name='OnPublishFinish',
  full_name='xi_client_ftest_fw.XiClientCallback.OnPublishFinish',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='return_code', full_name='xi_client_ftest_fw.XiClientCallback.OnPublishFinish.return_code', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2414,
  serialized_end=2452,
)

_XICLIENTCALLBACK = _descriptor.Descriptor(
  name='XiClientCallback',
  full_name='xi_client_ftest_fw.XiClientCallback',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='on_connect_finish', full_name='xi_client_ftest_fw.XiClientCallback.on_connect_finish', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='on_disconnect', full_name='xi_client_ftest_fw.XiClientCallback.on_disconnect', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='on_subscribe_finish', full_name='xi_client_ftest_fw.XiClientCallback.on_subscribe_finish', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='on_message_received', full_name='xi_client_ftest_fw.XiClientCallback.on_message_received', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='on_publish_finish', full_name='xi_client_ftest_fw.XiClientCallback.on_publish_finish', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_XICLIENTCALLBACK_ONCONNECTFINISH, _XICLIENTCALLBACK_ONDISCONNECT, _XICLIENTCALLBACK_ONSUBSCRIBEFINISH, _XICLIENTCALLBACK_ONMESSAGERECEIVED, _XICLIENTCALLBACK_ONPUBLISHFINISH, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1786,
  serialized_end=2452,
)

_XICLIENTAPI__SERVERADDRESS.containing_type = _XICLIENTAPI
_XICLIENTAPI_CONNECT.fields_by_name['server_address'].message_type = _XICLIENTAPI__SERVERADDRESS
_XICLIENTAPI_CONNECT.fields_by_name['mqtt_session_type'].enum_type = _XICLIENTAPI__MQTTSESSIONTYPE
_XICLIENTAPI_CONNECT.containing_type = _XICLIENTAPI
_XICLIENTAPI_DISCONNECT.containing_type = _XICLIENTAPI
_XICLIENTAPI__TOPICANDQOS.containing_type = _XICLIENTAPI
_XICLIENTAPI_SUBSCRIBE.fields_by_name['topic_qos_list'].message_type = _XICLIENTAPI__TOPICANDQOS
_XICLIENTAPI_SUBSCRIBE.containing_type = _XICLIENTAPI
_XICLIENTAPI_PUBLISHCOMMONDATA.containing_type = _XICLIENTAPI
_XICLIENTAPI_PUBLISHSTRING.fields_by_name['publish_common_data'].message_type = _XICLIENTAPI_PUBLISHCOMMONDATA
_XICLIENTAPI_PUBLISHSTRING.containing_type = _XICLIENTAPI
_XICLIENTAPI_PUBLISHBINARY.fields_by_name['publish_common_data'].message_type = _XICLIENTAPI_PUBLISHCOMMONDATA
_XICLIENTAPI_PUBLISHBINARY.containing_type = _XICLIENTAPI
_XICLIENTAPI_PUBLISHTIMESERIES.fields_by_name['publish_common_data'].message_type = _XICLIENTAPI_PUBLISHCOMMONDATA
_XICLIENTAPI_PUBLISHTIMESERIES.containing_type = _XICLIENTAPI
_XICLIENTAPI_PUBLISHFORMATTEDTIMESERIES.fields_by_name['publish_common_data'].message_type = _XICLIENTAPI_PUBLISHCOMMONDATA
_XICLIENTAPI_PUBLISHFORMATTEDTIMESERIES.containing_type = _XICLIENTAPI
_XICLIENTAPI_SETUPTLS.containing_type = _XICLIENTAPI
_XICLIENTAPI.fields_by_name['connect'].message_type = _XICLIENTAPI_CONNECT
_XICLIENTAPI.fields_by_name['disconnect'].message_type = _XICLIENTAPI_DISCONNECT
_XICLIENTAPI.fields_by_name['subscribe'].message_type = _XICLIENTAPI_SUBSCRIBE
_XICLIENTAPI.fields_by_name['publish_string'].message_type = _XICLIENTAPI_PUBLISHSTRING
_XICLIENTAPI.fields_by_name['publish_binary'].message_type = _XICLIENTAPI_PUBLISHBINARY
_XICLIENTAPI.fields_by_name['publish_timeseries'].message_type = _XICLIENTAPI_PUBLISHTIMESERIES
_XICLIENTAPI.fields_by_name['publish_formatted_timeseries'].message_type = _XICLIENTAPI_PUBLISHFORMATTEDTIMESERIES
_XICLIENTAPI.fields_by_name['setup_tls'].message_type = _XICLIENTAPI_SETUPTLS
_XICLIENTAPI__MQTTSESSIONTYPE.containing_type = _XICLIENTAPI
_XICLIENTCALLBACK_ONCONNECTFINISH.containing_type = _XICLIENTCALLBACK
_XICLIENTCALLBACK_ONDISCONNECT.containing_type = _XICLIENTCALLBACK
_XICLIENTCALLBACK_ONSUBSCRIBEFINISH.containing_type = _XICLIENTCALLBACK
_XICLIENTCALLBACK_ONMESSAGERECEIVED.containing_type = _XICLIENTCALLBACK
_XICLIENTCALLBACK_ONPUBLISHFINISH.containing_type = _XICLIENTCALLBACK
_XICLIENTCALLBACK.fields_by_name['on_connect_finish'].message_type = _XICLIENTCALLBACK_ONCONNECTFINISH
_XICLIENTCALLBACK.fields_by_name['on_disconnect'].message_type = _XICLIENTCALLBACK_ONDISCONNECT
_XICLIENTCALLBACK.fields_by_name['on_subscribe_finish'].message_type = _XICLIENTCALLBACK_ONSUBSCRIBEFINISH
_XICLIENTCALLBACK.fields_by_name['on_message_received'].message_type = _XICLIENTCALLBACK_ONMESSAGERECEIVED
_XICLIENTCALLBACK.fields_by_name['on_publish_finish'].message_type = _XICLIENTCALLBACK_ONPUBLISHFINISH
DESCRIPTOR.message_types_by_name['XiClientAPI'] = _XICLIENTAPI
DESCRIPTOR.message_types_by_name['XiClientCallback'] = _XICLIENTCALLBACK

XiClientAPI = _reflection.GeneratedProtocolMessageType('XiClientAPI', (_message.Message,), dict(

  _ServerAddress = _reflection.GeneratedProtocolMessageType('_ServerAddress', (_message.Message,), dict(
    DESCRIPTOR = _XICLIENTAPI__SERVERADDRESS,
    __module__ = 'xi_control_channel_protocol_pb2'
    # @@protoc_insertion_point(class_scope:xi_client_ftest_fw.XiClientAPI._ServerAddress)
    ))
  ,

  Connect = _reflection.GeneratedProtocolMessageType('Connect', (_message.Message,), dict(
    DESCRIPTOR = _XICLIENTAPI_CONNECT,
    __module__ = 'xi_control_channel_protocol_pb2'
    # @@protoc_insertion_point(class_scope:xi_client_ftest_fw.XiClientAPI.Connect)
    ))
  ,

  Disconnect = _reflection.GeneratedProtocolMessageType('Disconnect', (_message.Message,), dict(
    DESCRIPTOR = _XICLIENTAPI_DISCONNECT,
    __module__ = 'xi_control_channel_protocol_pb2'
    # @@protoc_insertion_point(class_scope:xi_client_ftest_fw.XiClientAPI.Disconnect)
    ))
  ,

  _TopicAndQoS = _reflection.GeneratedProtocolMessageType('_TopicAndQoS', (_message.Message,), dict(
    DESCRIPTOR = _XICLIENTAPI__TOPICANDQOS,
    __module__ = 'xi_control_channel_protocol_pb2'
    # @@protoc_insertion_point(class_scope:xi_client_ftest_fw.XiClientAPI._TopicAndQoS)
    ))
  ,

  Subscribe = _reflection.GeneratedProtocolMessageType('Subscribe', (_message.Message,), dict(
    DESCRIPTOR = _XICLIENTAPI_SUBSCRIBE,
    __module__ = 'xi_control_channel_protocol_pb2'
    # @@protoc_insertion_point(class_scope:xi_client_ftest_fw.XiClientAPI.Subscribe)
    ))
  ,

  PublishCommonData = _reflection.GeneratedProtocolMessageType('PublishCommonData', (_message.Message,), dict(
    DESCRIPTOR = _XICLIENTAPI_PUBLISHCOMMONDATA,
    __module__ = 'xi_control_channel_protocol_pb2'
    # @@protoc_insertion_point(class_scope:xi_client_ftest_fw.XiClientAPI.PublishCommonData)
    ))
  ,

  PublishString = _reflection.GeneratedProtocolMessageType('PublishString', (_message.Message,), dict(
    DESCRIPTOR = _XICLIENTAPI_PUBLISHSTRING,
    __module__ = 'xi_control_channel_protocol_pb2'
    # @@protoc_insertion_point(class_scope:xi_client_ftest_fw.XiClientAPI.PublishString)
    ))
  ,

  PublishBinary = _reflection.GeneratedProtocolMessageType('PublishBinary', (_message.Message,), dict(
    DESCRIPTOR = _XICLIENTAPI_PUBLISHBINARY,
    __module__ = 'xi_control_channel_protocol_pb2'
    # @@protoc_insertion_point(class_scope:xi_client_ftest_fw.XiClientAPI.PublishBinary)
    ))
  ,

  PublishTimeseries = _reflection.GeneratedProtocolMessageType('PublishTimeseries', (_message.Message,), dict(
    DESCRIPTOR = _XICLIENTAPI_PUBLISHTIMESERIES,
    __module__ = 'xi_control_channel_protocol_pb2'
    # @@protoc_insertion_point(class_scope:xi_client_ftest_fw.XiClientAPI.PublishTimeseries)
    ))
  ,

  PublishFormattedTimeseries = _reflection.GeneratedProtocolMessageType('PublishFormattedTimeseries', (_message.Message,), dict(
    DESCRIPTOR = _XICLIENTAPI_PUBLISHFORMATTEDTIMESERIES,
    __module__ = 'xi_control_channel_protocol_pb2'
    # @@protoc_insertion_point(class_scope:xi_client_ftest_fw.XiClientAPI.PublishFormattedTimeseries)
    ))
  ,

  SetupTLS = _reflection.GeneratedProtocolMessageType('SetupTLS', (_message.Message,), dict(
    DESCRIPTOR = _XICLIENTAPI_SETUPTLS,
    __module__ = 'xi_control_channel_protocol_pb2'
    # @@protoc_insertion_point(class_scope:xi_client_ftest_fw.XiClientAPI.SetupTLS)
    ))
  ,
  DESCRIPTOR = _XICLIENTAPI,
  __module__ = 'xi_control_channel_protocol_pb2'
  # @@protoc_insertion_point(class_scope:xi_client_ftest_fw.XiClientAPI)
  ))
_sym_db.RegisterMessage(XiClientAPI)
_sym_db.RegisterMessage(XiClientAPI._ServerAddress)
_sym_db.RegisterMessage(XiClientAPI.Connect)
_sym_db.RegisterMessage(XiClientAPI.Disconnect)
_sym_db.RegisterMessage(XiClientAPI._TopicAndQoS)
_sym_db.RegisterMessage(XiClientAPI.Subscribe)
_sym_db.RegisterMessage(XiClientAPI.PublishCommonData)
_sym_db.RegisterMessage(XiClientAPI.PublishString)
_sym_db.RegisterMessage(XiClientAPI.PublishBinary)
_sym_db.RegisterMessage(XiClientAPI.PublishTimeseries)
_sym_db.RegisterMessage(XiClientAPI.PublishFormattedTimeseries)
_sym_db.RegisterMessage(XiClientAPI.SetupTLS)

XiClientCallback = _reflection.GeneratedProtocolMessageType('XiClientCallback', (_message.Message,), dict(

  OnConnectFinish = _reflection.GeneratedProtocolMessageType('OnConnectFinish', (_message.Message,), dict(
    DESCRIPTOR = _XICLIENTCALLBACK_ONCONNECTFINISH,
    __module__ = 'xi_control_channel_protocol_pb2'
    # @@protoc_insertion_point(class_scope:xi_client_ftest_fw.XiClientCallback.OnConnectFinish)
    ))
  ,

  OnDisconnect = _reflection.GeneratedProtocolMessageType('OnDisconnect', (_message.Message,), dict(
    DESCRIPTOR = _XICLIENTCALLBACK_ONDISCONNECT,
    __module__ = 'xi_control_channel_protocol_pb2'
    # @@protoc_insertion_point(class_scope:xi_client_ftest_fw.XiClientCallback.OnDisconnect)
    ))
  ,

  OnSubscribeFinish = _reflection.GeneratedProtocolMessageType('OnSubscribeFinish', (_message.Message,), dict(
    DESCRIPTOR = _XICLIENTCALLBACK_ONSUBSCRIBEFINISH,
    __module__ = 'xi_control_channel_protocol_pb2'
    # @@protoc_insertion_point(class_scope:xi_client_ftest_fw.XiClientCallback.OnSubscribeFinish)
    ))
  ,

  OnMessageReceived = _reflection.GeneratedProtocolMessageType('OnMessageReceived', (_message.Message,), dict(
    DESCRIPTOR = _XICLIENTCALLBACK_ONMESSAGERECEIVED,
    __module__ = 'xi_control_channel_protocol_pb2'
    # @@protoc_insertion_point(class_scope:xi_client_ftest_fw.XiClientCallback.OnMessageReceived)
    ))
  ,

  OnPublishFinish = _reflection.GeneratedProtocolMessageType('OnPublishFinish', (_message.Message,), dict(
    DESCRIPTOR = _XICLIENTCALLBACK_ONPUBLISHFINISH,
    __module__ = 'xi_control_channel_protocol_pb2'
    # @@protoc_insertion_point(class_scope:xi_client_ftest_fw.XiClientCallback.OnPublishFinish)
    ))
  ,
  DESCRIPTOR = _XICLIENTCALLBACK,
  __module__ = 'xi_control_channel_protocol_pb2'
  # @@protoc_insertion_point(class_scope:xi_client_ftest_fw.XiClientCallback)
  ))
_sym_db.RegisterMessage(XiClientCallback)
_sym_db.RegisterMessage(XiClientCallback.OnConnectFinish)
_sym_db.RegisterMessage(XiClientCallback.OnDisconnect)
_sym_db.RegisterMessage(XiClientCallback.OnSubscribeFinish)
_sym_db.RegisterMessage(XiClientCallback.OnMessageReceived)
_sym_db.RegisterMessage(XiClientCallback.OnPublishFinish)


# @@protoc_insertion_point(module_scope)
