#!/usr/bin/python2

#step 1 : 
# (assume vg already exists)
#lv partition 2 GB


print "content-type: text/html"
print




import commands 
import getpass
import cgi



#serverIp=raw_input("Enter ip , where u want to setup nfs : ")
#serverPass=getpass.getpass("Enter server root  password : ")

serverIp=cgi.FormContent()['serverip'][0]
serverPass=cgi.FormContent()['serverpass'][0]


vgStatus=commands.getstatusoutput("sshpass -p  {0} ssh -o stricthostkeychecking=no -l root {1}  vgdisplay  myvg".format(serverPass, serverIp))

if vgStatus[0]  != 0:
	print "vg named 'myvg' doesnot exists, first create it manually"
	exit()
else:
	print "myvg vg is there .."

#userName=raw_input("Enter user name : ")
#partSize=raw_input("Enter part size in GB : ")

userName=cgi.FormContent()['username'][0]
partSize=cgi.FormContent()['partsize'][0]


commands.getoutput("sshpass -p  {3} ssh -o stricthostkeychecking=no -l root {0} lvcreate --size {1}G  --name {2}-lv1  myvg ".format(serverIp,partSize,userName,serverPass))


#step 2:
#format ext4

commands.getoutput("sshpass -p  {1} ssh -o stricthostkeychecking=no -l root {0}  mkfs.ext4  /dev/myvg/{2}-lv1".format(serverIp,serverPass,userName))

#step 3:
#mount  folder  /share


commands.getoutput("sshpass -p  {1} ssh -o stricthostkeychecking=no -l root {0}  mkdir -p  /share/{2}-lv1".format(serverIp,serverPass,userName))

commands.getoutput("sshpass -p  {1} ssh -o stricthostkeychecking=no -l root {0}  mount /dev/myvg/{2}-lv1  /share/{2}-lv1".format(serverIp,serverPass,userName))


fstabString="/dev/myvg/{0}-lv1   /share/{0}-lv1  ext4 defaults 1 2".format(userName)

commands.getoutput("sshpass -p {0} scp root@{1}:/etc/fstab  /mnt/".format(serverPass,serverIp))



# dont user 'w' mode over here
fstabfh=open('/mnt/fstab' , 'a')

fstabfh.write(fstabString + "\n")

fstabfh.close()

commands.getoutput("sshpass -p  {0} scp /mnt/fstab  root@{1}:/etc/fstab".format(serverPass,serverIp))

fstabStatus=commands.getstatusoutput("sshpass -p  {0} ssh -o stricthostkeychecking=no -l root {1}  mount -a".format(serverPass,serverIp))

if fstabStatus[0] == 0:
	pass
else:
	print "there are some in fstab, plz check manually .."



#step 4:
#nfs server :  /etc/exports

"""
clientIp=raw_input("Enter clientip , want to share : ")
shareLocation="/share/{0}-lv1   {1}".format(userName,clientIp)


nfsfh=open('/etc/exports', 'a')
nfsfh.write(shareLocation + "\n")
nfsfh.close()



#step 5:


commands.getoutput("systemctl restart nfs")



"""
