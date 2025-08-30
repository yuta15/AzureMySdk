from src.resources.common.model.common_class import ResourceBase
from src.resources.network.model.common.common_network_data_value import NetworkPrefix


class Subnet(ResourceBase):
    def __init__(self, name, prefix) -> None:
        self.name:str = name
        self.prefix:NetworkPrefix = prefix