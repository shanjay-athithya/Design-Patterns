class Classroom:
    def __init__(self, reg_no):
        self.reg = reg_no
        self.name = None
        self.attend = None
        self.cgpa = None
        self.admin = None

    def add_student(self, name, attend, cgpa, admin):
        self.name = name 
        self.attend = attend
        self.cgpa= cgpa
        self.admin = admin

    def check_attendance(self):
        if self.attend < 75:
            return "the attendance is not enough"
        elif self.attend == 100:
            return "full attendance"
        else:
            return f"enough attendance : {self.attend}"
        
    def update_cgpa(self,cgpa_new):
        self.cgpa = cgpa_new
    
    def update_attendance(self, new_attend):
        self.attend = new_attend

    def student_info(self):
        return (f"""
        reg no : {self.reg}
        the student name is : {self.name}
        Attendance : {self.attend}
        cgpa : {self.cgpa}
        admission type : {self.admin}
        """)
    
if '__main__' == __name__:
    s1 = Classroom(1)
    s1.add_student("shanj", 80, 8, "management")
    print(s1.student_info())
    print(s1.check_attendance())
    
    s1.update_attendance(79)
    s1.update_cgpa(8.4)
    print(s1.student_info())