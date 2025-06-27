from promtools import Manipulator
from promtools import ConveyerLine, ConveyerMuver
import time
from promtools import Lamp
angle=Manipulator("192.168.42.241", 8888)
conveyerl=ConveyerLine("192.168.42.49", 8888)
led=Lamp("192.168.42.16", 8888)
led.setColor(y=1)
time.sleep(3)
led.setColor(g=1)
conveyerl.setSpeed(-100)
time.sleep(1)
conveyerl.setSpeed(0)
angle.toPoint(200,0,200,180,0)
time.sleep(5)
led.setColor(y=1)

