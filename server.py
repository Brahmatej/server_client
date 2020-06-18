
import socket #importing the socket module
import os #importing os module this comunicates with over current operating system
from _thread import * #we are iporting all the functions from the  threads module

ServerSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#creating a socket
host = "TejaK"# assigining host address you can use any ip address you want
port = 1233# assigining the ort number
ThreadCount = 0#this counts the number of threads i.e when a client is connected this gets incremented by 1
lients=[]# this collects the client objects for sending the messages to the other clients connected to the server
try:
    ServerSocket.bind((host, port))#this try to bind the host id and the port for the server to run on if not it through's an error
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')
ServerSocket.listen(5)# this one specifies to how many clients it can connect here i have given 5 but you can give any other number
#when a new client is connected the following function runns and used for communication between the clients

def threaded_client(connection):
    print("connection is ",connection)
    connection.send(str.encode('Welcome to the Server\n'))
    while True:
        data = connection.recv(2048)
        reply = data.decode('utf-8')
        if not data:
            break#the above while function untill unless a string is been recieved if it recieves an empty string it breakes
       
        for i in lients:#this for loop sends the recieved message to all the other clients connected to the server 
            print(type(i))
            if connection!=i:
                i.send(str.encode(reply))
       
       
    connection.close()#offcourse this closes the connection

while True:#this is the while loop responsible for connecting to multiple servers until it reaches limit
    Client, address = ServerSocket.accept()
    lients.append(Client)
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client,))
   
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()
