#!/bin/python

import numpy as np
import math

length = 256
deviation_f = 2500


def print_sintable(deviation_f):
    f_resolution = 7.805347443
    deviation = (deviation_f/f_resolution)

    # Generate our sin table
    quadrant_range = np.arange(0, np.pi/2, (np.pi/2)/length)
    sintable = np.multiply(np.sin(quadrant_range), deviation)

    # stringify
    strings = [ "{0:0.0f}".format(x) for x in sintable ]
    maxlen =  max([ len(s) for s in strings ])

    # stringify in equal parts
    strings = [ "{0:>{width}.0f}".format(x, width=maxlen) for x in sintable ]
    string = ", ".join(strings)

    # lines
    line_len = int(math.floor(78 / (maxlen+2))*(maxlen+2))
    lines = [string[x:x+line_len].rstrip() for x in range(0, len(string), line_len)]
    string = "\n  ".join(lines)

    print "/**"
    print " * 1st quadrant sin lookup table for {0:0.1f}kHz deviation".format(deviation_f/1000.0)
    print " *"
    print " * Length: {0}".format(length)
    print " * Frequency Resolution: {0:0.3f} Hz".format(f_resolution)
    print " */"
    print "uint16_t sintable_{0}_{1}hz[] = {{".format(length, deviation_f)
    print "  "+string
    print "};"
    print



print "/**"
print " * Autogenerated sine tables. See tools/ax25_lookup/ax25_lookup.py"
print " */"
print

print "#ifndef AX25_SINTABLE_H"
print "#define AX25_SINTABLE_H"
print
print

print "#define AX25_SINTABLE_ORDER {0:d}".format(int(math.log(length, 2)))
print "#define AX25_SINTABLE_LENGTH {0:d}".format(length)
print
print

print_sintable(1600)
print_sintable(2500)

print "#endif /* AX25_SINTABLE_H */"