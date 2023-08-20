from typing import Any


class Greetings:
    def __init__(self, default_name):
        self.default_name = default_name

    def greet(self, name):
        return f"Hello, {name if name else self.default_name}"


c = Greetings("Alan")
print(c.default_name)
print(c.greet())
print(c.greet("David"))


class Temperature:
    def __init__(self, value, scale):
        self.value = value
        self.scale = scale
        if scale == "C":
            self.value_kelvin = value + 273.15
        elif scale == "F":
            self.value_kelvin = (value - 32) * 5 / 9 + 273.15

    def __repr__(self) -> str:
        return f"Temperature({self.value}, {self.scale!r})"

    def __str__(self) -> str:
        return f"Temperature is {self.value} °{self.scale}"

    def __eq__(self, other) -> bool:
        return self.value_kelvin == other.value_kelvin

    def __lt__(self, other):
        return self.value_kelvin < other.value_kelvin


t = Temperature(25, "C")
print(repr(t))  # "Temperature(25, 'C')"
print(str(t))  # "Temperature is 25 °C"
print(t)

tc = Temperature(25, "C")
tf = Temperature(77, "F")
tf2 = Temperature(100, "F")
print(tc == tf)  # True
print(tc < tf2)  # True


class Counter:
    def __init__(self):
        self.counter = 0

    def __call__(self, inc=1):
        self.counter += inc


c = Counter()
print(c.counter)  # 0
c()
print(c.counter)  # 1
c(10)
print(c.counter)  # 11
