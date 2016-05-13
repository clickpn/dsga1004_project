#!/usr/bin/env python
# trip_in_day
# Author: Sida Ye

import sys

current_key = None

for line in sys.stdin:
    line = line.strip('\n').split('\t')
    key = line[0]

    if current_key == key:
        count += 1
    else:
        if current_key:
            print "%s\t%s" % (current_key, count)
        current_key = key
        count = 1

print "%s\t%s" % (current_key, count)
