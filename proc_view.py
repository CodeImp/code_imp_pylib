#!/usr/bin/python
# coding: utf8

'''
    Prints information from /proc.
    Examples of usage:
        "python ./proc_view.py --collect stack,comm,cmdline > proc_stacks_for_all_threads.txt" - collect kernel call stacks for all processes and threads.
        "python ./proc_view.py --filter_comm=veeam,kworker --collect stack,comm,cmdline > proc_stacks_for_specific_threads.txt" - collect kernel call stacks for processes and threads filtered by name.
'''

import os
import getopt, sys

def collect_proc_all(rootDir, collect):
    print "Collecting /proc files: ",collect
    return 0

    for dirName, subdirList, fileList in os.walk(rootDir):
        printedDirName=None

        for fname in fileList:
            if fname in collect:
                if printedDirName == None:
                    print('------------------------------------------------------------------------------')
                    print('Directory: %s' % dirName)
                    printedDirName=dirName

                print('%s:' % fname)
                f = open(dirName+'/'+fname, 'r');
                print(f.read())
    return 0


def collect_proc_filter(rootDir, filter_type, filter_value, collect):
    print "Collecting /proc with filter"
    print "filter_type=",filter_type
    print "filter_value=",filter_value
    print "files: ",collect

    for dirName, subdirList, fileList in os.walk(rootDir):
        printedDirName=None

        bPrint = False
        if filter_type == "comm":
            if "comm" in fileList:
                f = open(dirName+"/comm", 'r');
                commValue = f.read()

                for filter in filter_value:
                    if commValue.find(filter) >= 0:
                        bPrint = True
        else:
            print "Invalid filter type"
            break

        if bPrint:
            for fname in fileList:
                if fname in collect:
                    if printedDirName == None:
                        print('------------------------------------------------------------------------------')
                        print('Directory: %s' % dirName)
                        printedDirName=dirName

                    print('%s:' % fname)
                    f = open(dirName+'/'+fname, 'r');
                    print(f.read())

    return 0

def print_usage():
    print "Usage:"
    print "\t--help - print usage"
    print "\t--root=<branch> - /proc by default, but you can set subtree"
    print "\t--filter_comm=<process and thread names> - filter by processes name"
    print "\t--collect=<file names>"

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'x', ['help','root=','filter_comm=','filter_exe=', 'collect='])

        print "Input options: ",opts
        print "Input arguments: ", args
    except:
        print_usage()
        exit(2)

    rootDir='/proc'
    filter_type = None
    filter_value = None
    collect = None

    for opt, arg in opts:

        if opt == "--filter_comm":
            filter_type = "comm"
            filter_value = arg.split(',')
        elif opt == "--filter_exe":
            filter_type = "exe"
            filter_value = arg
        elif opt == "--collect":
            collect = arg.split(',')
        elif opt == "--root":
            rootDir = arg
        else:
            print "Invalid option ",opt

    if filter_type == None:
        res = collect_proc_all( rootDir, collect )
    else:
        res = collect_proc_filter( rootDir, filter_type, filter_value, collect )

    exit(res)

if __name__ == "__main__":
    main()
