#!/usr/bin/env python
# trip_daily_usage taxi 2015
# Author: Sida Ye

import sys

current_key = None

for line in sys.stdin:
    line = line.strip('\n').split('\t')
    key = line[0]
    value = line[1]
    values = value.split(',')
    duration = float(values[0])

    if current_key == key:
        if 5 < duration < 21600:
            count += 1
    else:
        if current_key:
            print "%s\t%s" % (current_key, count)
        current_key = key
        count = 1

print "%s\t%s" % (current_key, count)
