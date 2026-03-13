"""
TODO:

Class `Foo` has an instance variable `bar`, which is an integer.
"""


class Foo:
    bar: int
    """Hint: you don't need to write __init__"""


foo = Foo()
foo.bar = 1
foo.bar = "1"  # expect-type-error
