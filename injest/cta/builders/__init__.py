import typing
import urllib.parse


def _constructAPI(url: str, **kwargs) -> str:
    """
    _constructAPI _summary_

    _extended_summary_

    :param url: _description_
    :type url: str
    :return: _description_
    :rtype: str
    """
    data: dict[str, typing.Any] = {}

    key: str
    val: typing.Any
    for key, val in kwargs.items():
        if val is None:
            continue

        if len(str(val)) == 0:
            continue

        data[key] = val

    params: str = urllib.parse.urlencode(query=data)
    return f"{url}?{params}"
