from datetime import date, datetime
class Current:
    def __init__(self):
        self.time = datetime.now().strftime("%H:%M:%S")
        self.date = date.today()
    def current_time(self):
        return self.time

    def current_date(self):
        return self.date.strftime("%d-%m-%Y")

    def current_date_diff(self):
        return  self.date.strftime("%m-%d-%Y")
    
    def __str__(self):
        a = self.date.strftime("%d-%m-%Y")
        return f"the current time is : {self.time}, the current date is : {a}"

    def display(self):
        print(self.time)
        print(self.date.strftime("%d-%m-%Y"))
        
c = Current()
print(c.current_date())
print(c.current_date_diff())
print(c)