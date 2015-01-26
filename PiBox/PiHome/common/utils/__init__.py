#coding=utf-8
import re
import sys
from socket import *


def validateEmail(email):
    if len(email) > 7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
            return 1
    return 0

def lines2html(lines):
    out = ''
    for line in lines:
        out += line
    return out

def lineslimit(lines, max):
    count = len(lines)
    if count > max:
        lines = lines[count-max:count]
    return lines2html(lines)