from dataclasses import dataclass

from src.resources.abstract.model.base_class import ResourceBase
from src.resources.common.model.common_class_values import LocationValues


@dataclass(frozen=True)
class Location:
    location:LocationValues


@dataclass(frozen=True)
class TagBase:
    tag_key: str
    tag_value: str


class TagAggregateResource(ResourceBase):
    def __init__(self, tags:list[TagBase]):
        self.tags:list[TagBase] = tags


class LocationAggregateResource(ResourceBase):
    def __init__(self, location:Location) -> None:
        self.location:Location = location


class TagLocationAggregateResource(ResourceBase):
    def __init__(self, location: Location, tags:list[TagBase]) -> None:
        self.location:Location = location
        self.tags:list[TagBase] = tags