#!/usr/bin/python

def decodeStdoutValue(strValue):
    result = {}

    lines = strValue.split("\n")
    for line in lines:
        if len(line) == 0:
            continue
        try:
            [name, value] = line.split("=")
            result[name] = value
        except:
            print "Failed to parse [", line, "]"

    return result;
