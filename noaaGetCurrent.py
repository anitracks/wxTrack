# noaaGetCurrent.py
#
# This script collects the current weather for Lincoln, NE
# from the NOAA website.
#
# Seth McNeill
# 2013 September 29

from urllib2 import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://forecast.weather.gov/MapClick.php?lat=40.806862&lon=-96.68167900000003&site=all&smap=1&searchresult=Lincoln%2C%20NE%2C%20USA#.Ukhf6ngzBDJ").read()
soup = BeautifulSoup(html)

curTempHtml = soup.find_all(attrs={'class',"myforecast-current-lrg"}) # current temp
# other current weather conditions
curWxHtml = soup.find_all(attrs={'class',"current-conditions-detail"})

curTempSoup = BeautifulSoup(str(curTempHtml[0]))
tempStr = curTempSoup.p.string

p = re.compile('[0-9\-\.]*')
curWxSoup = BeautifulSoup(str(curWxHtml[0]))
for d in curWxSoup.find_all('li'):
  print(d.contents[0].string),
  m = p.match(d.contents[1].string)
  print(m.group())
#  print(d.contents[1])

