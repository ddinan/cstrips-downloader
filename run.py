#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" download images """
def dwIMG(p_sID):
    sURL = URL % p_sID
    print sURL, 
    r = requests.get(sURL)
    
    if r.status_code == 200:
        f = open(p_sID + '.png','wb')
        f.write(r.content)
        f.close()
        print 'OK'
    else:
        print 'NONE'


def genIDS():
    chars = digits + uppercase
    iLast = getLAST()
    iCurrent = -1
    for sID in product(chars, repeat=5):
        iCurrent += 1

        # ignore already tested IDs
        if iCurrent < iLast:
            continue

        # save each 1000 iterations
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
