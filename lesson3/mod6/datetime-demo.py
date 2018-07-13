#!/usr/bin/python3

from datetime import datetime, timedelta
import os

rootinfo = os.stat("/")
rootmodtime = datetime.fromtimestamp(rootinfo.st_mtime)
print(rootmodtime)


rightnow = datetime.now()
print(rightnow)

since = rightnow - rootmodtime

print("'/' was modified {} days, {} hours and {} minutes ago".format(since.days, since.seconds//3600, (since.seconds%3600)//60))

import time

since = int(time.time() - rootinfo.st_mtime)
days = since//86400
hours = (since - days*86400) // 3600
mins = (since - (hours*3600) - (days * 86400)) // 60

print("'/' was modified {} days, {} hours and {} minutes ago".format(days, hours, mins))

fortnight = timedelta(days=14)
dueback = rightnow + fortnight

print("Your book is due back on {0:%d} of {0:%B}".format(dueback))
