class StringCalculator:
    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0
        return sum(map(int, numbers.split(",")))