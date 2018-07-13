#!/usr/bin/python3

import re
from subprocess import Popen, PIPE

regex = re.compile(r"(/dev/sd[ab][1-9])(.*)")

outfile = open("fstab.out", mode="w")

for line in open("fstab.in"):
	match = re.search(regex,line)
	if match:
		print("Need to replace %s" % (match.group(1)))
		lsblk = Popen(["lsblk", "-n", "--output", "UUID", match.group(1)], stdout=PIPE)
		uuid = lsblk.stdout.readline().decode()
		replacement = "UUID=" + uuid[:-1] + re.sub(regex, r"\2", line)
		print("replacement line is %s" % replacement)
		print(replacement, end='', file=outfile)
	else:
		print(line, end='', file=outfile)

outfile.close()
