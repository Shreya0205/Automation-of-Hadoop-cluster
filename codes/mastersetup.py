#!/usr/bin/python2

import os
import commands
import cgi

print "Content-Type: text/html"
print

print "<pre>"
def softinstall(software):

	websoftware=commands.getstatusoutput("sshpass -p redhat ssh -o stricthostkeychecking=no -l root {0} 'rpm -q {1}'".format(ip,software))
	if websoftware[0]==0:
        	print software+" already installed"
	else:
       		websoftwareinstall=commands.getstatusoutput("sshpass -p redhat ssh -o stricthostkeychecking=no -l root {0} 'yum install {1} -y'".format(ip,software))
        	if websoftwareinstall[0]==0:
	       	        print "Software"+software+" installed successfully"
        	else:
        	        print "Not installed successfully"


ip="192.168.43.27"
#cgi.FormContent()['ip'][0]

softinstall("jdk")
softinstall("hadoop")

#a=commands.getstatusoutput("sshpass -p redhat ssh -o stricthostkeychecking=no -l root {0} 'mkdir /name5'".format(ip))
#print a

hdfsdata="<?xml version=\"1.0\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>dfs.data.dir</name>\n<value>/name1</value>\n</property>\n</configuration>"
hdfsfile=open('/mnt/hdfs-site.xml','w')
hdfsfile.write(hdfsdata)
hdfsfile.close()


coredata="<?xml version=\"1.0\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://"+ip+":10001</value>\n</property>\n</configuration>"
corefile=open('/mnt/core-site.xml','w')
corefile.write(coredata)
corefile.close()


b=commands.getstatusoutput("sshpass -p redhat 'scp /mnt/hdfs-site.xml root@{}:/etc/hadoop/hdfs-site.xml'".format(ip))
print b

c=commands.getstatusoutput("sshpass -p redhat 'scp /mnt/core-site.xml root@{}:/etc/hadoop/core-site.xml'".format(ip))
print c
#i=commands.getstatusoutput("rm -rf /mnt/core-site.xml /mnt/hdfs-site.xml")


#f=commands.getstatusoutput("sshpass -p redhat ssh -o stricthostkeychecking=no -l root {0} 'hadoop namenode -format -force'".format(ip))
#print f

#g=commands.getstatusoutput("sshpass -p redhat ssh -o stricthostkeychecking=no -l root {0} 'hadoop-daemon.sh start namenode'".format(ip))
#print g

#h=commands.getstatusoutput("sshpass -p redhat ssh -o stricthostkeychecking=no -l root {0} 'netstat -tnlp | grep 10001'".format(ip))
#print h

if h>"1":
	print "MasterNode Successfully Created At Port Number 10001"
else:
	print "MasterNode Not Created"

print "</pre>"
