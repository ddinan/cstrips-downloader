#!/usr/bin/env python
# -*- coding: utf-8 -*-

from threading import Thread
from Queue import Queue
from string import digits, uppercase
from itertools import product
import sched
import time
import requests
from os import path
from progress.bar import IncrementalBar

# Change USER to your user ID and execute

URL = 'http://cstrips.bitstrips.com/%s_USER.png'
WAITTIME = 0.05
CONCURRENCY = 20

bar = IncrementalBar('Processing', max=60466176)

""" download images """


def dwIMG(p_sID):
    sURL = URL % p_sID
    idPath = p_sID + '.png'
    if path.exists(idPath):
        print(idPath, "already exists, skipping")
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
    chars = digits + uppercase
    for sID in product(chars, repeat=5):
        q.put(''.join(sID))
        bar.next()

    print("done computing")

    q.join()


if __name__ == '__main__':
    genIDS()
