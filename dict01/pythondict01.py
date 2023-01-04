#!/usr/bin/env python3
"""
Understanding dictionaries
{key: value, key:value, ...}
"""

def main():
    #runtime function

    #create a dictionary with 4 key:value pairs
    switch = {"hostname": "sw1",
            "ip": "10.0.1.1",
            "version": "1.2",
            "vendor": "cisco"}

    #display the entire dictionary
    print(switch)
    
    #proove that switch is indeed a dictionary
    print(type(switch))

    #display parts of the dictionary
    print(switch["hostname"])   #displays "sw1"
    print(switch["ip"])         #displays "10.0.1.1"

    #request a 'fake' key
    ##print(switch["lynx"]) #This will cause the program to fail
    print("First test - .get()")
    print(switch.get("lynx")) # alternative to switch["lynx"]
    #print(switch.get("lynx", None)) This is the default of get.  None is being used as our error message

    #Customizing the error message
    print("Second test - .get()")
    print(switch.get("lynx"),"Sorry Mario!  This key is another castle!")

    print("Third test - .get()")
    print(switch.get("version"))#Alternative to switch['version'].  It exists, so it'll return the value.

    #This returns all of the keys in the dictionary
    print("Fourth test - .keys()")
    print(switch.keys()) #dict.keys() returns all of the keys as a list like string

    #return all of the values in the dictionary
    print("Fifth test - .values()")
    print(switch.values()) #dict.values() returns all of the values as a list like string


    #remove a value from our dictionary using del
    del switch["vendor"] #This just removes key/value pair and returns nothing
    #del switch["pizza"] ## if you try to delete a key that does not exist it will return an error

    #remove a value via pop method
    print("Seventh test - .pop()")
    print(switch.pop("version"))#removes the key and also return the value "1.2"
    print(switch.keys()) #Notice the value of version is gone
    print(switch.values()) # notice the value of 1.2

    #add a value to the dictionary
    print("Eigth test - ADD a new value")
    switch["adminlogin"] = "karl08"
    print(switch.keys())
    print(switch.values())

    #Add another value to the dictionary
    print("Ninth test - ADD a new value")
    switch["password"] = "qwerty"
    print(switch.keys())
    print(switch.values())

    #Select a value from the results.  We must conver this list like structure into an actual list using list()
    print(list(switch.values())[2])## this selects the 2nd position (3rd item) from the list


#Call our main function
if __name__ == "__main__":
    main()
