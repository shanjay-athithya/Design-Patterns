import datetime
class Date:
    def __init__(self, day, month, year): 

        self.date = datetime.date(year, month, day)

    def display(self):
        return str(self.date)

c = Date(16, 9, 2004)
print(c.display())