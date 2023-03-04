from datetime import datetime

import shakespeare_translate as st

from application.salary import calculate_salary
from application.db.people import get_employees

if __name__ == '__main__':
    print(datetime.today())
    calculate_salary()
    get_employees()