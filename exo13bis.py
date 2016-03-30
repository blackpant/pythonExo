#same as the exo 13 but with try except
from sys import argv

try:

    script, first, second, third = argv

    print "The script is called:", script
    print "Your first variable is:", first
    print "Your second variable is:", second
    print "Your third variable is:", third
except Exception:

    print "You must give 3 arguments.!!!!"
