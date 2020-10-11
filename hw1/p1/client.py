import socket

# Specify the IP addr and port number 
# (use "127.0.0.1" for localhost on local machine)
# Create a socket and bind the socket to the addr
# TODO start
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST, PORT = "127.0.0.1", 8080 #"140.112.42.98", 7777 #
client.connect((HOST, PORT))
# TODO end

print("Connected to 127.0.0.1\n", end="")
while(True):
    # input user's question
    print("Receive server message:")
    recv_data = client.recv(4096)
    print(str(recv_data, "utf-8"), end="")

    question = input()
    question = question.encode("utf-8")
    client.sendall(question)

    print("Receive server message:")
    recv_data = client.recv(4096)
    print(str(recv_data, "utf-8"), end="")

    continue_or_not = input()
    client.sendall(continue_or_not.encode("utf-8"))

    if continue_or_not.upper() == "N":
        break


