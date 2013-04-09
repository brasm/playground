#!/usr/bin/env python2
import zipfile
zf = zipfile.ZipFile('data/channel.zip')
cl = []

for f in zf.filelist:
    c = f.comment
    if c is not " ":
        cl.append(c)

print cl

