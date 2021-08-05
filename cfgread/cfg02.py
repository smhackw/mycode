#!/usr/bin/python3
## create file object in "r"ead mode
configfile = open("vlanconfig.cfg", "r")

configblog = configfile.read()

configlist = configblog.splitlines()

print(configlist)

configfile.close()
