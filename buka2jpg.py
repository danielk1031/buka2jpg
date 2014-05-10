#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging, inspect, json, argparse, glob
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
    parser.add_argument('-f', '--files', type=str, nargs='+', action="store", dest="files", default=None, help='extract jpg from the specific file')
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
    vols = []
    if os.path.isfile(infofile) :
        finfo = json.loads(open(infofile, "r").read())
        comicname = finfo["name"]
        if args.files == None :
            vols = sorted(finfo["links"], key=lambda x:x["idx"])
        else :
            for i in args.files :
                if not os.path.isfile(i) :
                    print i + " does not exist"
                    continue
                if i[:2] == "./" :
                    i = i[2:]
                for each in finfo["links"] :
                    if str(each["cid"]) == i[:-5] : # the cid exist in chaporder.dat
                        vols.append({"idx":each["idx"], "cid":each["cid"]})
                        break
                if vols == [] or str(vols[-1]["cid"]) != i[:-5] : # cid does not exist
                    vols.append({"idx":i[:-5], "cid":i[:-5]})
    else : # chaporder.dat does not exist
        comicname = "comic"
        if args.files == None :
            for i in sorted(glob.glob("*.buka")) :
                vols.append({"idx":i[:-5], "cid":i[:-5]})
        else :
            for i in args.files :
                vols.append({"idx":i[:-5], "cid":i[:-5]})

    if vols == [] :
        sys.exit("there is no target to extract!")
    for each in vols :
        idx = str(each["idx"])
        dbg("vol "+ idx)
        cid = str(each["cid"])+".buka"
        if not os.path.isfile(cid) :
            print cid + " does not exist"
            continue
        if not os.path.exists(comicname) :
            os.makedirs(comicname)
        path = "./" + comicname + "/" + idx
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



        
