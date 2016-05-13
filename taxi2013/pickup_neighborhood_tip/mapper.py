#!/usr/bin/env python
# pickup_neighboor_tip
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
        if len(values) > 1:
            yield values

def mapper():
    index = rtree.Index()
    neighborhoods = []
    readNeighborhood('NYC.shp', index, neighborhoods)
    tip_agg = {}
    fare_agg = {}
    for values in parseInput():
        tips = float(values[-3])
        fare = float(values[-1])
        payment_type = values[10]
        pickup_location = (float(values[6]), float(values[7]))
        pickup_neighborhood = findNeighborhood(pickup_location, index, neighborhoods)
        if pickup_neighborhood != -1:
            if 0 < fare < 800 and payment_type == 'CRD':
                tip_agg[pickup_neighborhood] = tip_agg.get(pickup_neighborhood, 0) + tips
                fare_agg[pickup_neighborhood] = fare_agg.get(pickup_neighborhood, 0) + fare

    for item in tip_agg.keys():
        print '%s\t%s,%s' % (neighborhoods[item][0], fare_agg[item], tip_agg[item])

if __name__ == '__main__':
    mapper()