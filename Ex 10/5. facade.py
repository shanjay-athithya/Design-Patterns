class Student:
    def __init__(self, name, roll_no):
        self.name = name 
        self.roll_no = roll_no
        self.personal = {}
        self.hobbies = []
        self.professional = []
        
class Registration:
    def __init__(self, name, roll_no):
        stu = Student(name, roll_no)
        self.get_personal_details(stu)
        self.get_hobbies(stu)
        self.get_professsional(stu)
        self._store_details_in_file(stu)
        
    def get_personal_details(self, stu):
        stu.personal['email'] = input("enter student email : ")
        stu.personal['address'] = input("enter your address : ")
    
    def get_hobbies(self, stu):
        for i in range(int(input("enter the no of hobbies : "))):
            stu.hobbies.append(input(f"enter your hobby {i + 1} : "))
        
    def get_professsional(self, stu):
        for i in range(int(input("enter the no of professionals : "))):
            stu.professional.append(input(f"enter your professioanl {i + 1} : "))
            
    def _store_details_in_file(self, student):
        with open(f"{student.roll_no}_details.txt", 'w') as file:
            file.write(f"Name: {student.name}\n")
            file.write(f"Roll Number: {student.roll_no}\n")
            file.write(f"Email: {student.personal['email']}\n")
            file.write(f"Address: {student.personal['address']}\n")
            file.write(f"Hobbies: {', '.join(student.hobbies)}\n")
            file.write(f"Professional Body: {', '.join(student.professional)}\n")

    def display_details(self, student):
        print(f"Name: {student.name}")
        print(f"Roll Number: {student.roll_no}")
        print(f"Email: {student.personal['email']}")
        print(f"Address: {student.personal['address']}")
        print(f"Hobbies: {', '.join(student.hobbies)}")
        print(f"Professional Body: {', '.join(student.professional)}")
        
        
if __name__ == "__main__":
    r = Registration("Shanjay", 124)
        
