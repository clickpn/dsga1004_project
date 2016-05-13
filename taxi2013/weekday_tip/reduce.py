#!/usr/bin/env python
# weekday_tip
# Author: Sida Ye

import sys

current_key = None
total_fare = 0
total_tips = 0
total_count = 0

for line in sys.stdin:
    line = line.strip('\n').split('\t')
    key = line[0]
    fare, tips, count = map(lambda x: float(x), line[1].split(','))

    if current_key == key:
        total_fare += fare
        total_tips += tips
        total_count += count
    else:
        if current_key:
            if total_fare == 0:
                final_tip_pt = 0
            final_tip_pt = round((float(total_tips) / total_fare) * 100, 2)
            print "%s\t%.0f,%.2f,%.2f" % (current_key, total_count, total_fare, final_tip_pt)
        current_key = key
        total_fare = fare
        total_tips = tips
        total_count = count
if total_fare == 0:
    final_tip_pt = 0
final_tip_pt = round((float(total_tips) / total_fare) * 100, 2)
print "%s\t%.0f,%.2f,%.2f" % (current_key, total_count, total_fare, final_tip_pt)
