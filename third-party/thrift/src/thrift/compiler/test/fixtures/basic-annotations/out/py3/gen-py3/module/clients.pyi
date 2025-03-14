#
# Autogenerated by Thrift for thrift/compiler/test/fixtures/basic-annotations/src/module.thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#

import folly.iobuf as _fbthrift_iobuf
import thrift.py3.types
import thrift.py3.client
import thrift.py3.common
import typing as _typing
from types import TracebackType

import module.types as _module_types


_MyServiceT = _typing.TypeVar('_MyServiceT', bound='MyService')


class MyService(thrift.py3.client.Client):

    async def ping(
        self,
        *,
        rpc_options: _typing.Optional[thrift.py3.common.RpcOptions]=None
    ) -> None: ...

    async def getRandomData(
        self,
        *,
        rpc_options: _typing.Optional[thrift.py3.common.RpcOptions]=None
    ) -> str: ...

    async def hasDataById(
        self,
        id: int,
        *,
        rpc_options: _typing.Optional[thrift.py3.common.RpcOptions]=None
    ) -> bool: ...

    async def getDataById(
        self,
        id: int,
        *,
        rpc_options: _typing.Optional[thrift.py3.common.RpcOptions]=None
    ) -> str: ...

    async def putDataById(
        self,
        id: int,
        data: str,
        *,
        rpc_options: _typing.Optional[thrift.py3.common.RpcOptions]=None
    ) -> None: ...

    async def lobDataById(
        self,
        id: int,
        data: str,
        *,
        rpc_options: _typing.Optional[thrift.py3.common.RpcOptions]=None
    ) -> None: ...

    async def doNothing(
        self,
        *,
        rpc_options: _typing.Optional[thrift.py3.common.RpcOptions]=None
    ) -> None: ...



_MyServicePrioParentT = _typing.TypeVar('_MyServicePrioParentT', bound='MyServicePrioParent')


class MyServicePrioParent(thrift.py3.client.Client):

    async def ping(
        self,
        *,
        rpc_options: _typing.Optional[thrift.py3.common.RpcOptions]=None
    ) -> None: ...

    async def pong(
        self,
        *,
        rpc_options: _typing.Optional[thrift.py3.common.RpcOptions]=None
    ) -> None: ...



_MyServicePrioChildT = _typing.TypeVar('_MyServicePrioChildT', bound='MyServicePrioChild')


class MyServicePrioChild(MyServicePrioParent):

    async def pang(
        self,
        *,
        rpc_options: _typing.Optional[thrift.py3.common.RpcOptions]=None
    ) -> None: ...



_BadServiceT = _typing.TypeVar('_BadServiceT', bound='BadService')


class BadService(thrift.py3.client.Client):

    async def bar(
        self,
        *,
        rpc_options: _typing.Optional[thrift.py3.common.RpcOptions]=None
    ) -> int: ...

    def createBadInteraction(self) -> BadService_BadInteraction: ...
    def async_createBadInteraction(self) -> BadService_BadInteraction: ...

_BadService_BadInteraction = _typing.TypeVar('_BadService_BadInteraction', bound='BadService_BadInteraction')


class BadService_BadInteraction(thrift.py3.client.Client):

    async def foo(
        self,
        *,
        rpc_options: _typing.Optional[thrift.py3.common.RpcOptions]=None
    ) -> None: ...



_FooBarBazServiceT = _typing.TypeVar('_FooBarBazServiceT', bound='FooBarBazService')


class FooBarBazService(thrift.py3.client.Client):

    async def foo(
        self,
        *,
        rpc_options: _typing.Optional[thrift.py3.common.RpcOptions]=None
    ) -> None: ...

    async def bar(
        self,
        *,
        rpc_options: _typing.Optional[thrift.py3.common.RpcOptions]=None
    ) -> None: ...

    async def baz(
        self,
        *,
        rpc_options: _typing.Optional[thrift.py3.common.RpcOptions]=None
    ) -> None: ...

