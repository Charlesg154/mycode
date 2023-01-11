#!/usr/bin/env python3

import paramiko
import os
import getpass

def main():

    t = paramiko.Transport("10.10.2.3", 22)
    
    t.connect(username="bender", password=getpass.getpass())

    sftp = paramiko.SFTPClient.from_transport(t)

    sftp.put("file_to_move.txt","file_to_move.txt")

    sftp.close()



if __name__=="__main__":
    main()
