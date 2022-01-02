import sys
import os
import time
import random
import subprocess
import random
import threading
import socket


a = """
NNNNNNNN        NNNNNNNNEEEEEEEEEEEEEEEEEEEEEETTTTTTTTTTTTTTTTTTTTTTT
N:::::::N       N::::::NE::::::::::::::::::::ET:::::::::::::::::::::T
N::::::::N      N::::::NE::::::::::::::::::::ET:::::::::::::::::::::T
N:::::::::N     N::::::NEE::::::EEEEEEEEE::::ET:::::TT:::::::TT:::::T
N::::::::::N    N::::::N  E:::::E       EEEEEETTTTTT  T:::::T  TTTTTT
N:::::::::::N   N::::::N  E:::::E                     T:::::T        
N:::::::N::::N  N::::::N  E::::::EEEEEEEEEE           T:::::T        
N::::::N N::::N N::::::N  E:::::::::::::::E           T:::::T        
N::::::N  N::::N:::::::N  E:::::::::::::::E           T:::::T        
N::::::N   N:::::::::::N  E::::::EEEEEEEEEE           T:::::T        
N::::::N    N::::::::::N  E:::::E                     T:::::T        
N::::::N     N:::::::::N  E:::::E       EEEEEE        T:::::T        
N::::::N      N::::::::NEE::::::EEEEEEEE:::::E      TT:::::::TT      
N::::::N       N:::::::NE::::::::::::::::::::E      T:::::::::T      
N::::::N        N::::::NE::::::::::::::::::::E      T:::::::::T      
NNNNNNNN         NNNNNNNEEEEEEEEEEEEEEEEEEEEEE      TTTTTTTTTTT      
                                                                    
"""
print(a)

b = """
NETWORKING EXPLOITATION TOOLKIT

DESIGNED BY DARKC0DE
"""
print("Here are your options:")
print("1 = WIFI ATTACKS")
print("2 - PORT AND VULNERABILITY SCANNING")
print("3 - DOS/DDOS ATTACKS")


num = input("Enter your chosen option > ")
#DDOS ATTACK
#NETWORK SCAN
if int(num) == 1:
      os.system('clear')
      os.system('sudo python3 wifiattacks.py')
      
elif int(num) == 2:
      os.system('clear')
      os.system('sudo python3 scanner.py')
      
elif int(num) == 3:
      os.system('clear')
      os.system('sudo python3 dos.py')
      
else:
    print("You entered an invalid number, please restart the script")




