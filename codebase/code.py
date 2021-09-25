from typing import Optional


def code(arg: Optional[bool]) -> str:
    if arg is None:
        return "a"
    elif arg is True:
        return "b"

    if False:
        return "unreachable"
    return "c"
