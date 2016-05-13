#!/usr/bin/env python
# trip_in_day
# Author: Sida Ye

from __future__ import division
import sys

for line in sys.stdin:
    line = line.strip('\r\n')
    keys, values = line.split('\t')
    try:
        time_key = keys.split(',')[3].split(' ')[1].split(':')[0]
    except ValueError:
        continue
    print '{}\t1'.format(time_key)

