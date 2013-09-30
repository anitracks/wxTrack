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

p = re.compile('[0-9\-\.]*')
curTempSoup = BeautifulSoup(str(curTempHtml[0]))
tempStr = curTempSoup.p.string
tempMatch = p.match(tempStr)
tStr = tempMatch.group()
print "Temp",
print(tStr)

curWxSoup = BeautifulSoup(str(curWxHtml[0]))
for d in curWxSoup.find_all('li'):
  if(d.contents[0].string == 'Wind Speed'):
    windParts = d.contents[1].split(' ') # split direction, speed, and label or Gusts
    windDir = windParts[0]
    windSpeed = windParts[1]
    if(windParts[2] == 'G'):
      windGust = windParts[3]
    else:
      windGust = '0';
    print "windDir " + windDir
    print "windSpeed " + str(windSpeed)
    print "windGust " + str(windGust)
  else:
    print(d.contents[0].string),
    m = p.match(d.contents[1].string)
    print(m.group())

