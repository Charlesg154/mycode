#!/usr/bin/env python3
#EPOCH Time.  Jan 1, 1970.  Date UNIX came online.

import requests
import datetime

URL = "http://api.open-notify.org/iss-now.json"

def main():
    pull = requests.get(URL)
    data = pull.json()
    print(f"""
CURRENT LOCATION OF THE ISS:
Timestamp: {datetime.datetime.frometimestamp(data['timestamp'])}
Lon: {data[iss_position]['longitude']}
Lat: {data[iss_position]['lattitude']}
    """)

if __name__ == "__main__":
    main()
