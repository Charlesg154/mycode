#!/usr/bin/env python3

import csv

def main():
    option=0
    try:
        option=int(input("Option 1: \nOption 2: \nWould you like to (1 or 2)\n>"))
        if option not in range(1,3):#or you could say if option not in [1,2]
            print("input '1' or '2'")
            main()

    except Exception as err:
        print(err)
        main()

    if option == 1:
        outFile = open("admin.rc", "a")
        osAUTH = input("What is the OS_AUTH_URL? ")
        print("export OS_AUTH_URL=" + osAUTH, file=outFile)

        print("export OS_IDENTITY_API_VERSION=3", file=outFile)

        osPROJ = input("What is the OS_PROJECT_NAME? ")
        print("export OS_PROJECT_NAME=" + osPROJ, file=outFile)

        osPROJDOM = input("What is the OS_PROJECT_DOMAIN_NAME? ")
        print("export OS_PROJECT_DOMAIN_NAME=" + osPROJDOM, file=outFile)

        osUSER = input("What is the OS_USERNAME? ")
        print("export OS_USERNAME=" + osUSER, file=outFile)

        osUSERDOM = input("What is the OS_USER_DOMAIN_NAME? ")
        print("export OS_USER_DOMAIN_NAME=" + osUSERDOM, file=outFile)

        osPASS = input("What is the OS_PASSWORD? ")
        print("export OS_PASSWORD=" + osPASS, file=outFile)
        outFile.close()

    elif option == 2:
        with open("csv_users.txt","r") as csvfile:
            i=0
            for row in csv.reader(csvfile):
                i+=1
                filename = f"admin.rc{i}"

                with open(filename, "w") as rcfile:

                    print("export OS_AUTH_URL=" + row[0], file=rcfile)
                    print("export OS_IDENTITY_API_VERSION=3", file=rcfile)
                    print("export OS_PROJECT_NAME=" + row[1], file=rcfile)
                    print("export OS_PROJECT_DOMAIN_NAME=" + row[2], file=rcfile)
                    print("export OS_USERNAME=" + row[3], file=rcfile)
                    print("export OS_USER_DOMAIN_NAME=" + row[4], file=rcfile)
                    print("export OS_PASSWORD=" + row[5], file=rcfile)
        print("admin.rc files created!")


"""
def function1():

def function2():
"""
main()
