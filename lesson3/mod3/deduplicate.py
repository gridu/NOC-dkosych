#!/usr/bin/python3

import hashlib
import os


def gethash(file):
    hasher = hashlib.sha1()
    with open(file, "rb") as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()


hashmap = {}

for rootdir, dirs, files in os.walk("/home/student/tests"):
    for f in files:
        path = os.path.join(rootdir, f)
        if os.path.islink(path) or os.stat(path).st_size < 1024:
            continue
        hash = gethash(path)
        if hash in hashmap:
            matching = hashmap[hash]
            if os.stat(path).st_ino == os.stat(matching).st_ino:
                print("%s, %s are links to same file" % (path, matching))
                continue
            else:
                os.unlink(path)
                os.link(matching, path)
                print("%s same as %s" % (path, matching))
        else:
            hashmap[hash] = path
