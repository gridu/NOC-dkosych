#!/usr/bin/python3

import os
import tarfile
import time

os.chdir("/home/student/extract")

mintime = time.time() - (7 * 24 * 3600)

with tarfile.open("/tmp/test3.tar", "r") as t:
	for info in t:
		if info.mtime > mintime and info.isfile():
			print("extrsacting %s" % info.name)
			t.extract(info)
