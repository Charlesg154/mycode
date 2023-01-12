#!/usr/bin/env python3

import netifaces


def main():
    print(netifaces.interfaces())

    for i in netifaces.interfaces():
        print('\n**************Details of Interface - ' + i + ' *********************')
        try:
            macadr(i)
            ipadr(i)

        except:
            print("Could not collect adapter information")


def macadr(i):
    print("MAC: ",end="")
    print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])

def ipadr(i):
    print("IP: ", end="")
    print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])

if __name__=="__main__":
    main()
