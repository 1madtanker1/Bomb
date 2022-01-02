import os
import subprocess
options = """
1. SCAN YOUR WIFI NETWORK
2. DEAUTH A WIFI NETWORK

"""

choice = input("Enter your choice > ")
deauth = "deauth.py"
if choice == 1:
    os.system('clear')
    os.system('wifiscan.py')

elif choice == 2:
    subprocess.run('chmod', 'a+x', deauth)
    mac = input("Enter the MAC address you wish to deauth > ")
    subprocess.run('sudo', './deauth.py', mac)

else:
    print("\n No valid input try again")
