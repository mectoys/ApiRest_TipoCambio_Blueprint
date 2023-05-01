import datetime


class DateFormat:
    # nos permite llamar la funcion sin necesidad de instanciar la clase
    @classmethod
    def convert_date(self, date):
        return datetime.datetime.strftime(date, '%d/%m/%Y')
