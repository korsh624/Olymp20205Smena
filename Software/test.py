import socket
import time
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
serverAddressPort = ("192.168.42.241", 8888)
def moveManipulator(x, y, z, a, g):
    UDPClientSocket.sendto(str.encode("r#"), serverAddressPort)
    UDPClientSocket.sendto(str.encode(f"g:{x}:{y}:{a}:{z}:{g}#"), serverAddressPort)
def iteration():
    moveManipulator(200, 0, 200, 0, 1)
    time.sleep(2)
    moveManipulator(200, 100, 200, 0, 1)
    time.sleep(2)
    moveManipulator(100, 100, 200, 0, 1)
    time.sleep(0.1)
    moveManipulator(100, 0, 200, 0, 1)
    time.sleep(2)
    moveManipulator(200, 0, 200, 0, 1)
iteration()
print("send")