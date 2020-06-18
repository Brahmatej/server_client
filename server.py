
import socket
import os
from _thread import *

ServerSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "TejaK"
port = 1233
ThreadCount = 0
lients=[]
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')
ServerSocket.listen(5)


def threaded_client(connection):
    print("connection is ",connection)
    connection.send(str.encode('Welcome to the Server\n'))
    while True:
        data = connection.recv(2048)
        reply = data.decode('utf-8')
        if not data:
            break
       
        for i in lients:
            print(type(i))
            if connection!=i:
                i.send(str.encode(reply))
       
       
    connection.close()

while True:
    Client, address = ServerSocket.accept()
    lients.append(Client)
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client,))
   
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()