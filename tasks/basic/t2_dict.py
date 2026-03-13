"""
TODO:

foo should accept a dict argument, both keys and values are string.
"""


def foo(x: dict[str, str]) -> None:
    pass


foo({"foo": "bar"})
foo({"foo": 1})  # expect-type-error
