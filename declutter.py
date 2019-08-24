# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 12:20:00 2019

@author: quantum
"""

from os import listdir,remove,path
import shutil
from win10toast import ToastNotifier
toaster = ToastNotifier()
#toaster.show_toast("Sample Notification","Python is awesome!!!")


USERDIR = path.expanduser('~')


d       = USERDIR + '\\Downloads'
c1      = USERDIR + '\\Music'
zips    = USERDIR + "\\Documents\\zips"
exe     = USERDIR + "\\Documents\\exes"
pdf     = USERDIR + "\\Documents\\pdf"


def transfer(tp,copy_directory):
    
    print ("Copying %s Files from %s to %s" % (tp,d, copy_directory))
    file_count = 0
    for i in listdir(d):
        if i.find("Unconfirmed") !=-1:
            remove(d+"\\"+i)
            toaster.show_toast("removing incomplete downloads")
            
        elif  i.find(tp) !=-1:
            file_count += 1
            print ("transferring %s" % i)
            shutil.copy(d+"\\"+i, copy_directory)
            remove(d+"\\"+i, copy_directory)
            
    if file_count!=0:
        toaster.show_toast( 'Transferred %s files' % file_count)


if __name__ == "__main__":
    transfer(".mp3",c1)
    transfer(".zip",zips)
    transfer(".rar",zips)
    transfer(".exe",exe)
    transfer(".pdf",pdf)