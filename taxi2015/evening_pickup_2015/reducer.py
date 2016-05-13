#!/usr/bin/env python
# evening pick up taxi 2015
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

    for key, values in parseInput():
        pair = key
        count = int(values[0])
        duration = float(values[4])
        distance = float(values[3])
        numPass = float(values[1])
        fare = float(values[2])
        count_agg[pair] = count_agg.get(pair, 0) + count
        duration_agg[pair] = duration_agg.get(pair, 0) + duration
        distance_agg[pair] = distance_agg.get(pair, 0) + distance
        numPass_agg[pair] = numPass_agg.get(pair, 0) + numPass
        fare_agg[pair] = fare_agg.get(pair, 0) + fare

    for pair in count_agg.keys():
        try:
            avg_duration = float(duration_agg[pair]) / float(count_agg[pair])
            avg_distance = float(distance_agg[pair]) / float(count_agg[pair])
            avg_numPass = float(numPass_agg[pair]) / float(count_agg[pair])
            avg_fare = float(fare_agg[pair]) / float(count_agg[pair])

        except:
            continue
        print '%s\t%s,%.2f,%.2f,%.2f,%.2f' % (pair, count_agg[pair], avg_duration, avg_distance, avg_numPass, avg_fare) 

if __name__ == '__main__':
    reducer()
