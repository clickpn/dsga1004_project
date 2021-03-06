#!/usr/bin/env python
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
    agg = {}
    for keys, values in parseInput():
        pickup_time = int(keys[3].split()[1].split(':')[0])
        pickup_location = (float(values[6]), float(values[7]))
        pickup_neighborhood = findNeighborhood(pickup_location, index, neighborhoods)
        if pickup_neighborhood != -1:
            if 6 < pickup_time < 11: # 7:00 to 10:59
                agg[pickup_neighborhood] = agg.get(pickup_neighborhood, 0) + 1

    for item in agg.iteritems():
        print '%s\t%s' % (neighborhoods[item[0]][0], item[1])

if __name__ == '__main__':
    mapper()
