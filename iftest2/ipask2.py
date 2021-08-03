#!/usr/bin/env python3
ipchk = input("apply an IP: ")

if ipchk == "192.168.70.1":
    print("looks like the IP address of the Gateway was set: " + ipchk + " This is not recommended.")
elif ipchk:
    print("looks like the IP was set: " + ipchk)
else: 
    print("you did not provide input.")
