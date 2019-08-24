# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 12:20:00 2019

@author: quantum
"""

from os import listdir,remove
import shutil
from win10toast import ToastNotifier
toaster = ToastNotifier()
#toaster.show_toast("Sample Notification","Python is awesome!!!")

DIRECTORY = 'C:\\Users\\quantum\\Downloads'  # music source Directory
COPY_DIRECTORY = 'C:\\Users\\quantum\\Music'  # Destination directory

d = DIRECTORY
c1 = COPY_DIRECTORY
zips="C:\\Users\\quantum\\Documents\\zips"
exe="C:\\Users\\quantum\\Documents\\exes"
pdf ="C:\\Users\\quantum\\Documents\\pdf"


def transfer(tp,copy_directory):
    d_list=[] #deletelist 
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
            d_list.append(d+"\\"+i)
    for i in d_list:
        remove(i)
    if file_count!=0:
        toaster.show_toast( 'Transferred %s files' % file_count)


if __name__ == "__main__":
    #print("checking for mp3")
    transfer(".mp3",c1)
    transfer(".zip",zips)
    transfer(".rar",zips)
    transfer(".exe",exe)
    transfer(".pdf",pdf)