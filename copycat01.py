#!/usr/bin/env python3
"""
The following will create the directory if it does not exist already
"""

#import additional code to complete our task
import shutil
import os

def main():
    #move into the working directory
    os.chdir("/home/student/mycode/")
    
    #copy the fileA to fileB
    shutil.copy("5g_research/sdn_network.txt","5g_research/sdn_network.txt.copy")
    
    os.system("rm -rf /home/student/mycode/5g_research_backup/")#Seemingly removing previous backup before copying

    #copy the entire directoryA to directoryB
    shutil.copytree("5g_research/","5g_research_backup/")

#Execute main function
if __name__ == "__main__":#Couldn't tell you to be honest
    main()
