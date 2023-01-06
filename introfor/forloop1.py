#!/usr/bin/env python3


vendors = ["cisco","juniper","big_ip","f5","arista"]

approved_vendors = ["cisco", "juniper", "big_ip"]

for x in vendors:
    print("\nThis vendor is:", x, end="")
    if x not in approved_vendors:
        print(" - NOT AN APPROVED VENDOR!", end="")

print("\nOur loop has ended.")
