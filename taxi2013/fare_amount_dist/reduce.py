#!/usr/bin/env python
# task 2a
import sys

current_key = None
map_dict = {'a': '0,4',
            'b': '4.01,8',
            'c': '8.01,12',
            'd': '12.01,16',
            'e': '16.01,20',
            'f': '20.01,24',
            'g': '24.01,28',
            'h': '28.01,32',
            'i': '32.01,36',
            'j': '36.01,40',
            'k': '40.01,44',
            'l': '44.01,48',
            'm': '48.01,infinite'}

for line in sys.stdin:
    line = line.strip('\n').split('\t')
    key = line[0]
    if current_key is None:
        current_key = key
        count = 1
    elif current_key == key:
        count += 1
    else:
        print '{0}\t{1}'.format(map_dict[current_key], count)
        current_key = key
        count = 1

print '{0}\t{1}'.format(map_dict[current_key], count)
