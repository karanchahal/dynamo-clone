# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import dynamo_pb2 as dynamo__pb2


class DynamoInterfaceStub(object):
    """`service` 是用来给gRPC服务定义方法的, 格式固定, 类似于Golang中定义一个接口
    `service` is used to define methods for gRPC services in a fixed format, similar to defining
    an interface in Golang
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Put = channel.unary_unary(
                '/dynamo.DynamoInterface/Put',
                request_serializer=dynamo__pb2.PutRequest.SerializeToString,
                response_deserializer=dynamo__pb2.PutResponse.FromString,
                )
        self.Get = channel.unary_unary(
                '/dynamo.DynamoInterface/Get',
                request_serializer=dynamo__pb2.GetRequest.SerializeToString,
                response_deserializer=dynamo__pb2.GetResponse.FromString,
                )
        self.PutStreaming = channel.stream_stream(
                '/dynamo.DynamoInterface/PutStreaming',
                request_serializer=dynamo__pb2.PutRequest.SerializeToString,
                response_deserializer=dynamo__pb2.PutResponse.FromString,
                )
        self.GetStreaming = channel.stream_stream(
                '/dynamo.DynamoInterface/GetStreaming',
                request_serializer=dynamo__pb2.GetRequest.SerializeToString,
                response_deserializer=dynamo__pb2.GetResponse.FromString,
                )


class DynamoInterfaceServicer(object):
    """`service` 是用来给gRPC服务定义方法的, 格式固定, 类似于Golang中定义一个接口
    `service` is used to define methods for gRPC services in a fixed format, similar to defining
    an interface in Golang
    """

    def Put(self, request, context):
        """一元模式(在一次调用中, 客户端只能向服务器传输一次请求数据, 服务器也只能返回一次响应)
        unary-unary(In a single call, the client can only send request once, and the server can
        only respond once.)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PutStreaming(self, request_iterator, context):
        """client can put multiple requests 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStreaming(self, request_iterator, context):
        """client can get multiple requests
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DynamoInterfaceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Put': grpc.unary_unary_rpc_method_handler(
                    servicer.Put,
                    request_deserializer=dynamo__pb2.PutRequest.FromString,
                    response_serializer=dynamo__pb2.PutResponse.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=dynamo__pb2.GetRequest.FromString,
                    response_serializer=dynamo__pb2.GetResponse.SerializeToString,
            ),
            'PutStreaming': grpc.stream_stream_rpc_method_handler(
                    servicer.PutStreaming,
                    request_deserializer=dynamo__pb2.PutRequest.FromString,
                    response_serializer=dynamo__pb2.PutResponse.SerializeToString,
            ),
            'GetStreaming': grpc.stream_stream_rpc_method_handler(
                    servicer.GetStreaming,
                    request_deserializer=dynamo__pb2.GetRequest.FromString,
                    response_serializer=dynamo__pb2.GetResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dynamo.DynamoInterface', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DynamoInterface(object):
    """`service` 是用来给gRPC服务定义方法的, 格式固定, 类似于Golang中定义一个接口
    `service` is used to define methods for gRPC services in a fixed format, similar to defining
    an interface in Golang
    """

    @staticmethod
    def Put(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dynamo.DynamoInterface/Put',
            dynamo__pb2.PutRequest.SerializeToString,
            dynamo__pb2.PutResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dynamo.DynamoInterface/Get',
            dynamo__pb2.GetRequest.SerializeToString,
            dynamo__pb2.GetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PutStreaming(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/dynamo.DynamoInterface/PutStreaming',
            dynamo__pb2.PutRequest.SerializeToString,
            dynamo__pb2.PutResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStreaming(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/dynamo.DynamoInterface/GetStreaming',
            dynamo__pb2.GetRequest.SerializeToString,
            dynamo__pb2.GetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
