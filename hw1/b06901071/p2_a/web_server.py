#import socket module
from socket import *
import time
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

hostname = gethostname()
hostIp = gethostbyname(hostname)

HOST, PORT = str(hostIp), 8080 #"127.0.0.1", 8080 # 
serverSocket.bind((HOST, PORT))

while True:
    print('Ready to serve...')
    serverSocket.listen(5)
    try:
        connectionSocket, clientAddress = serverSocket.accept()
        message = connectionSocket.recv(4096).decode("utf-8")
        print("message:\n", message) ###

        filename = message.split()[1]
        print("filename:\n" + filename[1:].split("?")[0])
        f = open(filename[1:].split("?")[0])

        outputdata = f.readlines()
        print("outputdata:\n", outputdata)

        connectionSocket.send(b"HTTP/1.1 200 OK\r\n\r\n")

        for i in range(0, len(outputdata)):
            print(outputdata[i])
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()

    except IOError:
        connectionSocket.sendall(b"HTTP/1.1 404 Not Found\r\n")
        connectionSocket.close()

serverSocket.close()
sys.exit() #Terminate the program after sending the corresponding data
