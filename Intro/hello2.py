import util

print('This semester is ' + util.semester)
util.semester = '2025 Winter'
print('Next semester is ' + util.semester)
util.COLLEGE = 'UOTI'
# : defines a statement block, https://www.w3schools.com/python/python_syntax.asp
if util.liquor_age('2014-07-01'):
    print('Ok to sell liquor')
else:
    print('Cannot sell liquor')
