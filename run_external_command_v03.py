#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 12:02:16 2019

@author: clemente
"""
#import subprocess
#subprocess.call(["ping", "-c 3", "www.cyberciti.biz"])

#os.chdir('/home/clemente/test')
#cmd = "./test.sh"
#os.system(cmd)

import os
from tkinter import *
import netifaces as ni #import this to get ip from NIC

# FUNCTIONS

def fcmd1():
    var_arg1=e1.get()
    var_arg2=e2.get()
    var_arg3=e3.get()
    os.chdir(r"C:\usr\bin")
   #var_cmd = "./test.sh"
    var_cmd = "snmptrap.exe"
    
    os.system(var_cmd)
   #os.system("snmptrap -v 2c -c public localhost '' 1.3.6.1.4.1.8072.2.3.0.1 1.3.6.1.4.1.8072.2.3.2.1 s TestTRAP")
    os.system("%s -v 2c -c %s %s '' 1.3.6.1.4.1.8072.2.3.0.1 1.3.6.1.4.1.8072.2.3.2.1 s %s" % (var_cmd,var_arg1,var_arg2,var_arg3))
# get IP from NIC


ni.ifaddresses('wlp4s0')
ip = ni.ifaddresses('wlp4s0')[ni.AF_INET][0]['addr']

master = Tk()

var_arg1=Label(master, text="Community:         ", font=("dosis", '11'), bg='gray', fg='white')
var_arg1.place(x=180,y=22)
var_arg2=Label(master, text="Destination Host: ", font=("dosis", '11'), bg='gray', fg='white')
var_arg2.place(x=150,y=42)
var_arg3=Label(master, text="Message:", font=("dosis", '11'), bg='gray', fg='white')
var_arg3.place(x=196,y=62)

Label(master, text="Simulated TRAP:\nsnmptrap -v 2c -c <community> <Destination Host> '' 1.3.6.1.4.1.8072.2.3.0.1 1.3.6.1.4.1.8072.2.3.2.1 s <message>", font=("dosis", '9'), bg='gray',fg='#475057').place(x=20, y=150)
Label(master, text="source IP: %s" % (ip), font=("dosis", '9'),  bg='gray').grid(row=1) # show local IP in window master


master.geometry("660x200")
master.title("TRAP Simulator")
master.configure(bg='gray')


e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)

e1.grid(row=0, column=2)
e2.grid(row=1, column=2)
e1.place(x=270,y=22)
e2.place(x=270,y=42)
e3.place(x=270,y=62)

B1 = Button(master, text ="send", font=("dosis", '10'), highlightbackground='#190707', command = fcmd1, bg='#333333', fg='white',height=3, width=3)
B1.place(x=400, y=22)

           
mainloop( )