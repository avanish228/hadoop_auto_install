#!/usr/bin/python

import commands
import cpassw
def stop(ip):
	commands.getstatusoutput("sshpass -p "+cpassw.cpass()+"ssh {} source /root/.bashrc".format(ip))
	commands.getstatusoutput("sshpass -p "+cpassw.cpass()+"ssh {} systemctl stop firewalld".format(ip))
	commands.getstatusoutput("sshpass -p "+cpassw.cpass()+"ssh {} setenforce 0".format(ip))
