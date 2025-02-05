class StringCalculator:
    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0
        
        delimiter = ","
        if numbers.startswith("//"):
            parts = numbers.split("\n", 1)
            delimiter = parts[0][2:]
            numbers = parts[1]
        
        return sum(map(int, numbers.replace("\n", delimiter).split(delimiter)))