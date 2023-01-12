#!/usr/bin/env python3

import paramiko
import csv

def main():
    credz = []
    with open("results.log","w") as l:
        l.write("")#Clear file
    with open("credz.txt") as bar:
        for line in csv.reader(bar):
            print(line[0],line[1].strip())
            credz.append({"un": line[0], "ip":line[1].strip()})
#    credz = [
#            {"un": "bender", "ip": "10.10.2.3"}, 
#            {"un": "zoidberg", "ip": "10.10.2.5"}, 
#            {"un": "fry", "ip": "10.10.2.4"}
#            ]
    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

    for cred in credz:

        sshsession = paramiko.SSHClient()

        sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        print("Connecting to... " + cred.get("un") + "@" + cred.get("ip"))

        sshsession.connect(hostname=cred.get("ip"), username=cred.get("un"), pkey=mykey)

        sshsession.exec_command("touch /home/" + cred.get("un") + "/goodnews.everyone")

        sessin, sessout, sesserr = sshsession.exec_command("ls /home/" + cred.get("un"))

        content=sessout.read().decode('utf-8')

        with open("results.log","a") as l:
            l.write(content)

        sshsession.close()

    with open("results.log","r") as l:
        for x in l:
            print(x)
    print("Thanks for looping with Alta3!")

if __name__=="__main__":
    main()
