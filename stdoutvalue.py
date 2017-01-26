#!/usr/bin/python

def decodeStdoutValue(strValue):
    dict = {}

    lines = strValue.split("\n")
    for line in lines:
        if len(line) == 0:
            continue
        try:
            [name, value] = line.split("=")
            dict[name] = value
        except:
            print "Failed to parse [", line, "]"

    return dict;
