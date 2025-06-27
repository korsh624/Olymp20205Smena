from promtools import Manipulator
from promtools import ConveyerLine, ConveyerMuver
import time
from promtools import Lamp
conv1=ConveyerLine("192.168.10.25", 8888)
angle1=Manipulator("192.168.10.11", 8888,"g")
angle2=Manipulator("192.168.10.12", 8888,"g")
pp1=Manipulator("192.168.10.13", 8888,"p")
angle3=Manipulator("192.168.10.14", 8888,"g")
pp2=Manipulator("192.168.10.15", 8888,"p")
angle4=Manipulator("192.168.10.16", 8888,"g")
time.sleep(2)
conv1.setSpeed(0)




