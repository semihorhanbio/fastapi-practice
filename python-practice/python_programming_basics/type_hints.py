from collections.abc import Callable
from typing import Any, cast


def greeting(name: str | None = None) -> str:
    return f"Hello, {name}"


l: list[int | float] = [1, 2.5, 3.14, 4, 5]
t: tuple[int, str, float] = (2, "sss", 4.3)
s: set[int] = {1, 2, 3, 4, 5}
d: dict[str, int] = {"a": 1, "b": 2, "c": 3}

IntStringFloatTuple = tuple[int, float, str]

t: IntStringFloatTuple = (1, "hello", 3.14)


class Post:
    def __init__(self, title: str) -> None:
        self.title = title

    def __str__(self) -> str:
        return self.title


posts: list[Post] = [Post("Post A"), Post("Post B")]


def filter_list(l: list[int], condition: Callable[[int], bool]) -> list[int]:
    return [i for i in l if condition(i)]


def is_even(i: int) -> bool:
    return i % 2 == 0


print(filter_list([1, 2, 3, 4, 5], is_even))


def f(x: Any) -> Any:
    return x


f(10)
f([1, 2, 3])
a = f("a")  # inferred type is "Any"
a = cast(str, f("a"))  # forced type to be "str"
