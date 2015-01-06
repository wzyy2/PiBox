#!/usr/bin/python
import os
import sys
from Config import *

basedir = os.path.dirname(os.path.realpath(__file__)) + "/../"
gen_dir = basedir + "gen/"


HeaderFilename = gen_dir + 'autogen.h'

print HeaderFilename

HeaderFile = open(HeaderFilename, 'w')
def writeheader(s): HeaderFile.write(s+"\n");

writeheader("// auto-generated file")
writeheader("#ifndef AUTOGEN_H \n")
writeheader("#define AUTOGEN_H \n")

if DEBUG_BUILD == 1:
    writeheader("#define DEBUG_BUILD 1 \n")

writeheader("#endif // AUTOGEN_H\n")
HeaderFile.close()