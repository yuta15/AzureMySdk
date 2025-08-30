from src.resources.common.model.common_class import TagLocationAggregateResource
from src.resources.common.model.common_class import Location
from src.resources.common.model.common_class import TagBase
from src.resources.network.model.common.common_network_data_value import NetworkPrefix


class VirtualNetwork(TagLocationAggregateResource):
    """
    VNETを表現するクラス
    """
    def __init__(
        self,
        name: str,
        prefixies:list[NetworkPrefix],
        location: Location,
        tags:list[TagBase]=[]
    ) -> None:
        super().__init__(location, tags)
        self.name = name
        self.prefixies = prefixies