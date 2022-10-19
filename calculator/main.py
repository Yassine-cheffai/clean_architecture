from functools import reduce


class SimpleCalculator:
    def add(self, *args) -> int:
        """
        calculate the sum of multiple arguments
        """
        return sum(args)

    def sub(self, a: int, b: int) -> int:
        return a - b

    def mul(self, *args) -> int:
        return reduce(lambda x, y: x * y, args)
