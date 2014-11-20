__author__ = 'Xander'

import datetime

def myfunc(str):
    print str
    return


myfunc('Test test test')

lastdate = None

f = open('data.txt', 'r')

for line in f:

    line = line.rstrip()[11:24]

    dt = datetime.datetime.strptime(line, "%H:%M:%S,%f")


    if lastdate is None:
        lastdate = dt
    else:

        if lastdate > dt:
            print str(lastdate) + " " + str(dt)

        lastdate = dt

print "boom"