from langdetect import detect
import pickle

class Person:
    def __init__(self, name, department, category, salary, language):
        self.name = name
        self.dept = department
        self.cat = category
        self.sal = salary
        self.lang = language
    
    def __str__(self):
        return f"{self.name} : {self.dept} : {self.cat} : {self.sal} : {self.lang}"

class PplAsn:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        detected_lang = detect(person.name)
        if person.dept == "Security" and detected_lang != person.lang:
            print(f"the security name {person.name} is in :'{detected_lang}',so give in : '{person.lang}'")
            person.name = input("enter the name in mother tongue: ")
        self.people.append(person)

    def display(self, cat, dept):
        if len(self.people) == 0:
            raise Exception("The list is empty")
        else:
            for person in self.people:
                if person.cat == cat and person.dept == dept:
                    print(person)
    
    def bonus(self):
        for person in self.people:
            if person.dept == "Security":
                person.sal += 2000

    def get_unique_faculties(self):
        # Using set comprehension to create a unique set of faculty names
        faculties = {person.name for person in self.people if person.cat == "Faculty"}
        return list(faculties)



    def get_faculties_in_different_departments(self):
        # Using dictionary comprehension to organize faculty names by department
        faculties_by_department = {dept: [person.name for person in self.people if person.cat == "Faculty" and person.dept == dept] for dept in set(person.dept for person in self.people)}

        return faculties_by_department

    def store_people(self):
        with open(r'D:\PYTHON Code\SEM 3\Ex 8\people.pkl', 'wb') as f:
            pickle.dump(self, f)
            
    def __str__(self):
        string = ''
        for person in self.people:
            string += person.__str__() + '\n'
        return string
    
if __name__ == '__main__':
    # Example usage:
    ppl_asn = PplAsn()

    # Add some people to the list
    person1 = Person("John", "IT", "Student", 50000, "English")
    person2 = Person("Alice", "CSE", "Faculty", 60000, "Spanish")
    person3 = Person("அரவிந்த்", "Security", "Staff", 30000, "ta")
    person4 = Person("ശഞ്ജയ് ആദിത്യ", "Security", "Staff", 500, 'en')
    person5 = Person("Charlie", "CSE", "Faculty", 70000, "fr")

    ppl_asn.add_person(person1)
    ppl_asn.add_person(person2)
    ppl_asn.add_person(person3)
    ppl_asn.add_person(person4)
    ppl_asn.add_person(person5)

    # Display people in a specific category and department
    print("A student in IT :")
    ppl_asn.display("Student", "IT")

    # Add bonus to security
    ppl_asn.bonus()

    # Display updated salaries
    for person in ppl_asn.people:
        print(f"{person.name}'s Salary: {person.sal}")

    # Store people using pickle
    ppl_asn.store_people()

    # Get unique list of faculties
    unique_faculties = ppl_asn.get_unique_faculties()
    print("Unique Faculties:", unique_faculties)

    # Get list of faculties in different departments
    faculties_in_different_departments = ppl_asn.get_faculties_in_different_departments()
    print("Faculties in Different Departments:", faculties_in_different_departments)