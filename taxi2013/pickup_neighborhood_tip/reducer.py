#!/usr/bin/env python
# pickup_neighboor_tip
# Author: Sida Ye

from __future__ import division
import sys

def parseInput():
    for line in sys.stdin:
        line = line.strip('\n')
        key, value = line.split('\t')
        values = value.split(',')
        yield key, values

def reducer():
    tip_agg = {}
    fare_agg = {}
    for key, values in parseInput():
        neighborhood = key
        tip = float(values[1])
        fare = float(values[0])
        tip_agg[neighborhood] = tip_agg.get(neighborhood, 0) + tip
        fare_agg[neighborhood] = fare_agg.get(neighborhood, 0) + fare

    for neighborhood in tip_agg.keys():
        if fare_agg[neighborhood] > 0:
            print '%s\t%.2f' % (neighborhood, (tip_agg[neighborhood] / fare_agg[neighborhood]) * 100)

if __name__ == '__main__':
    reducer()
