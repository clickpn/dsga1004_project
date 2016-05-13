#!/usr/bin/env python
# trip_daily_usage
# Author: Sida Ye

from __future__ import division
import sys

for line in sys.stdin:
    line = line.strip('\r\n')
    values = line.split(',')
    if len(values) > 1 and values[0].strip('"') != 'tripduration':
        try:
            time_key = values[1].strip('"').split(' ')[0]
            duration = float(values[0].strip('"'))
        except ValueError:
            continue
        print '%s\t%.2f,1' % (time_key, duration)
