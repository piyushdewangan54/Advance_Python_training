import socket

localIP = '127.0.0.1'
localport = 20001

buffersize = 1024

msgFromServer = "Hello UDP client"

bytesToSend = str.encode(msgFromServer)

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPServerSocket.bind((localIP, localport))

print("UDP server up and listening...")

while True:
    bytesAddressPair = UDPServerSocket.recvfrom(buffersize)
    message= bytesAddressPair[0]
    address = bytesAddressPair[1]

    clientmsg = "Message from client : {}".format(message)
    clientIP = "Client IP address: {}".format(address)
    print(clientIP)
    print(clientmsg)
    UDPServerSocket.sendto(bytesToSend, address)