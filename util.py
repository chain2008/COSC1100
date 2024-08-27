"""Module providing a function printing python version."""
COLLEGE = 'Durham College' # global constant
semester = 'Fall 2024'  # global variable
LIQUOR_AGE = 19
DATE_FORMAT = '%Y-%m-%d'

from datetime import datetime
# py -m pip install --upgrade pip
# py -m pip install python-dateutil
from dateutil.relativedelta import relativedelta

def liquor_age(birthday): # [missing-function-docstring]
    """Function printing python version."""
    birthday = datetime.strptime(birthday, DATE_FORMAT)
    delta = relativedelta(datetime.now(), birthday)

    return delta.years >= LIQUOR_AGE  # : defines a statement block, https://www.w3schools.com/python/python_syntax.asp

