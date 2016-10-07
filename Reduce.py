#!/usr/bin/env python

import sys
#Reduce

key1=None
key2=None  
nbr = 0

for input in sys.stdin:
	input = input.strip();
	key1,value = input.split("\t",1)
	value=int(value)

	if key2 == key1:
		nbr += value
	else:
		if key2:
			print( "%s\t%d" % (key2, nbr) )
		nbr = value
		key2 = key1

if key2 == key1:
     print( "%s\t%d" % (key2,nbr))
