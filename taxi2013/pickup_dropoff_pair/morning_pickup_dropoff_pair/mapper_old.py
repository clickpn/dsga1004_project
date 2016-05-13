#!/usr/bin/env python
# pickup_dropoff_pair_morning_duration
# Author: Sida Ye

import sys
sys.path.append('.')
import matplotlib
matplotlib.use('Agg')
from matplotlib.path import Path
from rtree import index as rtree
import numpy, shapefile, time

def findNeighborhood(location, index, neighborhoods):
    match = index.intersection((location[0], location[1], location[0], location[1]))
    for a in match:
        if any(map(lambda x: x.contains_point(location), neighborhoods[a][1])):
            return a
    return -1

def readNeighborhood(shapeFilename, index, neighborhoods):
    sf = shapefile.Reader(shapeFilename)
    for sr in sf.shapeRecords():
        if sr.record[1] not in ['New York', 'Kings', 'Queens', 'Bronx']: continue
        paths = map(Path, numpy.split(sr.shape.points, sr.shape.parts[1:]))
        bbox = paths[0].get_extents()
        map(bbox.update_from_path, paths[1:])
        index.insert(len(neighborhoods), list(bbox.get_points()[0])+list(bbox.get_points()[1]))
        neighborhoods.append((sr.record[3], paths))
    neighborhoods.append(('UNKNOWN', None))

def parseInput():
    for line in sys.stdin:
        line = line.strip('\n')
        key, value = line.split('\t')
        values = value.split(',')
        keys = key.split(',')
        if len(values) > 1 and values[0] != 'medallion':
            yield keys, values

def mapper():
    index = rtree.Index()
    neighborhoods = []
    readNeighborhood('NYC.shp', index, neighborhoods)
    pair_agg = {}
    duration_agg = {}
    distance_agg = {}
    numPass_agg = {}
    fare_agg = {}
    tips_agg = {}
    for keys, values in parseInput():
        try:
            pickup_time = int(keys[3].split()[1].split(':')[0])
            pickup_location = (float(values[6]), float(values[7]))
            dropoff_location = (float(values[8]), float(values[9]))
            duration = float(values[4])
            distance = float(values[5])
            numPass = float(values[3])
            fare = float(values[-1])
            tips = float(values[-3])
            pickup_neighborhood = findNeighborhood(pickup_location, index, neighborhoods)
            dropoff_neighborhood = findNeighborhood(dropoff_location, index, neighborhoods)
        except:
            continue

        if pickup_neighborhood != -1 and dropoff_location != -1:
            if 6 < pickup_time < 11: # 7:00 to 10:59
                pickup = neighborhoods[pickup_neighborhood][0]
                dropoff = neighborhoods[dropoff_neighborhood][0]
                pair = pickup + ',' + dropoff
                pair_agg[pair] = pair_agg.get(pair, 0) + 1
                duration_agg[pair] = duration_agg.get(pair, 0) + duration
                distance_agg[pair] = distance_agg.get(pair, 0) + distance
                numPass_agg[pair] = numPass_agg.get(pair, 0) + numPass
                if fare > 0:
                    fare_agg[pair] = fare_agg.get(pair, 0) + fare
                tips_agg[pair] = tips_agg.get(pair, 0) + tips

    for item in pair_agg.keys():
        try:
            avg_duration = float(duration_agg[item]) / float(pair_agg[item])
            avg_distance = float(distance_agg[item]) / float(pair_agg[item])
            avg_numPass = float(numPass_agg[item]) / float(pair_agg[item])
            avg_fare = float(fare_agg[item]) / float(pair_agg[item])
            tips_pct = (float(tips_agg[item]) / float(fare_agg[item])) * 100

        except:
            continue
        print '%s\t%s,%.2f,%.2f,%.2f,%.2f,%.2f' % (item, pair_agg[item], avg_duration, avg_distance, avg_numPass, avg_fare, tips_pct)

if __name__ == '__main__':
    mapper()
