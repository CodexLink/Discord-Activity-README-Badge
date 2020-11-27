from typing import Final, Optional, TypedDict


SEMANTIC_VERSION_DIVIDER : Final = "-"
class SEMANTIC_VERSION(TypedDict, Final):
    MAJOR: int
    MINOR: int
    PATCH: int
    IDENTIFIERS: Optional[str]


PRODUCT_VERSION : SEMANTIC_VERSION = {
    "MAJOR": 0,
    "MINOR": 0,
    "PATCH": 0,
    "IDENTIFIERS": "11262020"
}

ON_DISPLAY_PRINT = """
 Hello.
"""


# Assert Tests
