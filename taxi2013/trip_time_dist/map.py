#!/usr/bin/env python
# trip_time_dist
# Author: Sida Ye

from __future__ import division
import sys

for line in sys.stdin:
    line = line.strip('\r\n')
    keys, value = line.split('\t')
    values = value.split(',')

    try:
        time_key = keys.split(',')[3].split(' ')[1].split(':')[0]
        duration = values[4]
    except ValueError:
        continue
    if int(values[4]) > 10:
        print '%s\t%s' % (time_key, duration)
