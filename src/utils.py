from validators import url as is_valid_url


def is_url(url: str) -> bool:
    return is_valid_url(url)
