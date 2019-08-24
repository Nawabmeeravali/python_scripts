# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 11:27:54 2019

@author: quantum
"""

import os, subprocess
import psutil


from win10toast import ToastNotifier
toaster = ToastNotifier()


totalsize = psutil.disk_usage('C:').total / 2**30
rem_size=psutil.disk_usage(".").free/ 2**30
del_dir = r'c:\windows\temp'
pObj = subprocess.Popen('del /S /Q /F %s\\*.*' % del_dir, shell=True, stdout = subprocess.PIPE, stderr= subprocess.PIPE)
rTup = pObj.communicate()
rCod = pObj.returncode
if rCod == 0:
    toaster.show_toast('Success: Cleaned Windows Temp Folder')
else:
    toaster.show_toast( 'Fail: Unable to Clean Windows Temp Folder')

#print('totalsize: ',round(totalsize,2), ' GB')
#toaster.show_toast("remaining size  "+ str(round(rem_size,2))+"GB")