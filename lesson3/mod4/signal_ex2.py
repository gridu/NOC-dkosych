#!/usr/bin/python3

from time import sleep
from signal import *

def isprime(n):
	sleep(0.1)
	x=2
	while (x*x) <=n:
		if not n % x:
			return False
		x += 1
	return True

debug = True

def sighup_handler(signum, frame):
	global debug
	debug = not debug

signal(SIGHUP, sighup_handler)
signal(SIGINT, SIG_IGN)
signal(SIGTERM, SIG_IGN)

n = 1
primes_list = []

while True:
	if isprime(n):
		if debug:
			print("%d is prime" % n)
		primes_list.append(n)
	n += 1
