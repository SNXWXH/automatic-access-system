#include <SPI.h>
#include <MFRC522.h>
#define SS_PIN 10  //SS 핀 설정
#define RST_PIN 9  //RST 핀 설정
 
MFRC522 rfid(SS_PIN, RST_PIN);  //클래스 객체 선언
MFRC522::MIFARE_Key key;

byte nuidPICC[4];  //카드 ID들을 저장하기 위한 변수 선언

void setup() { 
  Serial.begin(9600);
  SPI.begin();  //SPI 통신 시작
  rfid.PCD_Init();  //RFID 초기화

  //ID 값 초기화
  for (byte i = 0; i < 6; i++) {
    key.keyByte[i] = 0xFF;
  }
  Serial.println("카드를 대주세요");
}
 
void loop() {
  //새 카드가 인식되면 넘어감
  if ( ! rfid.PICC_IsNewCardPresent())
    return;
  //카드가 제대로 읽혀지면 넘어감
  if ( ! rfid.PICC_ReadCardSerial())
    return;
    
  //현재 접촉되는 카드 타입을 읽어와 모니터에 출력
  Serial.println();
  Serial.print(F("PICC type: "));
  MFRC522::PICC_Type piccType = rfid.PICC_GetType(rfid.uid.sak);
  Serial.println(rfid.PICC_GetTypeName(piccType));

  //MIFARE 방식의 카드인지 확인 루틴
  if (piccType != MFRC522::PICC_TYPE_MIFARE_MINI &&  
    piccType != MFRC522::PICC_TYPE_MIFARE_1K &&
    piccType != MFRC522::PICC_TYPE_MIFARE_4K) {
    Serial.println("MIFARE 방식의 카드가 아닙니다.");
    return;
  }

  //이전 인식된 카드와 다른 카드 혹은 새 카드가 인식 될 경우
  if (rfid.uid.uidByte[0] != nuidPICC[0] || 
    rfid.uid.uidByte[1] != nuidPICC[1] || 
    rfid.uid.uidByte[2] != nuidPICC[2] || 
    rfid.uid.uidByte[3] != nuidPICC[3] ) {
    Serial.println("새로운 카드가 감지되었습니다.");

    //고유 UID 저장
    for (byte i = 0; i < 4; i++) {
      nuidPICC[i] = rfid.uid.uidByte[i];
    }

    Serial.println(F("The NUID tag is:"));
    //저장된 UID 값을 16진수로 출력
    Serial.print(F("16진수: "));
    printHex(rfid.uid.uidByte, rfid.uid.size);
    Serial.println();
    //저장된 UID 값을 10진수로 출력
    Serial.print(F("10진수: "));
    printDec(rfid.uid.uidByte, rfid.uid.size);
    Serial.println();
  }
  //연속으로 동일한 카드 접촉 시 이미 인식된 카드라는 메시지 출력
  else Serial.println("이미 인식된 카드 입니다");
  rfid.PICC_HaltA();
  rfid.PCD_StopCrypto1();
}

//16진수로 변환하는 함수
void printHex(byte *buffer, byte bufferSize) {
  for (byte i = 0; i < bufferSize; i++) {
    Serial.print(buffer[i] < 0x10 ? " 0" : " ");
    Serial.print(buffer[i], HEX);
  }
}

//10진수로 변환하는 함수
void printDec(byte *buffer, byte bufferSize) {
  for (byte i = 0; i < bufferSize; i++) {
    Serial.print(buffer[i] < 0x10 ? " 0" : " ");
    Serial.print(buffer[i], DEC);
  }
}
