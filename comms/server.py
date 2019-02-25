#!/usr/bin/env python3
# 'Server' will first receive the message, then separate the string bases on the ';'
# and call the corresponding function from high level interface
# Author(s):
#   Wanjing Chen

import socket
from high_level import dummy
import ast

HOST = '192.168.105.116'  # Ev3 address
PORT = 64432        # Port to listen on (non-privileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print('listening on IP ' + HOST)
conn, addr = s.accept()
print('Connected by', addr)

def splitNcheck(message):
    result = "waiting for result"
    hle = dummy.High_Level_Interface()
    # convert byte string message back to normal string message
    data = message.decode('utf-8').split(";")
    if(data[0] == "move_piece" and len(data)==3):
        # convert cells information from type string back to tuple
        cell1 = ast.literal_eval(data[1])
        cell2 = ast.literal_eval(data[2])
        try:
            hle.move_piece(cell1,cell2)
            result = "OK"
        except:
            result = "Error: %s" % (exception.message)
    elif(data[0] == "move" and len(data)==3):
        cell1 = ast.literal_eval(data[1])
        cell2 = ast.literal_eval(data[2])
        try:
            hle.move(cell1,cell2)
            result = "OK"
        except:
            result = "Error: %s" % (exception.message)
    elif(data[0] == "take_piece" and len(data)==4):
        cell1 = ast.literal_eval(data[1])
        cell2 = ast.literal_eval(data[2])
        piece_name = data[3]
        try:
            hle.take_piece(cell1,cell2,piece_name)
            result = "OK"
        except:
            result = "Error: %s" % (exception.message)
    elif(data[0] == "perform_castling_at" and len(data)==5):
        cell1 = ast.literal_eval(data[1])
        cell2 = ast.literal_eval(data[2])
        cell3 = ast.literal_eval(data[3])
        cell4 = ast.literal_eval(data[4])
        try:
            hle.perform_castling_at(cell1,cell2,cell3,cell4)
            result = "OK"
        except:
            result = "Error: %s" % (exception.message)
    elif(data[0] == "reset"):
        try:
            hle.reset()
            result = "OK"
        except:
            result = "Error: %s" % (exception.message)
    else:
        print('No action')
    print(result)
    print("Called function: " + data[0])
    print("\n")
    return result


while True:
    message = conn.recv(4000)
    if not message:
        break
    response = splitNcheck(message)
    # send the byte message response back to the client
    conn.sendall(str.encode(response))
