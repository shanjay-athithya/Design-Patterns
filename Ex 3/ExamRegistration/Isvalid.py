import datetime
class ValidityModule:
    @staticmethod
    def is_valid_time(time):
        try:
            datetime.datetime.strptime(time, "%H:%M:%S")
            return True
        except ValueError:
            return False

    @staticmethod
    def is_valid_date(date):
        try:
            datetime.datetime.strptime(date, "%d.%m.%Y")
            return True
        except ValueError:
            return False
