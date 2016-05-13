#!/usr/bin/env python
# trip_daily_usage taxi 2015
# Author: Sida Ye

from __future__ import division
import sys
import datetime

for line in sys.stdin:
    line = line.strip('\r\n')
    values = line.split(',')
    if len(values) > 1 and values[0] != 'VendorID':
        try:
            time_key = values[1].split(' ')[0]
            a = datetime.datetime.strptime(values[1], "%Y-%m-%d %H:%M:%S")
            b = datetime.datetime.strptime(values[2], "%Y-%m-%d %H:%M:%S")
            duration = float((b - a).total_seconds())
        except ValueError:
            continue
        print '%s\t%.2f,1' % (time_key, duration)
