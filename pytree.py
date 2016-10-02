#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

def print_tree(path, indent="", lst = []):
    files = os.listdir(path)
    files = filter( lambda f: not f.startswith('.'), files)
    
    for i in range(0, len(files)):
        fullpath = path + "/" + files[i]
        lst.append(fullpath)
        if i == len(files)-1:
            print indent + '`–- ' + files[i]
            
        else:
            print indent + '|–- ' + files[i]
            

        if os.path.isdir(fullpath):
            if i == len(files)-1:
                print_tree(fullpath, indent+'    ')
            else:
                print_tree(fullpath, indent+'|   ')
    return lst



if __name__ == '__main__':
    # just for demo

    # Process command-line arguments.
	dir = os.getcwd()

	if len(sys.argv) == 1:
		dir = '.'
	if len(sys.argv) == 2:
	    dir = sys.argv[1]
	elif len(sys.argv) > 2:
	    print "Usage: %s [path]" % sys.argv[0]
	    sys.exit(0)

	# Make sure we really have a path.
	if not os.path.isdir(dir):
	    print "E: that is not a valid path"
	    sys.exit(0)

	print dir
	k = print_tree(dir)
	print

	d1,f1=0,0
	for i in k:
		if os.path.isdir(i):
			d1+=1
		else:
			f1+=1
	# print os.getcwd()
	print d1, "directories,",f1, "files" #, k, "list"

    # subprocess.run(['tree'] + sys.argv[1:])
