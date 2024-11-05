class ShowOff:
    
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.marks = kwargs['marks']
        self.subject = kwargs['subject']
        self.teacher_name = kwargs['teacher_name']
        
    def display(self):
        if self.marks > 60:
            return f"name : {self.name},marks : {self.marks}"
        else:
            return f"subject : {self.subject},teacher_name : {self.teacher_name}"
        
if __name__ == "__main__":
    # Test case 1: Marks greater than 60
    s1 = ShowOff(name='Alice', marks=75, subject='Math', teacher_name='Mr. Smith')
    result1 = s1.display()
    print(result1)  # Output: "name : Alice, marks : 75"

    # Test case 2: Marks equal to 60
    s2 = ShowOff(name='Bob', marks=60, subject='Science', teacher_name='Mrs. Johnson')
    result2 = s2.display()
    print(result2)  # Output: "subject : Science, teacher_name : Mrs. Johnson"

    # Test case 3: Marks less than 60
    s3 = ShowOff(name='Charlie', marks=45, subject='History', teacher_name='Mr. Davis')
    result3 = s3.display()
    print(result3)  # Output: "subject : History, teacher_name : Mr. Davis"

    # Test case 4: A student with a high score in a different subject
    s4 = ShowOff(name='David', marks=80, subject='Music', teacher_name='Mr. Thompson')
    result4 = s4.display()
    print(result4)  # Output: "name : David, marks : 80"
