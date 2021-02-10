#!/usr/bin/env python
# -*- coding: utf-8 -*-

from threading import Thread
from queue import Queue
from string import digits, ascii_uppercase
from itertools import product
import sched
import time
import requests
from os import path
from progressBar import GetPatchedProgress
progress = GetPatchedProgress()
from progress.bar import IncrementalBar

while True:
    val = input("Please enter your alphanumeric ID: ")

    if val.isdigit():
        print("Your ID should be alphanumeric and not consist of only numbers. For example JH38B is correct whereas 2862743 is not.");
        continue
    elif val.isalnum():
        break

while True:
    print("Starting to scan database for ID " + val + "...")
    break

# Change USER to your user ID and execute

URL = 'http://cstrips.bitstrips.com/%s_' + val + '.png'
WAITTIME = 0.05
CONCURRENCY = 20

bar = IncrementalBar('Processing ', suffix='%(index)d/%(max)d %(percent)d%% [%(elapsed_td)s / %(eta)d / %(eta_td)s]', max=60466176)

def dwIMG(p_sID):
    sURL = URL % p_sID
    idPath = p_sID + '.png'
    if path.exists(idPath):
        return

    # print sURL,
    r = requests.get(sURL)

    if r.status_code == 200:
        f = open(idPath, 'wb')
        f.write(r.content)
        f.close()


def genIDS():
    q = Queue(CONCURRENCY * 2)

    def doWork():
        while True:
            id = q.get()
            try:
                dwIMG(id)
            except:
                print("error", id)
            q.task_done()

    for i in range(CONCURRENCY):
        t = Thread(target=doWork)
        t.daemon = True
        t.start()

    print("computing ids")
    chars = digits + ascii_uppercase
    iLast = getLAST()
    iCurrent = -1

    bar.goto(iLast)

    for sID in product(chars, repeat=5):
        iCurrent += 1

        if iCurrent < iLast:
            continue

        if not iCurrent % 1000:
            saveLAST(iCurrent)
        q.put(''.join(sID))
        bar.next()

    print("The script has scanned all possible URLs for your comics and downloaded them.")
    q.join()
    bar.finish()

# ----------------- recover last session
FILELAST = 'session.last'

def saveLAST(p_iNum):
    f = open(FILELAST,'w')
    f.write(str(p_iNum))
    f.close()


def getLAST():
    if path.isfile(FILELAST):
        f = open(FILELAST,'r')
        iNum = int(f.read(), 10)
        print("Recovering from:", iNum)
        f.close()
        return iNum
    else:
        return 0


if __name__ == '__main__':
    genIDS()
