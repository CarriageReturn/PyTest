__author__ = 'Xander'

import datetime

dt = datetime.datetime.strptime("20.11.2014", "%d.%m.%Y")

print dt

list = ['Apfel','Banane']


list.append('Birne')

for l in list:
	print l

print list.index('Banane')