import re


class NameRule:
    def __init__(self, pattern: str) -> None:
        self._re = re.compile(pattern)

    def is_match(self, name: str) -> bool:
        if not isinstance(name, str):
            return False
        return bool(self._re.fullmatch(name))
