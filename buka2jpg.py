#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging, inspect, json, argparse
import os, sys

VERSION = 0
PATCHLEVEL = 9
SUBLEVEL = 0

def dbg(msg):
    if inspect.stack()[1][3] in dbg_target :
        log.debug(msg)

def argv_gen():
    global args
    parser = argparse.ArgumentParser(description='Extract JPG from the buka file')
    parser.add_argument('-f', '--file', type=str, action="store", dest="flist", default="", help='extract jpg from the specific file')
    parser.add_argument('-v', '--version', action='version', version='buka2jpg %d.%d.%d' % (VERSION, PATCHLEVEL, SUBLEVEL))
    args = parser.parse_args()

if __name__ == "__main__" :
    dbg_target = ['<module>']
    DEBUG = 0
    if DEBUG == 1 :
        logging.basicConfig(level=logging.DEBUG)
    else :
        logging.basicConfig(level=logging.ERROR)
    log = logging.getLogger(__name__)
    argv_gen()

    infofile = "chaporder.dat"
    if not os.path.isfile(infofile) :
        sys.exit("The chaporder.dat does not exist!")
    finfo = json.loads(open(infofile, "r").read())
    if not os.path.exists(finfo["name"]) :
        os.makedirs(finfo["name"])
    vols = sorted(finfo["links"], key=lambda x:x["idx"])
    for each in vols :
        idx = str(each["idx"])
        dbg("vol "+ idx)
        cid = str(each["cid"])+".buka"
        if not os.path.isfile(cid) :
            print cid + " failed"
            continue
        path = "./" + finfo["name"] + "/" + idx
        if not os.path.exists(path) :
            os.makedirs(path)
        flag = 0
        sn = 1
        fin = open(cid, "rb")
        byte = fin.read(1)
        lastbyte = 0x00
        try :
            while byte :
                if flag == 1 :
                    fout.write(byte)
                    if ord(byte) == 0xD9 :
                        if ord(lastbyte) == 0xFF : # EOI
                            flag = 0
                            sn = sn + 1
                            fout.close()
                elif ord(byte) == 0xD8 :
                    if ord(lastbyte) == 0xFF : # SOI
                        fout = open(path + "/%03d"%(sn) + ".jpg", "wb")
                        fout.write(lastbyte)
                        fout.write(byte)
                        flag = 1
                lastbyte = byte
                byte = fin.read(1)
        finally :
            fin.close()



        
