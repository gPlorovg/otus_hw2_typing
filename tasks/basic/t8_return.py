from typing import assert_type

"""
TODO:

foo should return an integer argument.
"""


def foo() -> int:
    return 1


assert_type(foo(), int)
assert_type(foo(), str)  # expect-type-error
