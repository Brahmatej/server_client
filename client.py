
import socket
from threading import *
ClientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "TejaK"
port = 1233

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))
name=input("Enter your name : ")
msgs=[]
def Reciver():
    while True:
        a=ClientSocket.recv(1024).decode()
        msgs.append(a)
   
t1=Thread(target=Reciver)
def Print():
    while True:
        if len(msgs)>=1:
            for i in msgs:
                print(i)
                msgs.pop(0)
  
t2=Thread(target=Print)
def Send():
    while True:
        Input =name+" : "+input()
        ClientSocket.send(str.encode(Input))
       
t3=Thread(target=Send)
t1.start()

t2.start()

t3.start()

t1.join()

Response = ClientSocket.recv(1024)
#while True:
#    Input =" "*30+name+" : "+input(" YOU : ")
#	
  #  ClientSocket.send(str.encode(Input))
   # Response = ClientSocket.recv(1024)
  #  print(Response.decode('utf-8'))

ClientSocket.close()
