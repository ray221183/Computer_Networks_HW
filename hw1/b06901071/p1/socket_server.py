import socket

# Specify the IP addr and port number 
# (use "127.0.0.1" for localhost on local machine)
# Create a socket and bind the socket to the addr
# TODO start
# ops = {'+': (lambda x, y: x+y),
#        '-': (lambda x, y: x-y), 
#        '*': (lambda x, y: x*y),
#        '/': (lambda x, y: x/y)}
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST, PORT = "127.0.0.1", 8080
server.bind((HOST, PORT))
# TODO end

while(True):
    # Listen for any request
    # TODO start
    server.listen(5)
    # TODO end
    print("The Grading server for HW2 is running..")

    while(True):
        # Accept a new request and admit the connection
        # TODO start
        client, address = server.accept()
        # TODO end
        print(str(address)+" connected")
        try:
            while (True):
                client.send(b"Welcom to the calculator server. Input your problem ?\n")
                # Recieve the data from the client and send the answer back to the client
                # Ask if the client want to terminate the process
                # Terminate the process or continue
                # TODO start
                print("receiving question...")
                data = str(client.recv(4096), "utf-8") #receive question from client
                print("server receives: ", data)

                # question = data.split()
                ans = ("The answer is " + str(eval(data)) + ".\n").encode("utf-8")
                # ans = ("The answer is " + str(ops[question[1]](int(question[0]), int(question[2]))) + ".\n").encode("utf-8")
                client.sendall(ans + ("Do you have any question? (Y/N)\n").encode("utf-8")) #send answer back to the client

                if str(client.recv(4096), "utf-8").upper() == 'N': #check whether to continue the communication
                    client.close()
                    break
                # TODO end
        except ValueError:
            print("except")

        print("Server ends...")
        break
    break
