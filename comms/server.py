#!/usr/bin/env python3
# 'Server' will first receive the message, then separate the string bases on the ';'
# and call the corresponding function from high level interface
#
# Author(s):
#   Wanjing Chen
#   Filip Smola

import socket
import ast
import time

# Server host and port
HOST = socket.gethostname()
PORT = 64432

# Accepts connections until terminated externally
class Server:
    # Initialize the socket
    def __init__(self, hli):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((HOST, PORT))

        self.hli = hli

    # Start listening on the socket, accepting connections until explicitly stopped
    def run(self):
        # Start listening
        self.s.listen(1)
        print('listening on %s:%d ' % (HOST, PORT))

        # Accept connections
        while True:
            # Accept connection
            conn, addr = self.s.accept()
            print('Connected by %s' % (addr))

            # Receive message until empty
            while True:
                message = conn.recv(4000)
                if not message:
                    break

                # Invoke HLI function and get response
                response = self.splitNcheck(message)

                # Send the byte message response back to the client
                conn.sendall(str.encode(response))

    # Split message, check it, and invoke the appropriate HLI function
    def splitNcheck(self, message):
        # Preapre result
        result = "Error: no result"

        # Convert byte string message back to normal string message and split by ;
        data = message.decode('utf-8').split(";")

        # Decide based on first segment and check length, then convert args and invoke
        if(data[0] == "move_piece" and len(data)==3):
            cell1 = ast.literal_eval(data[1])
            cell2 = ast.literal_eval(data[2])
            try:
                t0 = time.time()
                self.hli.move_piece(cell1,cell2)
                t1 = time.time()
                result = "OK (%f s)" % (t1 - t0)
            except Exception as exception:
                result = "Error: %s" % (repr(exception))
        elif(data[0] == "move" and len(data)==3):
            cell1 = ast.literal_eval(data[1])
            cell2 = ast.literal_eval(data[2])
            try:
                t0 = time.time()
                self.hli.move(cell1,cell2)
                t1 = time.time()
                result = "OK (%f s)" % (t1 - t0)
            except Exception as exception:
                result = "Error: %s" % (repr(exception))
        elif(data[0] == "take_piece" and len(data)==4):
            cell1 = ast.literal_eval(data[1])
            cell2 = ast.literal_eval(data[2])
            piece_name = ast.literal_eval(data[3])
            try:
                t0 = time.time()
                self.hli.take_piece(cell1,cell2,piece_name)
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
                self.hli.perform_castling_at(cell1,cell2,cell3,cell4)
                t1 = time.time()
                result = "OK (%f s)" % (t1 - t0)
            except Exception as exception:
                result = "Error: %s" % (repr(exception))
        elif(data[0] == "reset"):
            try:
                t0 = time.time()
                self.hli.reset()
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
                self.hli.en_passant(cellA, cellB, cellTake, piece)
                t1 = time.time()
                result = "OK (%f s)" % (t1 - t0)
            except Exception as exception:
                result = "Error: %s" %(repr(exception))
        else:
            result = "Error: no action"

        # Print result and function called
        print(result)
        print("Called function: " + data[0])

        return result
