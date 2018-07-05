#!/usr/bin/python
# -*- coding: utf-8 -*-


#不断重启程序(外部)
def restart_myself():
  import time,os,sys
  print "Restart 3 secods later"
  time.sleep(3)
  python = sys.executable
  os.execl(python, python, * sys.argv)
  return 0

print "Main Start"
restart_myself()
print "Main End"