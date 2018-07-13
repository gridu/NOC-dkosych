#!/usr/bin/python3
#no systemd on local machine#no systemd on local machine#no systemd on local machine
import logging
from systemd.journal import JournalHandler

logging.basicConfig(filename="example.log", level=logging.WARM, format="%(levelname)s %(asctime)s %(message)s")

logging.warning("this is a formatted warning")

jlogger = logging.getLogger("journal-logger")
jhandler = JournalHandler()
jformatter = logging.Formatter(fmt="%(levelname)s %(message)s")
jhandler.setFormatter(jformatter)

jlogger.addHandler(jhandler)
jlogger.warning("This is a warning sent to the journal")

jlogger.propagate = False
jlogger.warning("Warning ONLY to journal")

def bad_idea():
	try:
		c=1/0
	except:
		logging.error("Failed to divide", exc_info=True)

bad_idea()
