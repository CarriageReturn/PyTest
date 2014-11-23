__author__ = 'Xander'

import urllib2
import xml.etree.ElementTree as ET

content = urllib2.urlopen("http://www.earthtools.org/timezone/40.71417/-74.00639").read()

print content

root = ET.fromstring(content)

print root.find("localtime").text