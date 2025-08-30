from enum import Enum
from ipaddress import IPv4Network
from abc import ABC, abstractmethod

from src.resources.abstract.model.base_class_values import NameRule


class LocationValues(Enum):
    JAPAN_EAST = "Japan East"
    JAPAN_WEST = "Japan West"


class TagKeyNameRule(NameRule):
    PATTENR = r"^(?!\s)(?!.*\s$).{1,512}$"

    def __init__(self) -> None:
        super().__init__(self.PATTENR)


class NetworkPrefixRule(ABC):
    def __init__(
        self,
        min_prefix_len:int,
        max_prefix_len:int,
    ):
        self.min_prefix_len:int = min_prefix_len
        self.max_prefix_len:int = max_prefix_len

    def is_allowed_network(self, prefix:IPv4Network) -> bool:
        """
        interface関数
        """
        is_allow_prefix = self._check_allowed_network(prefix)
        is_allow_prefix_length = self._check_prefix_length(prefix)
        if is_allow_prefix and is_allow_prefix_length:
            return True
        return False

    def _check_prefix_length(self, prefix:IPv4Network) -> bool:
        """
        prefix lengthを確認する関数
        """
        length = prefix.prefixlen
        if length < self.min_prefix_len or length > self.max_prefix_len:
            return False
        return True

    @abstractmethod
    def _check_allowed_network(self, prefix: IPv4Network) -> bool:...