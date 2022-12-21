#!/usr/bin/env python3

def main():


    # collect string input from the user
    user_input = input("\nPlease enter an IPv4 IP address: ")

    ## the line below creates a single string that is passed to print()
    # print("You told me the IPv4 address is: " + user_input)
    
    ## print() can be given a series of objects separated by a comma
    print("\nYou told me the IPv4 address is:", user_input)


    #Asks for vendor names and then prints it
    vendor = input("\nWhat is the vendor name associated with this device? ")
    print("\nThe vendor is " + vendor, "\n")

main()
