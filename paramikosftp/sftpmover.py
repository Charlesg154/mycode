#!/usr/bin/env python3

import paramiko
import os

t = paramiko.Transport("10.10.2.3", 22)

t.connect(username="bender", password="alta3")

sftp = paramiko.SFTPClient.from_transport(t)

def movethemfiles(sftp):
    d=input("Where would you like to move your files?")
    try:
        for x in os.listdir("/home/student/filestocopy/"):
            if not os.path.isdir("/home/student/filestocopy/"+x):

                sftp.put("/home/student/filestocopy/"+x, "{d.rstrip('/')}/{x}")
                #sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x+"_cg")
    except Exception as err:
        print("An error occured", err)
    sftp.close()

movethemfiles(sftp)

t.close()

