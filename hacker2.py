import sys
import os
import time
import random
import subprocess
import random
import threading
import socket


a = """

NmNMNmNMNNMMNNMMmNMMmNMNmNMNmNMNmNMNmNMNmNMNmNMmmNMNNMMNNMMmNMNmmMNmNMNmNMNmNMNmNMNmNMNmNMNNMMNNMMNN
NMNmNMNmMMNmMMNNMMmNMMmNMNmNMNmNMNmNNmhhhysssssosysyhddNNmNMMmdyshmMNmNMNmNMNmNMNmNMNmNMNmNMNmMMNNMM
NmNMNmNMNmMMNmMMmNMMmNMMmNMNmNMNdyyo++/+++/++//++//++//+osyddy+++/odNMNmNMmysyyymMNmNMNmNMNmMMNmMMmN
NMNmNMNmMMNmMMmmMMmNMMmNMMmNNhs+/+++/+++/++//++//++//++//++/+++/+++/odNNo-......./yMNmNMNmNMNmMMmmMM
NmNMNmMMNmMMNmMMmmMMmNMMmmho++//++/+++/+++/+++/+++/+++/+++/++//++//++/o-...........:hMNmNMNmMMNmMMmm
NMNmNMNmMMNmMMNmMMmmMMmdy+++//++/+++/+++/+++/+++/+++/+++/++//++//++//++/:-/hmmmo-..../hMNmNMNmMMNmMM
NmNMNmNMNmMMNmMMNmMMNds+++//++/+++/+++/+++/+++/+++/+++/++//++//++//++//++/sdNMNmmo-..../hMNmNMNmMMNm
NMNmNMNmNMNmNMNmMMNmy+++//++/+++/+++/+++/+++/+++/+++/++//++//++//++//++/++++ydNMNmd+....-/dMNmNMNmMM
NmNMNmNMNmNMNmNMNmmo++//++/+++/+++/+++/+++/+++/+++/++//++//++//++//++/+++/++++ydNMNmd+....-+dMNmNMNm
NMNmNMNmNMNmNMNmNd++//++/+++/+++/+++/+++/+++/+++/++//++//++//++//++/+++/+++/+++smmNMNmd/...-omNMNmNM
NmNMNmNMNmNMNmNMh+//++//++//++//++//++//++//++/++//++//++//++//++//++//++//++oymNMNmNMNmh/+hNMNmNMNm
NMNmNMNmNMNmNMNh+/+++/+++/++//++//++//++//++/+++/+++/+++/+++/+++/+++/++//++/+dNMNmNMNmNMNmNMNmNMNmNM
NmNMNmNMNmNMNmm++++/+++/++//++//++//++//++/+++/+++/+++/+++/+++/+++/++//++//++yNmNMNmNMNmNMNmNMNmNMNm
NMNmNMNmNMNmNMs++/+++/++//++//++//++//++/+++/+++/+++/+++/+++/+++/++//++//++//+dMNmNMNmNMNmNMNmNMNmNM
NmNMNmNMNmNMNh+/+++/++/:------://+//-------:///+++/+++/+++/+++//:--:///++//++/omNMNmNMNmNMNmNMNmNMNm
NMNmNMNmNMNmNs+++/++//+-        ./+/        `-/+/+++/+++/+++//`     `:+//++//++mMmNMNmNMNmNMNmNMNmNM
MmNMNmNMNmNMN++/++//++/.  .:::-   //   ::::`  .+++/+++/+++/+/`  -:-   /++//++/+yNMMmNMNmNMNmNMNmNMNm
NMNmNMNmNMNmd/+++/+++/+-  .++/+`  :/   ///+:  `+//-.`  `.:++/`  -:///+++/++//++sMmNMNmNMNmNMNmNMNmNM
NmNMNmNMNmNMd++/+++/+++.  ./+++`  -/   /++/:  `//`  `..`  ./+:`     .//++//++//sNMMmNMNmNMNmNMNmNMNm
NMNmNMNmNMNmd/+++/+++/+-  .++/+`  :/   ///+:  `+-  .////`  :/+//:-.  `///++//++sMmNMNmNMNmNMNmNMNmNM
NmNMNmNMNmNMm++/+++/+++.  .///:   :/   ////.  .+:  `://:   :/.``:/:`  :++//++//sNMMNNMNmNMNmNMNmNMNm
NMNmNMNmNMNmNo+++/+++/+-   ```  `-+/   ````  ./+/-`  ``  `-//-`  ``  .///++//++dMNNMNNNMNmNMNmNMNmNM
MNNMNNNMNmNMNy+/+++/+++-.......:/+//.......-://++//-....://+++/-...-://++//++/+mNMMNNMNNNMNmNMNmNMNm
NMNNNMNmNMNmNN+++//++/++//++//++//++//++//++//++//++//++//++//+//++//++//++//+yNMNNMMNNMNNNMNmNMNmNM
MNNMMNNMNmNMNmh+/++/+++/+++/+++/+++/+++/+++/++//++//++//++//++/+++/+++/+++/++oNNNNMNNMMNNMNmNMNmNMNm
NMMNNMMmNMNmNMNs+/+++/+++/+++/+++/+++/+++/++//++//++//++//++/+++/+++/+++/++++dmNMNNMMNNMMNNMNmNMNmNM
MNNMMNNMMmNMNmNNs++/+++/+++/+++/+++/+++/++//++//++//++//++/+++/+++/+++/+++/+hNMNmNMNNMMNNMMmNMMmNMNm
mMMNNMMmNMMmNMMmms+++/+++/+++/+++/+++/++//++//++//++//++/+++/+++/+++/+++/++dMNmNMNmMMNmMMNNMMmNMMmNM
MNmMMmmMMmNMMmNMMmy++++/+++/+++/+++/++//++//++//++//++/+++/+++/+++/+++/++omNmNMNmNMNmMMNmMMmNMMmNMMm
mMMNmMMmmMMmNMMmNMMho/+++/+++/+++/++//++//++//++//++/+++/+++/+++/+++/+++ymmNMNmNMNmMMNmMMmmMMmNMMmNM
MNmMMNmMMmmMMmNMMmNMNy+//++/+++/+++/+++/+++/+++/++//++//++//++//++/+++sdmNMNmNMNmMMNmMMNmMMmmMMmNMMm
mMMNmMMNmMMmNMMmNMNmNMNy+/+++/+++/+++/+++/+++/++//++//++//++//++/+++sdmNMNmNMNmNMNmMMNmMMNmMMmmMMmNM
MNmMMNmMMNNMMmNMMmNMNmNMNys++++/+++/+++/+++/++//++//++//++//++/+++ydmNMNmNMNmNMNmNMNmMMNmMMNmMMNNMMm
mNMNmMMNmMMNNMMNNMNmNMNmNMNdho+++/+++/+++/++//++//++//++//++/+osdmmNMNmNMNmNMNmNMNmNMNmNMNmMMNNMMNNM
MNmNMNmNMNNMMNNMMNNMNmNMNmNMNmmdso+++++/++//++//++//++//++ooydNNmNMNmNMNmNMNmNMNmNMNmNMNmNMNmMMNNMMN
mNMNmNMNmNMNNMMNNMNNNMNmNMNmNMNmNNmddyssoo+++++++++oooshdmmmMNNNMNmNMNmNMNmNMNmNMNmNMNmNMNmNMNNMMNNM
MNmNMNmNMNNNMNNMMNNMNNNMNmNMNmNMNmNMNmNMmdmmddmmddNNmmNMNNMMNNMNNNMNmNMNmNMNmNMNmNMNmNMNmNMNmNMNNNMN

"""
print(a)
print("Here are your options:")
print("1 = Preform a Wifi scan to find network devices")
print("2 - Scan a port")
print("3 - DOS attack an IP")
print("4 - Read credits")

num = input("Enter your chosen option > ")
#DDOS ATTACK
#NETWORK SCAN
elif int(num) == 1:
      os.system('clear')
      os.system('sudo python3 wifiscan.py')
      
elif int(num) == 2:
      os.system('clear')
      os.system('sudo python3 portscanner.py')
      
elif int(num) == 3:
      os.system('clear')
      os.system('sudo python3 dos.py')

elif int(num) == 4:
      os.system('vim credits.txt')
      
else:
    print("You entered an invalid number, please restart the script")



