#!/usr/bin/python3

import sys

def process_file (f):
	for line in f:
		if target in line:
			print(line, end='')

if (len(sys.argv)) == 1:
	print("usage: %s string [file...]" % sys.argv[0], file=sys.stderr)
	exit(1)	

target = sys.argv[1]
if len(sys.argv) == 2:
	process_file(sys.stdin)
else:
	for path in sys.argv[2:]:
		print("One")
		try:
			file = open(path, "r")
		except Exception as e:
			print("Catch  %s" % e, file=sys.stderr)
			continue
		process_file(file)
		close(file)

