class Convert:
    def convert_hrs_days(self, hrs):
        return hrs/24
    def convert_days_hours(self, hrs):
        return hrs*24
    def convert_man_hrs_days(self, man_hrs):
        return man_hrs/8

c = Convert()

print(c.convert_man_hrs_days(100))
