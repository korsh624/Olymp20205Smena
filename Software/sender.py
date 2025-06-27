import socket
import time
unit1=('192.168.42.13',8888)
unit2= ('192.168.42.11',8888)
unit3= ('192.168.42.14',8888)
unit4= ('192.168.42.12',8888)
def udp_sender(host='192.168.42.10', port=8888, data='', addresat='' ):
    # Создаем UDP сокет
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        # Привязываем сокет к адресу и порту
        sock.bind((host, port))
        sock.sendto(data.encode(), addresat)
                 

if __name__ == "__main__":
    while True:
        udp_sender(data='unitstart', addresat=unit1)
        udp_sender(data='unitstart', addresat=unit2)
        udp_sender(data='unitstart', addresat=unit3)
        udp_sender(data='unitstart', addresat=unit4)
        time.sleep(10)
