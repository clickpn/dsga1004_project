#!/usr/bin/env python
# weekday_tip
# Author: Sida Ye


import sys
from datetime import datetime

for line in sys.stdin:
    line = line.strip('\r\n')
    keys, value = line.split('\t')
    values = value.split(',')

    try:
        payment = values[10]
        date = datetime.strptime(values[2], "%Y-%m-%d %H:%M:%S")
        weekday = date.weekday()
    except ValueError:
        continue
    # only consider credit payment
    if payment == 'CRD':
        tips = float(values[-3])
        fare = float(values[-1])
        print "%s\t%.2f,%.2f,%s" % (weekday, fare, tips, 1)
