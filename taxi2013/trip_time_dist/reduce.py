#!/usr/bin/env python
# trip_time_dist
# Author: Sida Ye

import sys

current_key = None

for line in sys.stdin:
    line = line.strip('\n').split('\t')
    key = line[0]
    duration = int(line[1])

    if current_key == key:
        count += 1
        total_duration += duration
    else:
        if current_key:
            avg = float(total_duration) / count
            print "%s\t%s,%s,%.2f" % (current_key, count, total_duration, avg)
        current_key = key
        count = 1
        total_duration = duration
avg = float(total_duration) / count
print "%s\t%s,%s,%.2f" % (current_key, count, total_duration, avg)
