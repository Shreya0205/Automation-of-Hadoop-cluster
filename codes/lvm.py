#!/usr/bin/python2

import commands
import cgi

print "content-type: text/html"
print 


lvContent = cgi.FormContent()

lvName = lvContent['lvName'][0]
lvSize = lvContent['lvSize'][0]
#lvName = raw_input("Enter LV Name : ")
#lvSize = raw_input("Enter LV Size : ")

with open('lvm_demo.yml', 'r') as file1 :
	filedata = file1.read()
filedata = filedata.replace('lvName',lvName)
filedata = filedata.replace('lvSize',lvSize)
with open('lvm.yml', 'w') as file1:
	file1.write(filedata)
	file1.close();

print commands.getstatusoutput("sudo ansible-playbook lvm.yml")
commands.getstatusoutput("rm lvm.yml")

