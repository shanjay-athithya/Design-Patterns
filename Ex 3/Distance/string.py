class string:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def hamming_distance(self):
        if len(self.str1) != len(self.str2):
            raise ValueError("Strings must have the same length for Hamming distance")
        
        return sum(c1 != c2 for c1, c2 in zip(self.str1, self.str2))


if __name__ == '__main__':
    str1 = "hello"
    str2 = "hallo"
    distance_calculator = string(str1, str2)
    distance = distance_calculator.hamming_distance()
    print(f"Hamming Distance between '{str1}' and '{str2}': {distance}")
