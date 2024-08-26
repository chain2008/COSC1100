import util

# This line is not part of the function
print(util.cal_age('d'))
print(util.COLLEGE)
i = 3
j = 2 * -i
print(j)
print(i)
msg = "hello world"
print(msg)


from datetime import datetime
# py -m pip install --upgrade pip
# py -m pip install python-dateutil
from dateutil.relativedelta import relativedelta

# Define the two dates
date1 = datetime(2017, 8, 14)
date2 = datetime(2022, 3, 16)

# Calculate the difference
delta = relativedelta(date2, date1)

# Print the difference in years
print(f"Difference in years: {delta.years}")