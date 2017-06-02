# hadoop_auto_install
this script will help you to install hadoop over large cluster
prerequsites for the working of script are
1:- Red hat or cent os linux (minimum 4 1- client 1-jobtraker 1- namenode 1-(datanode and tasktracker)
2:- install dialod and nmap from given link
3 :- download all files from given link
https://drive.google.com/open?id=0B_4MFrhoOJPkWjFBNi1JMS00ZTg
un zip it and the copy the entire code in the obtained folder by unziping the above link

now copy entire folder with the name my_project (which containes all files and softwares )
open the directory
the first file to be run is project_99.py

run it by typing   python project_99.py
username hadoop
password redhat
comman password (please have common password for all the node system )

note :-
please make sure that namp and dialog is previously installed before running the script
to install 
for nmap  
1: open directory open terminal in my_project directory 
then type      yum install nmap-6.40-7.el7.x86_64.rpm
for dialog
1: open directory open terminal in my_project directory 
then type yum install dialog-1.2-4.20130523.el7.x86_64.rpm
