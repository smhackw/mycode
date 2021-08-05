#!/usr/bin/env python3
# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
# open the file for reading
keystone_file = open("/home/student/mycode/attemptedlogin/keystone.common.wsgi","r")

keystone_file_lines=keystone_file.readlines()

for line in keystone_file_lines:

    if "- - - - -] Authorization failed" in line:
        loginfail += 1
print("the number of failed attempts is", loginfail)
keystone_file.close()
