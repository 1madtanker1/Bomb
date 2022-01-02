import scapy.all as scapy
import re
import time
import os
import sys
import subprocess
#Some of this code was used from outside sources

b = """

  ,/((/,                            
                                       (%%%%%%%####%%%%%%%*                     
                                   .%%%%*                #%%%%                  
                                   %%    (%%%%%%%%%%%%%%    *%%                 
                                       %%%#            %%%%                     
                                            %%%%%%%%%                           
                                           #%       %%                          
                                               %%%(        (@@@@@@@   #@@@.     
     #@@@@/         *@@@@@@          @@@@@    %%%%%.     @@@@@@@@@@  .@@@@@     
      @@@@@.       *@@@@@@@@        #@@@@.               @@@@@                  
       @@@@@      .@@@@ @@@@&      (@@@@.     @@@@@      @@@@@@@@@@   @@@@@     
        @@@@@     @@@@  .@@@@(    ,@@@@#      @@@@@      @@@@@@@@@@   @@@@@     
         @@@@@   @@@@/   (@@@@    @@@@%       @@@@@      @@@@@        @@@@@     
         *@@@@, @@@@@     @@@@@  @@@@@        @@@@@      @@@@@        @@@@@     
          &@@@@#@@@@       @@@@#@@@@@         @@@@@      @@@@@        @@@@@     
           @@@@@@@@         @@@@@@@@          @@@@@      @@@@@        @@@@@     
             @@@@#           (@@@@.           @@@@@      @@@@@        @@@@@     
                                                                                

"""
print(b)

time.sleep(2)
ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")

while True:
    ip_add_range_entered = input("Enter the Ip and range of the network you want to scan (i.e. 192.168.1.1/24) >  ")
    if ip_add_range_pattern.search(ip_add_range_entered):
        print(f"{ip_add_range_entered} is a valid range")
    break

#ARPing the network    
arp = scapy.arping(ip_add_range_entered)

time.sleep(2)

#Thank you to David Bombal for the tutorial

#part 2 of the script (I coded this part on my own)


print("Now you have a few options")

op=True
for i in range(1):
    print("""
    1. Scan an IP with NMAP
    2. Return to the homescreen
    """)

op = input("Enter your choice > ")

if op =="1":
    IPy = input("Enter your IP to scan > ")
    nmap = ("sudo", "nmap", IPy,"-Pn", "-sV", "-O")
    p = subprocess.Popen(nmap, stdout=subprocess.PIPE,text=True)
    
    (output, err) = p.communicate()
    
    p_status = p.wait()
    
    print(output)
   
elif op =="2":
    print("\n NET will now return to the main menu")
    os.system('clear')
    os.system('sudo python3 hacker2.py')

elif op !="":
    print("\n no valid answer try again")




