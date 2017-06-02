#!/usr/bin/python
import commands
import os
import cpassw


#hadoop 1 installation
def hadoop_1install(ip):
     print "coppying hadoop software to client"
     commands.getstatusoutput("sshpass -p "+cpassw.cpass()+" scp hadoop-1.2.1-1.x86_64.rpm root@{}:".format(ip))
     print "installing hadoop on client system"
     commands.getstatusoutput("sshpass -p "+cpassw.cpass()+" ssh {} rpm -ivh hadoop-1.2.1-1.x86_64.rpm --replacefiles".format(ip))
          
     
     #p=commands.getstatusoutput("ssh {} hadoop -version".format(ip))
     #print p[1]
     #ad=commands.getstatusoutput("ssh 192.168.43.51 /usr/java/jdk1.7.0_79/bin/jps")
     #print ad[1]

def dialog():
	y=commands.getstatusoutput("yum install dialog-1.2-4.20130523.el7.x86_64.rpm -y")
	if y[0]==0 :
		print "dialog successfully installed"
	else :
		print "dialog not able to install"

def sshpass():
	y=commands.getstatusoutput("yum install sshpass-1.05-5.el7.x86_64.rpm -y")
	if y[0]==0 :
		print "sshpass successfully installed"
	else :
		print "sshpass not able to install"




def jdk_install(ip):
    os.system("dialog --infobox 'coppying jdk software to client '  10 30 ")
    print "sshpass -p "+cpassw.cpass()+" scp jdk-7u79-linux-x64.rpm root@{}:".format(ip)
    os.system("sshpass -p "+cpassw.cpass()+" scp jdk-7u79-linux-x64.rpm root@{}:".format(ip))
    os.system("dialog --infobox 'installing jdk on client system '  10 30 ")
    os.system("sshpass -p "+cpassw.cpass()+" ssh {} yum install jdk-7u79-linux-x64.rpm -y".format(ip))
    



def hadoop_2install(ip):
#     print "hello"
     os.system("dialog --infobox 'coppying and installing hadoop software to client '  10 30 ")

     os.system("sshpass -p "+cpassw.cpass()+" scp hadoop-2.6.4.tar.gz root@{}:".format(ip))
     os.system("sshpass -p "+cpassw.cpass()+" ssh {} tar -xvzf hadoop-2.6.4.tar.gz".format(ip))
     os.system("sshpass -p "+cpassw.cpass()+" ssh {} mv hadoop-2.6.4 /hadoop2".format(ip))

     commands.getstatusoutput("sshpass -p "+cpassw.cpass()+" scp  .bashrc root@{}:/root/".format(ip))
     commands.getstatusoutput("sshpass -p "+cpassw.cpass()+" scp -r startbash.py root@{}:".format(ip))
     commands.getstatusoutput("sshpass -p "+cpassw.cpass()+" ssh {} python startbash.py".format(ip))

