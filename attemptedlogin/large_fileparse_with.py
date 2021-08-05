#!/usr/bin/python3

loginfail = 0

with open("/home/student/mycode/attemptedlogin/keystone.common.wsgi") as kfile:

    for line in kfile:

        if "- - - - -] Authorization failed" in line:
            loginfail += 1

print("the number of attempts is", loginfail)
