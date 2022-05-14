#include <Adafruit_Fingerprint.h>
#include <LiquidCrystal_I2C.h>
#include <Wire.h>
#include<Servo.h> //Servo 라이브러리를 추가
Servo servo;      //Servo 클래스로 servo객체 생성

//핀 정의
int red = 9;
int green = 10;
int blue = 11;
int servoPin = 7; //0도에 열고 180도에 닫고
//서보 모터 각도 조절을 위한 변수
bool flag = false;
LiquidCrystal_I2C lcd(0x3F, 16, 2);

SoftwareSerial mySerial(2, 3);

Adafruit_Fingerprint finger = Adafruit_Fingerprint(&mySerial);

void setup()  
{
  pinMode(red, OUTPUT);
  pinMode(green, OUTPUT);
  pinMode(blue, OUTPUT);
  lcd.init();
  lcd.backlight();
  servo.attach(servoPin);  
  servo.write(180);   
  Serial.begin(9600);
  while (!Serial);  // For Yun/Leo/Micro/Zero/...
  delay(100);
  Serial.println("\n\nAdafruit finger detect test");

  finger.begin(57600);
  delay(5);
  if (finger.verifyPassword()) {
    Serial.println("Found fingerprint sensor!");
  } else {
    Serial.println("Did not find fingerprint sensor :(");
    while (1) { delay(1); }
  }

  finger.getTemplateCount();
  Serial.print("Sensor contains "); Serial.print(finger.templateCount); Serial.println(" templates");
  Serial.println("Waiting for valid finger...");
}

void loop()                     // run over and over again
{  
  getFingerprintIDez();
  if(flag) {
    servo.write(1); 
    delay(1000);
  }
  if(finger.fingerID != 1 && finger.fingerID != 2) {
    digitalWrite(red, HIGH);
    delay(500);
    digitalWrite(red, LOW);
  }
}

uint8_t getFingerprintID() {
  uint8_t p = finger.getImage();
  switch (p) {
    case FINGERPRINT_OK:
      Serial.println("Image taken");
      break;
    case FINGERPRINT_NOFINGER:
      Serial.println("No finger detected");
      return p;
    case FINGERPRINT_PACKETRECIEVEERR:
      Serial.println("Communication error");
      return p;
    case FINGERPRINT_IMAGEFAIL:
      Serial.println("Imaging error");
      return p;
    default:
      Serial.println("Unknown error");
      return p;
  }

  // OK success!

  p = finger.image2Tz();
  switch (p) {
    case FINGERPRINT_OK:
      Serial.println("Image converted");
      break;
    case FINGERPRINT_IMAGEMESS:
      Serial.println("Image too messy");
      return p;
    case FINGERPRINT_PACKETRECIEVEERR:
      Serial.println("Communication error");
      return p;
    case FINGERPRINT_FEATUREFAIL:
      Serial.println("Could not find fingerprint features");
      return p;
    case FINGERPRINT_INVALIDIMAGE:
      Serial.println("Could not find fingerprint features");
      return p;
    default:
      Serial.println("Unknown error");
      return p;
  }
  
  // OK converted!
  p = finger.fingerFastSearch();
  if (p == FINGERPRINT_OK) {
    Serial.println("Found a print match!");
  } else if (p == FINGERPRINT_PACKETRECIEVEERR) {
    Serial.println("Communication error");
    return p;
  } else if (p == FINGERPRINT_NOTFOUND) {
    Serial.println("Did not find a match");
    return p;
  } else {
    Serial.println("Unknown error");
    return p;
  }   
  
  // found a match!
  Serial.print("Found ID #"); Serial.print(finger.fingerID); 
  Serial.print(" with confidence of "); Serial.println(finger.confidence); 

  return finger.fingerID;
}

// returns -1 if failed, otherwise returns ID #
int getFingerprintIDez() {
  uint8_t p = finger.getImage();
  if (p != FINGERPRINT_OK)  {
    Serial.println("Waiting");
    return -1;
  }

  p = finger.image2Tz();
  if (p != FINGERPRINT_OK) {
    Serial.println("22");
    return -1;
  }

  p = finger.fingerFastSearch();
  if (p != FINGERPRINT_OK) {
    Serial.println("Not Admin");
    lcd.print("Not Admin");
    flag = false;
    servo.write(179);
    return -1;
    digitalWrite(red, HIGH);
    delay(500);
    digitalWrite(red, LOW);
  }

  if(finger.confidence >= 100){
    Serial.println("Hi Admin");
    lcd.print("Hi Admin");
    digitalWrite(green, HIGH);
    delay(500);
    digitalWrite(green, LOW);
    flag=true;
   }
  else{
    Serial.println("retouch"); 
  }
  return finger.fingerID;
  
  // found a match!
  Serial.print("Found ID #"); Serial.print(finger.fingerID); 
  Serial.print(" with confidence of "); Serial.println(finger.confidence);
}
