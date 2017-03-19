import sys
from Problem import Problem

if (len(sys.argv) == 10) or (len(sys.argv) == 17):
    problem = Problem(sys.argv[1:])
else:
    print 'Parametros incorrectos'
