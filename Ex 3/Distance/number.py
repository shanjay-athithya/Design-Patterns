class number:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def number_difference(self):
        return abs(self.num1 - self.num2)

if __name__ == '__main__':
    num1 = 10
    num2 = 5

    distance_calculator = number(num1, num2)
    distance = distance_calculator.number_difference()
    print(f"Absolute Difference between numbers: {distance}")