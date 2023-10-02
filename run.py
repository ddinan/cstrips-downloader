#!/usr/bin/env python
# -*- coding: utf-8 -*-

from threading import Thread
from queue import Queue
from string import digits, ascii_uppercase
from itertools import product
import time
import requests
from os import path
from tqdm import tqdm

while True:
    val = input("Please enter your alphanumeric ID: ")

    if val.isdigit():
        print("Your ID should be alphanumeric and not consist of only numbers. For example JH38B is correct whereas 2862743 is not.")
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

def dwIMG(p_sID):
    sURL = URL % p_sID
    idPath = p_sID + '.png'
    if path.exists(idPath):
        return

    r = requests.get(sURL)

    if r.status_code == 200:
        with open(idPath, 'wb') as f:
            f.write(r.content)

def genIDS():
    q = Queue(CONCURRENCY * 2)

    def doWork():
        while True:
            id = q.get()
            try:
                dwIMG(id)
            except Exception as e:
                print(f"error {id}: {e}")
            q.task_done()

    for i in range(CONCURRENCY):
        t = Thread(target=doWork)
        t.daemon = True
        t.start()

    print("computing ids")
    chars = digits + ascii_uppercase
    iLast = getLAST()
    iCurrent = -1

    with tqdm(total=60466176, initial=iLast, position=0, leave=True) as pbar:
        for sID in product(chars, repeat=5):
            iCurrent += 1

            if iCurrent < iLast:
                continue

            if not iCurrent % 1000:
                saveLAST(iCurrent)
            q.put(''.join(sID))
            pbar.update()

    print("The script has scanned all possible URLs for your comics and downloaded them.")
    q.join()

# ----------------- recover last session
FILELAST = 'session.last'

def saveLAST(p_iNum):
    with open(FILELAST,'w') as f:
        f.write(str(p_iNum))

def getLAST():
    if path.isfile(FILELAST):
        with open(FILELAST,'r') as f:
            iNum = int(f.read(), 10)
            print("Recovering from:", iNum)
            return iNum
    else:
        return 0

if __name__ == '__main__':
    genIDS()
