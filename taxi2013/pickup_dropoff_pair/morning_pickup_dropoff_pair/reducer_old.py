#!/usr/bin/env python
# pickup_dropoff_pair_morning_duration
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
    distance_agg = {}
    numPass_agg = {}
    fare_agg = {}
    tips_agg = {}

    for key, values in parseInput():
        pair = key
        count = int(values[0])
        duration = float(values[1])
        distance = float(values[2])
        numPass = float(values[3])
        fare = float(values[4])
        tips = float(values[5])
        count_agg[pair] = count_agg.get(pair, 0) + count
        duration_agg[pair] = duration_agg.get(pair, 0) + duration
        distance_agg[pair] = distance_agg.get(pair, 0) + distance
        numPass_agg[pair] = numPass_agg.get(pair, 0) + numPass
        fare_agg[pair] = fare_agg.get(pair, 0) + fare
        tips_agg[pair] = tips_agg.get(pair, 0) + tips

    for pair in count_agg.keys():
        print '%s\t%s,%.2f,%.2f,%.2f,%.2f,%.2f' % (pair, count_agg[pair], duration_agg[pair], distance_agg[pair], numPass_agg[pair], fare_agg[pair], tips_agg[pair])

if __name__ == '__main__':
    reducer()
