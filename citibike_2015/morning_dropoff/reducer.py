#!/usr/bin/env python
# citibike_morning_dropoff
# Author: Sida Ye

import sys

def parseInput():
    for line in sys.stdin:
        key, value = line.strip('\n').split('\t')
        values = value.split(',')
        yield key, values

def reducer():
    count_agg = {}

    for key, values in parseInput():
        pair = key
        count = int(values[0])
        count_agg[pair] = count_agg.get(pair, 0) + count

    for pair in count_agg.keys():
        print '%s\t%s' % (pair, count_agg[pair])

if __name__ == '__main__':
    reducer()
