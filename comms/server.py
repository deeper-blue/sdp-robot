#!/usr/bin/env python3
# 'Server' will first receive the message, then separate the string bases on the ';'
# and call the corresponding function from high level interface
# Author(s):
#   Wanjing Chen
import socket
from . import dummy

HOST = '192.168.105.116'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print('listening to IP ' + HOST)
conn, addr = s.accept()
print('Connected by', addr)
while True:
    message = conn.recv(1024)
    splitNcheck(message)
    if not data:
        break
        conn.sendall(message)

def splitNcheck(message):
    data = message.split(";")
    if(data[0] == "move_piece"):
        dummy.move_piece(self,data[1],data[2])
    else if(data[0] == "move"):
        dummy.move(self,data[1],data[2])
    else if(data[0] == "take_piece"):
        dummy.take_piece(self,data[1],data[2],data[3])
    else if(data[0] == "perform_castling_at"):
        dummy.perform_castling_at(self,data[1],data[2],data[3],data[4])
    else if(data[0] == "reset"):
        dummy.reset(self)
    print("Called function: " + data[0])
