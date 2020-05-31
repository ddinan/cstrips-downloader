#!/usr/bin/env python
# -*- coding: utf-8 -*-

from string import digits, uppercase
from itertools import product
import sched, time, requests
from os import path
from progress.bar import IncrementalBar

# Change USER to your user ID and execute

URL = 'http://cstrips.bitstrips.com/%s_USER.png'
WAITTIME = 0.05

bar = IncrementalBar('Processing', max=60466176)

""" download images """
def dwIMG(p_sID):
    bar.next()

    sURL = URL % p_sID
    #print sURL,
    r = requests.get(sURL)

    if r.status_code == 200:
        f = open(p_sID + '.png','wb')
        f.write(r.content)
        f.close()
        print ' YES'
        #print ' NONE'

def genIDS():
    chars = digits + uppercase
    iLast = getLAST()
    iCurrent = -1
    for sID in product(chars, repeat=5):
        iCurrent += 1

        # Ignore already tested IDs
        if iCurrent < iLast:
            continue

        # Save each 1000 iterations
        if not iCurrent % 1000:
            savLAST(iCurrent)

        dwIMG(''.join(sID))
        time.sleep(WAITTIME)

# ----------------- recover last session
FILELAST = 'session.last'

def savLAST(p_iNum):
    f = open(FILELAST,'w')
    f.write(str(p_iNum))
    f.close()
    print "** saved session [", p_iNum, "] **"


def getLAST():
    if path.isfile(FILELAST):
        f = open(FILELAST,'r')
        iNum = int(f.read(), 10)
        print "recover from:", iNum
        f.close()
        return iNum
    else:
        print "process started..."
        return 0

if __name__ == '__main__':
    genIDS()
