#!/usr/bin/env python3
"""
dnsfile = open("dnsservers.txt","r")
dnslist = dnsfile.readlines()

for svr in dnslist:
    print(svr, end="")
dnsfile.close()
"""

"""
with open("dnsservers.txt","r") as dnsfile:
    dnslist = dnsfile.readlines()

    for svr in dnslist:
        print(svr, end="")
"""

"""
with open("dnsservers.txt","r") as dnsfile:
    for svr in dnsfile:
        print(svr, end="")
"""

#"""
with open("dnsservers.txt","r") as dnsfile:
    for svr in dnsfile:
        svr = svr.rstrip('\n')

        if svr.endswith('org'):
            with open("org-domain.txt","a") as srvfile:
                srvfile.write(svr + "\n")

        elif svr.endswith('com'):
            with open("com-domain.txt","a") as srvfile:
                srvfile.write(svr+"/n")
#"""

"""
import uuid
howmany = int(input("How many UUIDs should be generated? "))
print("Generating UUIDs...")

for rando in range(howmany):
    print(uuid.uuid4())
"""
