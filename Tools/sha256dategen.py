#!/usr/bin/python
# Generates all possible outputs to stdout for cracking following the advice found here: https://www.howtogeek.com/howto/30184/10-ways-to-generate-a-random-password-from-the-command-line/
# Usage: python sha256dategen.py > file

__authors__ = ['Chick3nman']

import hashlib
import base64

#start and end times are in Epoch(UNIX) time
starttime = 1262304000
endtime = 1586796831


while starttime < endtime:
    i = str(starttime) + "\n"
    i2 = bytes(i.encode("UTF-8"))
    m = hashlib.sha256(i2).hexdigest().encode("utf-8")
    b = base64.b64encode(bytes(m[:24]))
    starttime +=1
    print(b.decode())
