__author__ = 'Xander'

import datetime


dt = datetime.datetime.strptime("20.11.2014", "%d.%m.%Y")

print dt

fruits = ['Apfel', 'Banane', 'Orangen']

for l in fruits:
    print l

print fruits.index('Banane')

