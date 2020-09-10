#!/usr/bin/python2

import cgi
import commands

print "content-type: text/html"
print

ccmd=cgi.FormContent()['code'][0]


print commands.getstatusoutput("sudo docker exec centos_dh {0}".format(ccmd))








