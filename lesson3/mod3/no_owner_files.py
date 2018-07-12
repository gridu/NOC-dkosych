#!/usr/bin/python3

import pwd
import os

uidset = set()
for user in pwd.getpwall():
    uidset.add(user.pw_uid)

testdir = "/home/student/tests"
for folder, dirs, files in os.walk(testdir):
    for file in files:
        path = folder + "/" + file
        try:
            attributes = os.stat(path)
        except FileNotFoundError:
            print(path + " not found")
            continue
        if attributes.st_uid not in uidset:
            print(path + " has no owner")
