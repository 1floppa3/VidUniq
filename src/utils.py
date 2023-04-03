from dataclasses import dataclass

from validators import url as is_valid_url


@dataclass
class Videos:
    path: list[str]
    url: list[str]


def is_url(url: str) -> bool:
    return is_valid_url(url)
