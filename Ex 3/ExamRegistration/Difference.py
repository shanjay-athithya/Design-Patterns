import datetime
class Difference():
    def __init__(self):
        self.currentdate = datetime.datetime.now().date()

    def days_in_month(self, year, month):
        if month == 2:  # February
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                return 29  # Leap year
            else:
                return 28  # Non-leap year
        elif month in [4, 6, 9, 11]:  # April, June, September, November
            return 30
        else:
            return 31  # All other months

    def DifferenceWithCurrent(self, date):
        return (self.currentdate - date).days

    def Difference(self, Date1, Date2):
        return (Date1 - Date2).days

    def days_after(self, days):
        current_date = datetime.datetime.now().date()
        new_date = current_date

        for _ in range(days):
            new_date = self.add_day(new_date)

        return new_date

    def days_before(self, days):
        current_date = datetime.datetime.now().date()
        new_date = current_date

        for _ in range(days):
            new_date = self.subtract_day(new_date)

        return new_date

    def add_day(self, date):
        year, month, day = date.year, date.month, date.day
        if month == 12 and day == 31:
            return datetime.date(year + 1, 1, 1)
        elif day == self.days_in_month(year, month):
            return datetime.date(year, month + 1, 1)
        else:
            return datetime.date(year, month, day + 1)

    def subtract_day(self, date):
        year, month, day = date.year, date.month, date.day
        if month == 1 and day == 1:
            return datetime.date(year - 1, 12, 31)
        elif day == 1:
            return datetime.date(year, month - 1, self.days_in_month(year, month - 1))
        else:
            return datetime.date(year, month, day - 1)

    def months_after(self, months):
        current_date = self.currentdate
        year = current_date.year + (current_date.month + months - 1) // 12
        month = (current_date.month + months - 1) % 12 + 1
        day = min(current_date.day, self.days_in_month(year, month))
        return datetime.date(year, month, day)

    def month_before(self, months):
        current_date = self.currentdate
        year = current_date.year + (current_date.month - months - 1) // 12
        month = (current_date.month - months - 1) % 12 + 1
        day = min(current_date.day, self.days_in_month(year, month))
        return datetime.date(year, month, day)

# You can test the Difference class with the following driver code:
if __name__ == "__main__":
    difference = Difference()
    current_date = datetime.datetime.now().date()

    print("Current Date:", current_date)
    print("Difference with Current:", difference.DifferenceWithCurrent(current_date))
    print("Difference between two dates:", difference.Difference(current_date, current_date))
    print("Date after 5 days:", difference.days_after(5))
    print("Date before 5 days:", difference.days_before(5))
    print("Date 3 months after:", difference.months_after(3))
    print("Date 2 months before:", difference.month_before(2))