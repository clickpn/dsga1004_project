#!/usr/bin/env python
# morning pick up taxi 2015
# Author: Sida Ye

import sys
sys.path.append('.')
import matplotlib
matplotlib.use('Agg')
from matplotlib.path import Path
from rtree import index as rtree
import numpy, shapefile, time
import datetime

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
        line = line.strip('\r\n')
        values = line.split(',')
        if len(values) > 1 and values[0] != 'VendorID':
            yield values

def mapper():
    index = rtree.Index()
    neighborhoods = []
    readNeighborhood('NYC.shp', index, neighborhoods)
    agg = {}
    # duration_agg = {}
    numPass_agg = {}
    fare_agg = {}
    distance_agg = {}
    duration_agg = {}

    for values in parseInput():
        try:
            pickup_time = int(values[1].split()[1].split(':')[0])
            pickup_location = (float(values[5]), float(values[6]))
            pickup_neighborhood = findNeighborhood(pickup_location, index, neighborhoods)
            distance = float(values[4])
            fare = float(values[12])
            numPass = float(values[3])
            a = datetime.datetime.strptime(values[1], "%Y-%m-%d %H:%M:%S")
            b = datetime.datetime.strptime(values[2], "%Y-%m-%d %H:%M:%S")
            duration = float((b - a).total_seconds())
        except:
            continue
        if pickup_neighborhood != -1:
            if 6 < pickup_time < 11: # 7:00 to 10:59
                if fare > 0 and duration < 21600:
                    agg[pickup_neighborhood] = agg.get(pickup_neighborhood, 0) + 1
                    fare_agg[pickup_neighborhood] = fare_agg.get(pickup_neighborhood, 0) + fare
                    numPass_agg[pickup_neighborhood] = numPass_agg.get(pickup_neighborhood, 0) + numPass
                    distance_agg[pickup_neighborhood] = distance_agg.get(pickup_neighborhood, 0) + distance
                    duration_agg[pickup_neighborhood] = duration_agg.get(pickup_neighborhood, 0) + duration

    for item in agg.keys():
        print '%s\t%s,%.2f,%.2f,%.2f,%.2f' % (neighborhoods[item][0], agg[item], numPass_agg[item], fare_agg[item], distance_agg[item], duration_agg[item])

if __name__ == '__main__':
    mapper()
