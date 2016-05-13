#!/usr/bin/env python
# Citibike morning pickup

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
        if len(values) > 1 and values[0] != 'tripduration':
            yield values

def mapper():
    index = rtree.Index()
    neighborhoods = []
    readNeighborhood('NYC.shp', index, neighborhoods)
    agg = {}
    duration_agg = {}

    for values in parseInput():
        try:
            pickup_time = int(values[1].split()[1].split(':')[0])
            pickup_location = (float(values[6].strip('""')), float(values[5].strip('""'))) #long, lat
            pickup_neighborhood = findNeighborhood(pickup_location, index, neighborhoods)
            duration = float(values[0].strip('""'))
        except:
            continue
        if pickup_neighborhood != -1:
            if 6 < pickup_time < 11: # 7:00 to 10:59
                if 5 < duration < 21600:
                    agg[pickup_neighborhood] = agg.get(pickup_neighborhood, 0) + 1
                    duration_agg[pickup_neighborhood] = duration_agg.get(pickup_neighborhood, 0) + duration

    for item in agg.keys():
        print '%s\t%s,%.2f' % (neighborhoods[item][0], agg[item], duration_agg[item])

if __name__ == '__main__':
    mapper()
