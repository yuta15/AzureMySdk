
from ipaddress import IPv4Network
from src.resources.abstract.model.base_class_values import NameRule
from src.resources.common.model.common_class_values import NetworkPrefixRule


class VirtualNetworkNameRule(NameRule):
    """
    命名規則
    """
    PATTERN = r"^(?:[A-Za-z0-9][A-Za-z0-9._-]{0,62}[A-Za-z0-9_])$"

    def __init__(self) -> None:
        super().__init__(self.PATTERN)


class VirtualNetworkPrefixRule(NetworkPrefixRule):
    min_prefix_len:int = 2
    max_prefix_len:int = 29
    allowed_prefixies: list = [
        IPv4Network("10.0.0.0/8"),
        IPv4Network("172.16.0.0/12"),
        IPv4Network("192.168.0.0/16")
    ]

    def __init__(self):
        super().__init__(
            self.min_prefix_len,
            self.max_prefix_len,
        )

    def _check_allowed_network(self, prefix: IPv4Network) -> bool:
        """
        Networkの整合性をチェック
        """
        for allowed_prefix in self.allowed_prefixies:
            if prefix.subnet_of(allowed_prefix):
                return True
        return False


class SubnetNameRule(NameRule):
    """
    命名規則
    """
    PATTERN = r"^(?:[A-Za-z0-9][A-Za-z0-9._-]{0,78}[A-Za-z0-9_])$"

    def __init__(self) -> None:
        super().__init__(self.PATTERN)


class SubnetPrefixRule(NetworkPrefixRule):
    max_prefix_len:int = 29

    def __init__(self, vnet_prefixies:list[IPv4Network]):
        self.vnet_prefixies = vnet_prefixies
        self.min_prefix_len = 24
        self.match_vnet_prefix:IPv4Network

    def _check_allowed_network(self, prefix: IPv4Network) -> bool:
        for allowed_prefix in self.vnet_prefixies:
            if prefix.subnet_of(allowed_prefix):
                self.match_vnet_prefix = allowed_prefix
                return True
        return False

    def _check_prefix_length(self, prefix: IPv4Network) -> bool:
        self.min_prefix_len = self.match_vnet_prefix.prefixlen
        if not self.min_prefix_len:
            return False
        length = prefix.prefixlen
        if length < self.min_prefix_len or length > self.max_prefix_len:
            return False
        return True