# Домашнее задание к лекции 1. «Import. Module. Package»
# Разработать структуру программы «Бухгалтерия»:
# main.py;
# application/salary.py;
# application/db/people.py.
# Main.py — основной модуль для запуска программы.
# В модуле salary.py функция calculate_salary.
# В модуле people.py функция get_employees.

# Импортировать функции в модуль main.py и вызывать эти функции в конструкции.
# if __name__ == '__main__':
# Сами функции реализовывать не нужно. Достаточно добавить туда какой-либо вывод.

# Познакомиться с модулем datetime. При вызове функций модуля main.py выводить текущую дату.

# Найти интересный для себя пакет на pypi и в файле requirements.txt указать его с актуальной версией. При желании можно написать программу с этим пакетом.

# *5. Создать рядом с файлом main.py модуль dirty_main.py и импортировать все функции с помощью конструкции (необязательное задание).

# from package.module import *

from application.salary import calculate_salary, current_date, days_passed_written
from application.db.people import get_employees

if __name__ == '__main__':

    employee = get_employees()
    employees_salary = calculate_salary()

    print(f'Для сотрудника {employee} с повременной системой оплаты труда на сегодняшний день ({current_date}) начисления за текущий месяц составят {employees_salary} рублей (за {days_passed_written} прошедших дней(дня))')
