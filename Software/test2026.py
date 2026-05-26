import time
from promtools import Manipulator
man1=Manipulator('192.168.42.3',8888,'g')
man1.toPoint(200,0,200,0,1)
time.sleep(2)
man1.toPoint(200,0,3,0,0)
time.sleep(2)
man1.toPoint(200,0,10,0,1)
time.sleep(2)
man1.toPoint(200,0,200,0,1)

