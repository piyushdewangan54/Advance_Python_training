import socket

msgfromclient = "hello udp server"

bytesTosend = str.encode(msgfromclient)

serverAddressPort = ('127.0.0.1', 20001)

buffersize = 1024

UdpClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UdpClientSocket.sendto(bytesTosend, serverAddressPort)

msgfromserver = UdpClientSocket.recvfrom(buffersize)

msg = "Message from server : {}".format(msgfromserver[0])

print(msg)