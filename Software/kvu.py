import socket
import time
from promtools import Lamp
from promtools   import Manipulator
from promtools import ConveyerLine
unit=('192.168.42.13',8888)
kvu= ('192.168.42.10',8888)
kmr=Manipulator('192.168.42.241',8888)
conveer=ConveyerLine('192.168.42.49',8888)
led=Lamp('192.168.42.16',8888)

def process_up():
    led.setColor(g=1)
    conveer.setSpeed(1000)
    time.sleep(5)
    conveer.setSpeed(0)
    kmr.toPoint(200,0,200,180,1)
    kmr.toPoint(200, 100, 200, 0, 1)
    kmr.toPoint(100, 100, 200, 0, 0)
    kmr.toPoint(100, 0, 200, 0, 1)
    kmr.toPoint(200, 0, 200, 0, 0)
    led.setColor(y=1)

def udp_server(host='192.168.42.10', port=8888):
    # Создаем UDP сокет
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        # Привязываем сокет к адресу и порту
        sock.bind((host, port))
        print(f"Сервер запущен и слушает на {host}:{port}")
        while True:
            # Ожидаем получение данных
            data, addr = sock.recvfrom(1024)  # Буфер размером 1024 байта
            #print(f"Получено сообщение от {addr}: {data.decode()}")
            message=data.decode()
            print(message)
            if message=="unitstart":
                process_up()
                message=''
            
if __name__ == "__main__":
    udp_server()