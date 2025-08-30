from ipaddress import IPv4Network
from dataclasses import dataclass

from src.resources.abstract.model.base_class_values import NameRule


@dataclass(frozen=True)
class NetworkPrefix:
    prefix:IPv4Network