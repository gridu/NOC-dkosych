#!/usr/bin/python3

import sys

version = 2

if version == 1:
	def revline(line):
		outline = ""
		index = len(line)
		while index:
			index -= 1
			outline += line[index]
		print(outline, end='')

if version == 2:
	def revline(line):
		if line:
			revline(line[1:])
			print(line[0], end='')

if version == 3:
	def revline(line):
		print(line[::-1], end='')

def process_file (f):
	for line in f:
		revline(line)

if (len(sys.argv)) == 1:
	process_file(sys.stdin)
else:
	for path in sys.argv[1:]:
		print("One")
		try:
			file = open(path, "r")
		except Exception as e:
			print("Catch  %s" % e, file=sys.stderr)
			continue
		process_file(file)
		file.close()

