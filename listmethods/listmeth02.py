#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append("dns")# This will add "DNS" to the end of our list
protoa.append("dns")# This will add dns to the end of our list
print(proto) 
proto2 = [22, 80, 443, 53]#add a list of common ports
proto.extend(proto2)#pass proto2 as an argument to the extend method
print(proto)
protoa.append(proto2)#pass proto 2 as an argument to the append method
print(protoa)

protoa.insert(3,"ftp")#insert ftp after https
print(protoa)
