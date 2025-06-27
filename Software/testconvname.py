from promtools import ConveyerLineNamet
A=ConveyerLineNamet('192.168.10.21',8888,"A")
B=ConveyerLineNamet('192.168.10.21',8888,"B")
C=ConveyerLineNamet('192.168.10.21',8888,"C")
D=ConveyerLineNamet('192.168.10.21',8888,"D")
F=ConveyerLineNamet('192.168.10.21',8888,"F")

A.setSpeed(0)
B.setSpeed(0)
C.setSpeed(50)
D.setSpeed(50)
F.setSpeed(0)