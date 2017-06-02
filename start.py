#!/usr/bin/python

import commands
import cpassw

def nn(ip):
	#commands.getstatusoutput("ssh {} hdfs namenode -format".format(ip))
	commands.getstatusoutput("sshpass -p "+cpassw.cpass()+" ssh {} hadoop-daemon.sh start namenode".format(ip))

def jt(ip):
	commands.getstatusoutput("sshpass -p "+cpassw.cpass()+" ssh {} yarn-daemon.sh start resourcemanager".format(ip))

def dn(ip):
	commands.getstatusoutput("sshpass -p "+cpassw.cpass()+" ssh {} hadoop-daemon.sh start datanode".format(ip))

def tt(ip):
	commands.getstatusoutput("sshpass -p "+cpassw.cpass()+" ssh {} yarn-daemon.sh start nodemanager".format(ip))
