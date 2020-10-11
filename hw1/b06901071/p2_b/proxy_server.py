from socket import *
import sys

import os

if len(sys.argv) <= 1:
	print('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
	sys.exit(2)

tcpSerSock = socket(AF_INET, SOCK_STREAM)

HOST, PORT = str(sys.argv[1]), 8080
tcpSerSock.bind((HOST, PORT))
tcpSerSock.listen(5)

while 1:
	print('Ready to serve...')
	tcpCliSock, addr = tcpSerSock.accept()
	print('Received a connection from:', addr)

	message = tcpCliSock.recv(4096).decode("utf-8")
	print(message)

	filename = message.split()[1].partition("/")[2].split('?')[0]
	print(filename)

	fileExist = "false"
	filetouse = "/" + filename
	print(filetouse)
	print("==========================================") ###

	try:
		f = open(filetouse[1:], "r")
		outputdata = f.readlines()
		fileExist = "true"

		print("================response===================") ###
		for line in outputdata:
			print(line, end='') ###
			tcpCliSock.send(line.encode("utf-8"))
		tcpCliSock.send(b"\r\n")
		print('Read from cache')

	except IOError:
		if fileExist == "false":
			print("=================proxy server=================") ###
			c = socket(AF_INET, SOCK_STREAM)
			hostname = gethostname()
			hostIp = gethostbyname(hostname)

			try:
				c.connect((hostIp, 8080))
				print("connected")

				fileobj = c.makefile('rw', None)
				fileobj.write("GET /"+ filename + " HTTP/1.1\n\n")
				fileobj.flush()

				buffer = fileobj.readlines()
				print(buffer)
				
				print("================response===================") ###
				tmpFile = open(filename,"w")
				for line in buffer:
					print(line, end='') ###
					tmpFile.write(line)
					tcpCliSock.send(line.encode("utf-8"))
				tmpFile.close()
			except:
				print("Illegal request")
		else:
			print("=================404 Not Found=================") ###
			tcpCliSock.send(b"HTTP/1.1 404 Not Found")
	tcpCliSock.close()

tcpSerSock.close()
sys.exit()
