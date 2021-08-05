#!/usr/bin/python3
######### EXPLORE READ #########
## create file object in "r"ead mode
configfile = open("vlanconfig.cfg", "r")

print(configfile.read())

configfile.close()

configfile = open("vlanconfig.cfg", "r")

configlist = configfile.readlines()
print(configlist)

for x in configlist:
    print(x.strip())

configfile.close()
