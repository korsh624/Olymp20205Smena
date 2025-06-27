import socket

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
serverAddressPort = ("192.168.42.15", 8888)
msgFromClient="l:1:1:1:1#"
# r b g

print(msgFromClient)
bytesToSend = str.encode(msgFromClient)
bufferSize = 1024
UDPClientSocket.sendto(bytesToSend, serverAddressPort)
