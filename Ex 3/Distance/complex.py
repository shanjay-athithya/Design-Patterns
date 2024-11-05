class ComplexDistanceCalculator:
    def __init__(self, complex1, complex2):
        self.complex1 = complex1
        self.complex2 = complex2

    def complex_distance(self):
        real_part_diff = self.complex1.real - self.complex2.real
        imag_part_diff = self.complex1.imag - self.complex2.imag
        return (real_part_diff ** 2 + imag_part_diff ** 2) ** 0.5

if __name__ == '__main__':
    complex1 = 1 + 2j
    complex2 = 3 + 4j

    distance_calculator = ComplexDistanceCalculator(complex1, complex2)
    distance = distance_calculator.complex_distance()
    print(f"Euclidean Distance between complex numbers: {distance}")
