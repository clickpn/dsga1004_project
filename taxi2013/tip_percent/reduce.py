#!/usr/bin/env python
# tip_percentage
# Author: Sida Ye

import sys

current_key = None
total_fare = 0
total_tips = 0

for line in sys.stdin:
    line = line.strip('\n').split('\t')
    key = line[0]
    fare, tips = map(lambda x: float(x), line[1].split(','))

    if current_key == key:
        total_fare += fare
        total_tips += tips
    else:
        if current_key:
            final_tip_pt = round((float(total_tips) / total_fare) * 100, 2)
            print "%s\t%.2f,%.2f,%.2f" % (current_key, total_fare, total_tips, final_tip_pt)
        current_key = key
        total_fare = fare
        total_tips = tips
final_tip_pt = round((float(total_tips) / total_fare) * 100, 2)
print "%s\t%.2f,%.2f,%.2f" % (current_key, total_fare, total_tips, final_tip_pt)
