#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
Script to check for the existence of new applications installed

Creation date: 17/01/2017
Date last updated: 19/03/2017

Nagios check_app plugin

* License: GPL
* Copyright (c) 2017 DI-FCUL
* 
* Description:
* 
* This file contains the check_app plugin
* 
* Use the nrpe program to check the application are installed in remote host.
* 
* 
* This program is free software: you can redistribute it and/or modify
* it under the terms of the GNU General Public License as published by
* the Free Software Foundation, either version 3 of the License, or
* (at your option) any later version.
* 
* You should have received a copy of the GNU General Public License
* along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import os
import sys
import difflib
from optparse import OptionParser

__author__ = "\nAuthor: Raimundo Henrique da Silva Chipongue\nE-mail: fc48807@alunos.fc.ul.pt, chipongue1@gmail.com\nInstitution: Faculty of Science of the University of Lisbon\n"
__version__= "1.0.0"

# define exit codes
ExitOK = 0
ExitWarning = 1
ExitCritical = 2
ExitUnknown = 3

def checkapp(opts):
    path = opts.storefolder
    if opts.path:
        folder_paths = opts.path
        folder_paths = folder_paths.replace(","," ")
    else:
        folder_paths = "/usr/bin/ /sbin/ /bin/ /usr/sbin/ /usr/local/bin/"
        
    path_exist = ("%sapp1.txt" %path)
    if not os.path.exists(path_exist):
        if os.path.exists(path):
            os.popen("find %s | sort > %sapp1.txt" %(folder_paths, path)).read()           
        else:
            os.makedirs(path)
            os.popen("find %s | sort > %sapp1.txt"%(folder_paths, path)).read()
     
    diff_num = int(os.popen("find %s | sort | diff - %sapp1.txt | wc -l"%(folder_paths, path)).read())
    os.popen("find %s | sort | diff - %sapp1.txt > %sappdiff.txt"%(folder_paths, path, path)).read()    
    if diff_num:
        diff_num = diff_num -1
        print("%s recently installed applications, see %sappdiff.txt" %(diff_num,path))
        sys.exit(ExitCritical)
    else:
        print("Not found any recently installed applications")
        sys.exit(ExitOK)

def main():
    parser = OptionParser("usage: %prog This plugin doesn't require any argument for this works.")
    parser.add_option("-V","--version", action="store_true", dest="version", help="This option show the current version number of the program and exit")
    parser.add_option("-A","--author", action="store_true", dest="author", help="This option show author information and exit")
    parser.add_option("-p","--path", dest="path", default=False,
                      help="Specify all bin folder you need to monitoring, Ex. check_app.py -p /usr/bin/,/sbin/,/bin/,/usr/sbin/,/usr/local/bin/, if this argument is not used, the program uses the default folders. Whenever you change the folders to be monitored, restart the file /tmp/appdiff.txt")
    parser.add_option("-s","--storefolder", dest="storefolder", default="/tmp/",
                      help="Specify the full path of the folder where you save the file with information of installed applications." +
                      "By default this is /tmp/ folder")
    (opts, args) = parser.parse_args()
    if not os.path.exists(opts.storefolder):
        parser.error("Please, this program requires to specifay a valid and private folder to store temp file")
    if opts.author:
        print(__author__)
        sys.exit()
    if opts.version:
        print("check_app.py %s"%__version__)
        sys.exit()
    checkapp(opts)

if __name__ == '__main__':
    main()

