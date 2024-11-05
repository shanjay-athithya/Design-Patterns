class Average:
    def __init__(self, *args):
        self.marks = args
    def average(self):
        sum = 0
        for mark in self.marks:
            sum += mark
        return sum / len(self.marks)
    
if __name__ == '__main__':
    # Test case 1: Average of five marks
    a1 = Average(2, 3, 3, 2, 3)
    print("Test case 1 average:", a1.average())  # Output: 2.6

    # Test case 2: Average of two marks
    a2 = Average(5, 10)
    print("Test case 2 average:", a2.average())  # Output: 7.5

    # Test case 3: Average of an empty set of marks
    a3 = Average()
    print("Test case 3 average:", a3.average())  # Output: 0.0

    # Test case 4: Average of a single mark
    a4 = Average(8)
    print("Test case 4 average:", a4.average())  # Output: 8.0

    # Test case 5: Average of negative marks
    a5 = Average(-2, -4, -6)
    print("Test case 5 average:", a5.average())  # Output: -4.0
