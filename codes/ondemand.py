#!/usr/bin/python2


print "content-type: text/html"



import cgi
import commands
slaves = cgi.FormContent()['slaves'][0]
tasktrackers = cgi.FormContent()['tasktrackers'][0]

number=int(slaves)+int(tasktrackers)

def containerinstall(name):
			
			
		
	f=open(filename,'r')
	m=f.read().replace('\n',' ').split()
	#print m[1]
	ip=commands.getoutput("sshpass -p redhat ssh -o stricthostkeychecking=no -l root {} ' docker inspect {} | jq \".[].NetworkSettings.Networks.bridge.IPAddress\" '".format(m[1],name))
	IP=ip.strip("\"")
	#print IP
			
	f=open('/etc/ansible/hosts','r')
	p=f.read()
	f.close()
	p=p.replace(m[1],IP)
			
			
	f=open('/etc/ansible/hosts','w')
	f.write(p)
	f.close()
	p=name+"map.yml"
	print commands.getstatusoutput("sudo ansible-playbook /ansible/{}".format(p))

	return IP


	def ansiblesetup(setup):
		data="\n\n["+setup+"]\n"
		f=open("/mnt/hosts2",'a')
		f.write(data)
		f.close()


	def ansiblehosts(ID):
		print ID
		data=ID+" ansible_ssh_user=root ansible_ssh_pass=root\n"
		f=open("/mnt/hosts2",'a')
		f.write(data)
		f.close()


		


#	commands.getoutput("cat /mnt/master.txt > /etc/ansible/hosts")
	IP=containerinstall("master")
	print IP
#		ansiblesetup("master")
#		ansiblehosts(IP)


#		IP=containerinstall("jobtracker")
#		ansiblesetup("jobtracker")
#		ansiblehosts(IP)

#		i=0
#ansiblesetup("tasktracker")
#for i in range(tasktracker):
#	t="tasktracker"+str(i)
#	IP=containerinstall(t)
#	ansiblehosts(IP)
#	i=i+1

#print commands.getstatusoutput("sudo ansible-playbook /ansible/mastersetup.yml")
