class Employee:
    def __init__(self, fname='', lname=''):
        self.fname = fname
        self.lname = lname
    
    def from_string(self, name):
        try:
            l = name.split(' ')
            self.fname = l[0]
            self.lname = l[1]
        except IndexError:
            self.fname = name
        return self
    
    def __str__(self):
        return f'{self.fname} {self.lname}'

if __name__ == '__main__':
    # Test case 1: Initialize with first and last name
    e1 = Employee('John', 'Doe')
    print(e1)  # Output: "John Doe"
    
    # Test case 2: Initialize with a single name (no last name)
    e2 = Employee('Alice')
    print(e2)  # Output: "Alice "
    
    # Test case 3: Initialize with an empty string
    e3 = Employee()
    print(e3)  # Output: " "
    
    # Test case 4: Update an employee's name from a string
    e4 = Employee()
    e4.from_string('Jane Smith')
    print(e4)  # Output: "Jane Smith"
    
    # Test case 5: Update an employee's name from a string with a single name
    e5 = Employee()
    e5.from_string('Tom')
    print(e5)  # Output: "Tom "
