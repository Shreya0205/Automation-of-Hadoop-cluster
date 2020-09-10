#!/usr/bin/python2

print "content-type:text/html"
print


import cgi 
import commands

cat=cgi.FormContent()['n1'][0]
rating=cgi.FormContent()['n2'][0]

if rating=='top':
	
	data="""#!/usr/bin/python2


import re
import sys
for x in sys.stdin:
	 y=x.split(':')
         if re.search('"""+cat+"""',y[2]):
		top=str(y[3])
		if top >= '4' and top <= '5':
			print str(y[1]) +\"->"""+cat+"""->\"+  str(y[3])\n
	 else:
		pass
"""
elif rating=='mod':
	
	data="""#!/usr/bin/python2


import re
import sys
for x in sys.stdin:
	 y=x.split(':')
         if re.search('"""+cat+"""',y[2]):
		top=str(y[3])
		if top > '3' and top < '4':
			print str(y[1]) +\"->"""+cat+"""->\"+  str(y[3])\n
	 else:
		pass
"""
else:
	
	data="""#!/usr/bin/python2


import re
import sys
for x in sys.stdin:
	 y=x.split(':')
         if re.search('"""+cat+"""',y[2]):
		top=str(y[3])
		if top >= '1' and top <= '3':
			print str(y[1]) +\"->"""+cat+"""->\"+  str(y[3])\n
	 else:
		pass
"""

#print commands.getstatusoutput('sudo echo {0} > /webcontent/scripts/mapper1.py'.format(data))
f=open('/webcontent/scripts/mapper1.py','w')
f.write(data)
f.close()
print "hello"
