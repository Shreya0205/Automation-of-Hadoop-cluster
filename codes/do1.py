#!/usr/bin/python2


import commands

print "content-type: text/html"
print

print """
<script>
function Check(stat,mycname)
{

	if (stat=="Start")
		document.location='docker_start.py?x=' + mycname;
	else if (stat=="Stop")
		document.location='docker_stop.py?x=' + mycname;
	else if (stat=="Remove")
		document.location='docker_remove.py?x=' + mycname;

}
</script>
"""


print "<table>"
print "<tr><th>Image Name</th><th>ContainerName</th><th>Status</th><th>Stop</th><th>Start</th><th>Remove</th></tr>"

z=1
for i in commands.getoutput("sudo docker ps -a").split('\n'):
	if z == 1:
		z+=1
		pass
	else:
		j=i.split()
		cStatus=j[6]
		
		if cStatus=='Exited' :
			print """
<tr>
	<td>""" + j[1] + """</td>
	<td>""" + j[-1] + """</td>
	<td>Exited</td>
	<td><input name='"""+j[-1]+"""' value='Stop' type='button' onclick=Check(this.value,this.name) disabled/></td>
	<td><input name='"""+j[-1]+"""' value='Start' type='button' onclick=Check(this.value,this.name) /></td>
	<td><input name='"""+j[-1]+"""' value='Remove' type='button' onclick=Check(this.value,this.name)  /></td>
</tr>"""
		else :
			print """
<tr>
	<td>""" + j[1] + """</td>
	<td>""" + j[-1] + """</td>
	<td>Running</td>
	<td><input name='"""+j[-1]+"""' value='Stop' type='button' onclick=Check(this.value,this.name) /></td>
	<td><input name='"""+j[-1]+"""' value='Start' type='button' onclick=Check(this.value,this.name)  disabled/></td>
	<td><input name='"""+j[-1]+"""' value='Remove' type='button' onclick=Check(this.value,this.name) /></td>
</tr>"""

print "</table>"
