from typing import Union


class Calculator:
    def divide(self, x: Union[int, float], y: Union[int, float]) -> int | float:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("both arguments should be numbers")
        if y == 0:
            raise ZeroDivisionError("cannot divide by zero")
        return x / y

    def add(self, x: Union[int, float], y: Union[int, float]) -> int | float:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("both arguments should be numbers")
        return x + y


if __name__ == '__main__':
    calculator = Calculator().divide(6, 3)