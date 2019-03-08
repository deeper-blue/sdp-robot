#!/usr/bin/env python3
# 'Server' will first receive the message, then separate the string bases on the ';'
# and call the corresponding function from high level interface
#
# Author(s):
#   Wanjing Chen
#   Filip Smola

import socket
from high_level import hli_implementation
from low_level import arch, platform, grabber
import ast
import time

# Instantiate LLI
ar = arch.Arch()
pl = platform.Platform()
gr = grabber.grabber

# Instantiate HLI
hli = hli_implementation.High_Level_Interface(('L',1), ar, pl, gr)

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
    # convert byte string message back to normal string message
    data = message.decode('utf-8').split(";")
    if(data[0] == "move_piece" and len(data)==3):
        # convert cells information from type string back to tuple
        cell1 = ast.literal_eval(data[1])
        cell2 = ast.literal_eval(data[2])
        try:
            t0 = time.time()
            hli.move_piece(cell1,cell2)
            t1 = time.time()
            result = "OK (%f s)" % (t1 - t0)
        except Exception as exception:
            result = "Error: %s" % (repr(exception))
    elif(data[0] == "move" and len(data)==3):
        cell1 = ast.literal_eval(data[1])
        cell2 = ast.literal_eval(data[2])
        try:
            t0 = time.time()
            hli.move(cell1,cell2)
            t1 = time.time()
            result = "OK (%f s)" % (t1 - t0)
        except Exception as exception:
            result = "Error: %s" % (repr(exception))
    elif(data[0] == "take_piece" and len(data)==4):
        cell1 = ast.literal_eval(data[1])
        cell2 = ast.literal_eval(data[2])
        piece = ast.literal_eval(data[3])
        try:
            t0 = time.time()
            hli.take_piece(cell1,cell2,piece)
            t1 = time.time()
            result = "OK (%f s)" % (t1 - t0)
        except Exception as exception:
            result = "Error: %s" % (repr(exception))
    elif(data[0] == "perform_castling_at" and len(data)==5):
        cell1 = ast.literal_eval(data[1])
        cell2 = ast.literal_eval(data[2])
        cell3 = ast.literal_eval(data[3])
        cell4 = ast.literal_eval(data[4])
        try:
            t0 = time.time()
            hli.perform_castling_at(cell1,cell2,cell3,cell4)
            t1 = time.time()
            result = "OK (%f s)" % (t1 - t0)
        except Exception as exception:
            result = "Error: %s" % (repr(exception))
    elif(data[0] == "reset"):
        try:
            t0 = time.time()
            hli.reset()
            t1 = time.time()
            result = "OK (%f s)" % (t1 - t0)
        except Exception as exception:
            result = "Error: %s" % (repr(exception))
    elif(data[0] == "en_passant"):
        cellA = ast.literal_eval(data[1])
        cellB = ast.literal_eval(data[2])
        cellTake = ast.literal_eval(data[3])
        piece = ast.literal_eval(data[4])
        try:
            t0 = time.time()
            hli.en_passant(cellA, cellB, cellTake, piece)
            t1 = time.time()
            result = "OK (%f s)" % (t1 - t0)
        except Exception as exception:
            result = "Error: %s" %(repr(exception))
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
