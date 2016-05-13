#!/usr/bin/env python
# citibike_morning_pickup
# Author: Sida Ye

import sys

def parseInput():
    for line in sys.stdin:
        key, value = line.strip('\n').split('\t')
        values = value.split(',')
        yield key, values

def reducer():
    count_agg = {}
    duration_agg = {}

    for key, values in parseInput():
        pair = key
        count = int(values[0])
        duration = float(values[1])
        count_agg[pair] = count_agg.get(pair, 0) + count
        duration_agg[pair] = duration_agg.get(pair, 0) + duration

    for pair in count_agg.keys():
        try:
            avg_duration = float(duration_agg[pair]) / float(count_agg[pair])
        except:
            continue
        print '%s\t%s,%.2f,%.2f' % (pair, count_agg[pair], duration_agg[pair], avg_duration) 

if __name__ == '__main__':
    reducer()
