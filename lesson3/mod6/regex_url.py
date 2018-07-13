#!/usr/bin/python3

import re
urls = "http://docs.oldplace.com/index/1 https://oldplace.com/ http://oldplace.com/static/one.png"

regex = r"(https?)://(\w+)\.oldplace\.com/(\S+)"
newurls = re.sub(regex, r"\1://\2.newplace.org/\3", urls)
print((re.findall(regex, urls)))
print(newurls)
