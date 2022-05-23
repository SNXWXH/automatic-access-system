#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN 10   //SS 핀 설정
#define RST_PIN 9   //RST 핀 설정

MFRC522 rfid(SS_PIN, RST_PIN);  //클래스 객체 선언

void setup() {
  Serial.begin(9600);
  SPI.begin();      //SPI 통신 시작
  rfid.PCD_Init();  //RFID 초기화
}

void loop() {
  //새 카드가 인식되면 넘어감
  if (! rfid.PICC_IsNewCardPresent())
    return;
  //카드가 제대로 읽혀지면 넘어감
  if (!rfid.PICC_ReadCardSerial())
    return;

  //현재 접촉되는 카드 타입 읽어오기
  String content = "";
  byte letter;
  for (byte i = 0; i < rfid.uid.size; i++)
  {
    content.concat(String(rfid.uid.uidByte[i] < 0x10 ? " 0" : " "));
    content.concat(String(rfid.uid.uidByte[i], HEX));
  }

  content.toUpperCase();

  //UID값이 지정해 둔 값과 같으면 출입 가능
  if (content.substring(1) == "21 CE 50 D3") //key1
  {
    same();
  }

  //UID값이 다르면 출입금지
  else
  {
    notsame();
  }
}


//출입가능 함수 선언
void same() {
  Serial.println("1");
  Serial.println();
  delay(500);
}

//출입불가능 함수 선언
void notsame() {
  Serial.println("0");
  Serial.println();
  delay(500);
}
