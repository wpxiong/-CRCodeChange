#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import array

DEBUG_MODE = True

def printDebug(strval):
  if DEBUG_MODE:
     print(strval)
  
def FileReplace(filename):
  print(filename)
  file=open(filename,"rb")
  lines=file.readlines()
  file.seek(0)
  file.close()
  os.remove(filename)
  newfile=open(filename,'wb')
  for line in lines:
    strline=line.replace(b'\r\n',b'\n')
    printDebug(strline)
    newfile.write(strline)
  newfile.close()

def DirReplace(dirname):
  if os.path.isdir(dirname)==False:
    print("%s is not dir " % dirname)
  else:
    for file in os.listdir(dirname):
      filename=dirname + "\\" + file
      if os.path.isdir(filename):
         DirReplace(filename)
      else:
         FileReplace(filename)
         print("File has changed!")

if __name__ == "__main__":
  argvs = sys.argv  # コマンドライン引数を格納したリストの取得
  argc = len(argvs) # 引数の個数
  printDebug("引数の個数:" +  str(argc))
  printDebug("引数:" + str(argvs))
  if argc < 2:
     printDebug("引数数が不正")
     sys.exit()
  folderPath= argvs[1]
  DirReplace(folderPath)