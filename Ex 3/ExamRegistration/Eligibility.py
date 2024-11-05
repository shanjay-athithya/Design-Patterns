from datetime import datetime, date
import Current  # Import the Current module
import Difference  # Import the Difference module

class StudentCompetition:
    def __init__(self, name, birthdate, registration_date):
        self.name = name
        self.birthdate = birthdate
        self.registration_date = registration_date

    def calculate_age(self):
        today = date.today()
        age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        return age

    def is_valid_registration(self):
        six_months_ago = Current.Current().months_before(6)  # Use the months_before method from Current module
        return self.registration_date >= six_months_ago

    def is_eligible(self):
        age = self.calculate_age()
        return age <= 17

    def display_registration_status(self):
        if self.is_eligible() and self.is_valid_registration():
            return f"{self.name} is eligible and has a valid registration."
        elif self.is_eligible() and not self.is_valid_registration():
            return f"{self.name} is eligible but has an expired registration."
        else:
            return f"{self.name} is not eligible."

# Driver code for testing the application
if __name__ == "__main__":
    name = input("Enter student's name: ")
    birthdate = datetime.strptime(input("Enter birthdate (YYYY-MM-DD): "), "%Y-%m-%d").date()
    registration_date = datetime.strptime(input("Enter registration date (YYYY-MM-DD): "), "%Y-%m-%d").date()

    student = StudentCompetition(name, birthdate, registration_date)
    registration_status = student.display_registration_status()

    print(registration_status)
