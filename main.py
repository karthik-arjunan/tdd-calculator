class StringCalculator:
    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0
        
        delimiter = ","
        if numbers.startswith("//"):
            parts = numbers.split("\n", 1)
            delimiter = parts[0][2:]
            numbers = parts[1]
        
        number_list = list(map(int, numbers.replace("\n", delimiter).split(delimiter)))
        negatives = [num for num in number_list if num < 0]
        if negatives:
            raise ValueError(f"Negatives not allowed: {negatives}")
        
        return sum(number_list)