#!/usr/bin/env python
# task 2a
import sys

for line in sys.stdin:
    line = line.strip('\r\n')
    values = line.split(',')
    if values[18] == 'total_amount':
        continue
    fare = float(values[18])
    if 0 <= fare <= 4:
        print 'a\t1'

    elif 4.01 <= fare <= 8:
        print 'b\t1'

    elif 8.01 <= fare <= 12:
        print 'c\t1'

    elif 12.01 <= fare <= 16:
        print 'd\t1'

    elif 16.01 <= fare <= 20:
        print 'e\t1'

    elif 20.01 <= fare <= 24:
        print 'f\t1'

    elif 24.01 <= fare <= 28:
        print 'g\t1'

    elif 28.01 <= fare <= 32:
        print 'h\t1'

    elif 32.01 <= fare <= 36:
        print 'i\t1'

    elif 36.01 <= fare <= 40:
        print 'j\t1'

    elif 40.01 <= fare <= 44:
        print 'k\t1'

    elif 44.01 <= fare <= 48:
        print 'l\t1'

    elif fare >= 48.01:
        print 'm\t1'
"""
[0,4], a
[4.01,8], b
[8.01,12], c
[12.01, 16], d
[16.01, 20], e
[20.01, 24], f
[24.01, 28], g
[28.01, 32], h
[32.01, 36], i
[36.01, 40], j
[40.01, 44], k
[44.01, 48], l
[48.01, infinite], m
"""
