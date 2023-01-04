#!/usr/bin/env python3
"""
Moves and rename files to user's request
"""
import shutil
import os

def main():
    #change directory
    os.chdir('/home/student/mycode/')
    
    #move raynor object
    shutil.move('raynor.obj','ceph_storage/')
    
    #prompts user for to rename the kerrigan object
    xname = input("What is the new name for kerrigan.obj? ")

    #renames kerrigan to user's input
    shutil.move('ceph_storage/kerrigan.obj','ceph_storage/'+xname)

#Call main function
main()
