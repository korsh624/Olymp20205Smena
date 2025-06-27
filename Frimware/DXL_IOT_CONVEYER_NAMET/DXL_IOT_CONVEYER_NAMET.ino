#include "DxlMaster.h"

#include <Ethernet.h>
#include <EthernetUdp.h>
#include <EEPROM.h>

#define DXL_BAUDRATE 1000000
#define DXL_ID_A 21
#define DXL_ID_B 22
#define DXL_ID_C 23
#define DXL_ID_D 24
#define DXL_ID_E 25
#define DXL_ID_F 26
#define DXL_REG 27
#define UDP_PORT 8888

IPAddress MyIP(192, 168, 10, 21);

EthernetUDP udp;
char packetBuffer[UDP_TX_PACKET_MAX_SIZE];
byte mac[6];

byte serialBuffer[15];

DynamixelMotor motorA((byte)DXL_ID_A);
DynamixelMotor motorB((byte)DXL_ID_B);
DynamixelMotor motorC((byte)DXL_ID_C);
DynamixelMotor motorD((byte)DXL_ID_D);
DynamixelMotor motorE((byte)DXL_ID_E);
DynamixelMotor motorF((byte)DXL_ID_F);

void setup() {
  DxlMaster.begin(DXL_BAUDRATE);
  motorA.init();
  motorA.wheelMode();
  motorB.init();
  motorB.wheelMode();
  motorC.init();
  motorC.wheelMode();
  motorD.init();
  motorD.wheelMode();
  motorE.init();
  motorE.wheelMode();
  motorF.init();
  motorF.wheelMode();
  Serial.begin(115200);
  //Считываем данные из EEPROM и представляем их как IP адреса
  //IP адрес модуля
  // for (int addr = 0; addr < 4; addr++) {
  //   MyIP[addr] = EEPROM.read(addr);
  // }
  mac[0] = MyIP[0];
  mac[1] = MyIP[1];
  mac[2] = MyIP[2];
  mac[3] = MyIP[3];
  mac[4] = MyIP[2];
  mac[5] = MyIP[3];
  Serial.begin(115200);
  Ethernet.begin(mac, MyIP);
  udp.begin(UDP_PORT);
  Serial.println("----------------------");
  Serial.println("UDP connection is at: ");
  Serial.println(Ethernet.localIP());
  // Serial.println("Type 1 to change localIP");  
  Serial.println("----------------------");
}

int16_t parseSpeed(){
  int16_t result;
  String str = "";
  bool valFound = false;
  for(int i = 2; i < 6; i++){
    if(packetBuffer[i] > '0' || packetBuffer[i] < '9' || packetBuffer[i] == '-'){
      str += (String)packetBuffer[i];
      result = str.toInt();      
    } else {
      return result;      
    }
  }
  return result;
}

void processUdp(){
int packetSize = udp.parsePacket();
  if (packetSize) {
    Serial.print("From ");
    IPAddress remote = udp.remoteIP();
    for (int i = 0; i < 4; i++) {
      Serial.print(remote[i], DEC);
      if (i < 3) {
        Serial.print(".");
      }
    }
    Serial.print(", port ");
    Serial.println(udp.remotePort());
    udp.read(packetBuffer, UDP_TX_PACKET_MAX_SIZE);
    Serial.println("Contents:");
    Serial.println(packetBuffer);
    if(
        packetBuffer[0] == 'A' &&
        packetBuffer[1] == ':'
      ) {
        motorA.speed(parseSpeed());
    }
    if(
        packetBuffer[0] == 'B' &&
        packetBuffer[1] == ':'
      ) {
        motorB.speed(parseSpeed());
    }
    if(
        packetBuffer[0] == 'C' &&
        packetBuffer[1] == ':'
      ) {
        motorC.speed(parseSpeed());
    }
    if(
        packetBuffer[0] == 'D' &&
        packetBuffer[1] == ':'
      ) {
        motorD.speed(parseSpeed());
    }
    if(
        packetBuffer[0] == 'E' &&
        packetBuffer[1] == ':'
      ) {
        motorE.speed(parseSpeed());
    }
    if(
        packetBuffer[0] == 'F' &&
        packetBuffer[1] == ':'
      ) {
        motorF.speed(parseSpeed());
    }

    
  }  
}

void loop() {

  processUdp();
}
