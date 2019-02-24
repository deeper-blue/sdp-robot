#!/usr/bin/env python3
# 'Server' will first receive the message, then separate the string bases on the ';'
# and call the corresponding function from high level interface
# Author(s):
#   Wanjing Chen

import socket
from high_level import dummy

HOST = '192.168.105.116'  # Standard loopback interface address (localhost)
# HOST = "127.0.0.1"
PORT = 64432        # Port to listen on (non-privileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print('listening to IP ' + HOST)
conn, addr = s.accept()
print('Connected by', addr)

def splitNcheck(message):
    hle = dummy.High_Level_Interface()
    data = message.decode('utf-8').split(";")
    if(data[0] == "move_piece" and len(data)==3):
        hle.move_piece(data[1],data[2])
    elif(data[0] == "move" and len(data)==3):
        hle.move(data[1],data[2])
    elif(data[0] == "take_piece" and len(data)==4):
        hle.take_piece(data[1],data[2],data[3])
    elif(data[0] == "perform_castling_at" and len(data)==5):
        hle.perform_castling_at(data[1],data[2],data[3],data[4])
    elif(data[0] == "reset"):
        hle.reset()
    else:
        print('No action')
    print("Called function: " + data[0])


while True:
    message = conn.recv(1024)
    if not message:
        break
    splitNcheck(message)
    conn.sendall(message)
