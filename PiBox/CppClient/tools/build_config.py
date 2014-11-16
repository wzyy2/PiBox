#!/usr/bin/python
import os
import sys
from Config import *

basedir = os.path.dirname(os.path.realpath(__file__)) + "/../"
gen_dir = basedir + "gen/"


HeaderFilename = gen_dir + 'autogen.h'

print HeaderFilename

HeaderFile = open(HeaderFilename, 'w')
def writeheader(s): pininfoHeaderFile.write(s+"\n");

writeheader("// auto-generated file")

if DEBUG_BUILD == 1
    writeheader("#define DEBUG_BUILD 1")


HeaderFile.close()