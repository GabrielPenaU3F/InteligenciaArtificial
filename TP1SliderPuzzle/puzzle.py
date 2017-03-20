import sys
from Problem import Problem

params = sys.argv[1].split(',')
if (len(params) == 9):
    problem = Problem(params)

else:
    print 'Incorrect parameters'
