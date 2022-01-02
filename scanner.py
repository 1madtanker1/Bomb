import os

print("Here you can conduct Port Scans and Vulerability scans for future use")

print("Here are your options:")
options = """
1. CONDUCT A PORT SCAN
"""

opt = input("Enter your choice > ")

if opt == 1:
    os.system('clear')
    os.system('sudo python3 wifiscanner.py')

else:
    print("No valid number try again")
