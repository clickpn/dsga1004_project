#!/usr/bin/env python
# payment_type
# Author: Sida Ye

from __future__ import division
import sys

for line in sys.stdin:
    line = line.strip('\r\n')
    keys, value = line.split('\t')
    values = value.split(',')

    try:
        time_key = keys.split(',')[3].split(' ')[1].split(':')[0]
        payment_type = values[10]
    except ValueError:
        continue

    print '%s,%s\t1' % (time_key, payment_type)
