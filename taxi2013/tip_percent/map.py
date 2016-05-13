#!/usr/bin/env python
# tip_percentage
# Author: Sida Ye

from __future__ import division
import sys

for line in sys.stdin:
    line = line.strip('\r\n')
    keys, value = line.split('\t')
    values = value.split(',')

    try:
        payment = values[10]
        time_key = keys.split(',')[3].split(' ')[1].split(':')[0]
    except ValueError:
        continue
    if payment == 'CRD':
        tips = float(values[-3])
        fare = float(values[-1])

        if fare > 0:
            print '%s\t%f,%f' % (time_key, fare, tips)
        else:
            print '%s\t%f,%f' % (time_key, 0.00, 0.00)
