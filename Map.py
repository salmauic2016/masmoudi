#!/usr/bin/env python 

import sys
#Map

for line in sys.stdin:
        line = line.strip()
	keys = line.split()
	for key in keys:
		val = 1
		print( "%s\t%d" % (key,val) )
