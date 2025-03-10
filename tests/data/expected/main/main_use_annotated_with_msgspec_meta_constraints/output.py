# generated by datamodel-codegen:
#   filename:  api_constrained.yaml
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from typing import Annotated, List, Optional, Union

from msgspec import Meta, Struct


class Pet(Struct):
    id: Annotated[int, Meta(ge=0, le=9223372036854775807)]
    name: Annotated[str, Meta(max_length=256)]
    tag: Annotated[Optional[str], Meta(max_length=64)] = None


Pets = List[Pet]


UID = Annotated[int, Meta(ge=0)]


Phone = Annotated[str, Meta(min_length=3)]


FaxItem = Annotated[str, Meta(min_length=3)]


class User(Struct):
    id: Annotated[int, Meta(ge=0)]
    name: Annotated[str, Meta(max_length=256)]
    uid: UID
    tag: Annotated[Optional[str], Meta(max_length=64)] = None
    phones: Optional[List[Phone]] = None
    fax: Optional[List[FaxItem]] = None
    height: Annotated[Optional[Union[int, float]], Meta(ge=1.0, le=300.0)] = None
    weight: Annotated[Optional[Union[float, int]], Meta(ge=1.0, le=1000.0)] = None
    age: Annotated[Optional[int], Meta(gt=0, le=200)] = None
    rating: Annotated[Optional[float], Meta(gt=0.0, le=5.0)] = None


Users = List[User]


Id = str


Rules = List[str]


class Error(Struct):
    code: int
    message: str


class Api(Struct):
    apiKey: Annotated[
        Optional[str], Meta(description='To be used as a dataset parameter value')
    ] = None
    apiVersionNumber: Annotated[
        Optional[str], Meta(description='To be used as a version parameter value')
    ] = None
    apiUrl: Annotated[
        Optional[str], Meta(description="The URL describing the dataset's fields")
    ] = None
    apiDocumentationUrl: Annotated[
        Optional[str], Meta(description='A URL to the API console for each API')
    ] = None


Apis = List[Api]


class Event(Struct):
    name: Optional[str] = None


class Result(Struct):
    event: Optional[Event] = None
