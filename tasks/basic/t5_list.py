"""
TODO:

foo should accept a list argument, whose elements are string.
"""


def foo(x: list[str]):
    pass


foo(["foo", "bar"])
foo(["foo", 1])  # expect-type-error
