#!/usr/bin/python2


print "content-type: text/html"
print


import cgi
import commands



masterip='192.168.43.182'#cgi.FormContent()['masterIP'][0]
tasktracker='2'#cgi.FormContent()['tasktracker'][0]

i=0
jobtrackerIP=''
while i < tasktracker:
	
	f=open('/webcontent/ansible/ondemandcluster','r')
	lines=f.readlines()
	f.close()
	
	x=lines[1]
	p=x.split()
	#print m[1]

	data="---\n- hosts: linux\n  tasks:\n  - docker_container:\n       name: 'ondemandcluster"+str(i)+"'\n       image: 'cluster:v1'\n       state: started\n       tty: true\n       interactive: true\n       detach: true\n       privileged: true"

	print commands.getstatusoutput("echo {} > /ansible/containersetup.yml".format(data))
          
	print commands.getstatusoutput("sudo ansible-playbook -i /webcontent/ansible/ondemandcluster /ansible/containersetupmap.yml")
	
	ip=commands.getoutput("sshpass -p redhat ssh -o stricthostkeychecking=no -l root {0} ' docker inspect ondemandcluster{1} | jq \".[].NetworkSettings.Networks.bridge.IPAddress\" '".format(p[0],i))
	IPa=ip.strip("\"")

	
	if i==0:
		data=IPa+"ansible_ssh_user=root ansible_ssh_pass=redhat\n[tasktracker]\n"
		global jobtrackerIP
		jobtrackerIP=IPa
	else:
		data=IPa+"ansible_ssh_user=root ansible_ssh_pass=redhat\n"

	fh=open('/webcontent/ansible/ondemandclusterfinal','a')
	fh.write(data)
	f.close()
	i=i+1


coredata="""
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://"""+masterIP+""":10001</value>
</property>
</configuration>
"""
f=open('/webcontent/xml/ondemandmapcore-site.xml','w')
f.write(coredata)
f.close()
#print commands.getstatusoutput(" sudo echo -e  > /webcontent/xml/core-site.xml".format(coredata))

mapreddata="""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>

<property>
<name>mapred.job.tracker</name>
<value>"""+jobtrackerIP+""":9001</value>
</property>
</configuration>"""
f=open('/webcontent/xml/ondemandmapred-site.xml','w')
f.write(mapreddata)
f.close()

#print commands.getstatusoutput(" echo {0} > /mnt/mapred-site.xml".format(mapreddata))

#hdfsdata="""<?xml version="1.0"?>
#<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
#<!-- Put site-specific property overrides in this file. -->
#<configuration>
#<property>
#<name>dfs.name.dir</name>
#<value>/clusterdir</value>
#</property>
#</configuration>
#"""
#print hdfsdata
#f=open('/webcontent/xml/hdfs-site.xml','w')
#f.write(hdfsdata)
#f.close()

print commands.getstatusoutput("sudo ansible-playbook -i /webcontent/ansible/manualmapclusterfinal /ansible/mapreduceondemand.yml")
