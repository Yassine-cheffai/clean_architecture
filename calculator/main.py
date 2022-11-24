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
        if 0 in args:
            raise ValueError
        return reduce(lambda x, y: x * y, args)

    def div(self, a: int, b: int) -> float:
        if not b:
            return float("inf")
        return a / b

    def avg(
        self, values: list[int | float], lt: None | int = None, ut: None | int = None
    ) -> float:
        filtred_values = []
        if ut and lt:
            for value in values:
                if value in range(lt, ut + 1):
                    filtred_values.append(value)
            return sum(filtred_values) / len(filtred_values) if filtred_values else 0

        if ut and not lt:
            for value in values:
                if value <= ut:
                    filtred_values.append(value)
            return sum(filtred_values) / len(filtred_values) if filtred_values else 0

        if not ut and lt:
            for value in values:
                if value >= lt:
                    filtred_values.append(value)
            return sum(filtred_values) / len(filtred_values) if filtred_values else 0

        return sum(values) / len(values) if values else 0
