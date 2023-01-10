#!/usr/bin/env python3
import requests

NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

def returncreds():
    with open("/home/student/mycode/nasa/nasa.creds") as mycreds:
        nasacreds = mycreds.read()
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

def main():
    nasacreds = returncreds()
    startdate = "start_date=2019-11-11"
    
    neowrequest = requests.get(NEOURL + startdate + "&" + nasacreds)
    
    neodata = neowrequest.json()
    
    print(neodata)

if __name__ == "__main__":
    main()
