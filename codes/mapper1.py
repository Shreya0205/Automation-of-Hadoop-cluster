#!/usr/bin/python2


import re
import sys
for x in sys.stdin:
	 y=x.split(':')
         if re.search('Animation',y[2]):
		top=str(y[3])
		if top >= '4' and top <= '5':
			print str(y[1]) +"->Animation->"+  str(y[3])

	 else:
		pass
