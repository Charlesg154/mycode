#!/usr/bin/env python3
import urllib.request as req
import json

NASAAPI = "https://api.nasa.gov/planetary/apod?"

def main():
    with open("/home/student/mycode/nasa/nasa.creds") as mycreds:
        mycreds= mycreds.read()

    nasacreds = "api_key=" + mycreds.strip("\n")

    apodurlobj = req.urlopen(NASAAPI + nasacreds)
    
    apodread = apodurlobj.read()
    
    apod = json.loads(apodread.decode("utf-8"))
    
    print("\n\nConverted Python data")
    print(apod)
    
    print()
    
    print(apod["title"] + "\n")

    print(apod["date"] + "\n")

    print(apod["explanation"] + "\n")

    print(apod["url"])

if __name__ == "__main__":
    main()
