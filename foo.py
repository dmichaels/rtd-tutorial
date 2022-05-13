"""
Lumache - Python library for FOO lovers (i.e. testing).
"""

__version__ = "0.1.0"


def get_foo(kind=None):
    """
    Return a list of FOO.

    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :raise lumache.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]
    """
    return ["shells", "gorgonzola", "parsley"]
