from __future__ import print_function

from dateutil.parser import parse as dateuitil_parser
import radar

print(radar.random_date(start='2013-05-24', stop='2013-07-01', parse=dateuitil_parser))

print(radar.random_datetime(start='2013-05-24T00:00:00', stop='2013-05-24T23:59:59', parse=radar.utils.parse))

start = radar.utils.parse('2012-01-01')

stop = radar.utils.parse('2013-01-01')

print(radar.random_datetime(start=start, stop=stop))

print(radar.random_datetime(start=start))

print(radar.random_datetime(stop=stop))

print(radar.random_time(start='2012-01-01T00:00:00', stop='2012-01-01T23:59:59'))
