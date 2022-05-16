#include <SPI.h>
#include <MFRC522.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#define SS_PIN 10   //SS 핀 설정
#define RST_PIN 9   //RST 핀 설정
MFRC522 rfid(SS_PIN, RST_PIN);  //클래스 객체 선언

LiquidCrystal_I2C lcd(0x27, 16, 2);
int red = 4;
int green = 5;
int blue = 6;

void setup(){
  Serial.begin(9600);
  SPI.begin();      //SPI 통신 시작
  rfid.PCD_Init();  //RFID 초기화


  lcd.init();
  lcd.backlight();
  
  Serial.println("카드를 대주세요");
  Serial.println();
  lcd.setCursor(0, 0);
  lcd.print("card");
  delay(1000);
  lcd.clear();

  pinMode(red, OUTPUT);
  pinMode(green, OUTPUT);
  pinMode(blue, OUTPUT);
}

void loop() {
  //새 카드가 인식되면 넘어감
  if(! rfid.PICC_IsNewCardPresent())
    return;
  //카드가 제대로 읽혀지면 넘어감
  if(!rfid.PICC_ReadCardSerial())
    return;

    //현재 접촉되는 카드 타입 읽어오기
    String content = "";
    byte letter;
    for(byte i = 0; i<rfid.uid.size; i++) 
    {
      content.concat(String(rfid.uid.uidByte[i] < 0x10?" 0" : " "));
      content.concat(String(rfid.uid.uidByte[i], HEX));
    }
 
    content.toUpperCase();

    //UID값이 지정해 둔 값과 같으면 출입 가능
    if(content.substring(1) == "21 CE 50 D3") //key1
    {
      digitalWrite(red, HIGH);   // 빨간색 LED ON
      delay(500);
      digitalWrite(red, LOW);    // 빨간색 LED OFF
      delay(500);
      Serial.println("출입자명: MJC");
      Serial.println("Message: 출입 가능");
      Serial.println();
      lcd.setCursor(0, 0);
      lcd.println("Hi Admin");
      delay(1000);
      lcd.clear();
    }
    //UID값이 다르면 출입금지
    else
    {
      digitalWrite(green, HIGH); // 초록색 LED ON
      delay(500);
      digitalWrite(green, LOW);  // 초록색 LED OFF
      delay(500);
      Serial.println("해당 출입자가 아닙니다");
      Serial.println("Message: 출입 금지");
      Serial.println();
      lcd.setCursor(0, 0);
      lcd.print("Not Admin");
      delay(1000);
      lcd.clear();
    }
}
