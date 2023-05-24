# В модуле salary.py функция calculate_salary.
from datetime import datetime
import calendar

from num_to_rus import Converter

conv = Converter()

current_date = datetime.today().date()

days_in_month = calendar.monthrange(current_date.year, current_date.month)[1]
days_passed = current_date.day

days_passed_written = (conv.convert(days_passed))

def calculate_salary():
    his_salary = 100000 / 30 * days_passed
    return round(his_salary, 2)